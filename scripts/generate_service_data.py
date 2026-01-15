#!/usr/bin/env python3
"""Generate realistic service issue data using Claude AI with Pydantic structured output."""

import json
import os
import re
import click
from anthropic import Anthropic
from pydantic import BaseModel, Field

# Pydantic models for structured output
class ServiceIssue(BaseModel):
	"""A single service issue with problem, solution, and parts."""
	problem: str = Field(description="Conversational problem description as a restaurant worker would describe it (2-4 sentences, everyday language, not technical jargon)")
	solution: str = Field(description="Detailed repair solution applied (1-2 sentences)")
	parts: list[str] = Field(description="List of 1-3 replacement parts, each with SKU prefix format: 'SKU-XX-###### - Part Name with specs'")


class ServiceIssueList(BaseModel):
	"""List of service issues for a category."""
	issues: list[ServiceIssue] = Field(description="List of service repair scenarios")


# Machine categories with context for realistic generation
CATEGORY_CONTEXT = {
	"Ovens": {
		"description": "Commercial ovens including convection, combi-steam, deck, and rapid-bake ovens",
		"subsystems": [
			"heating elements (electric) or burners (gas)",
			"temperature control (thermocouples, RTDs, controllers)",
			"convection systems (fans, motors, ducting)",
			"door seals, latches, and hinges",
			"control boards and interfaces",
			"steam injection systems (combi ovens)",
			"safety systems (high-limit, flame sensors)",
			"ignition systems (pilot, electronic)",
			"timers and programmable controls",
			"stone decks and baking surfaces",
		],
	},
	"Fryers": {
		"description": "Commercial deep fryers including gas and electric models with filtration systems",
		"subsystems": [
			"heating elements or gas burners",
			"oil temperature control and thermostats",
			"high-limit safety switches",
			"oil filtration and pump systems",
			"basket lift mechanisms",
			"gas valves and solenoids",
			"temperature probes and sensors",
			"drain valves and plumbing",
			"control panels and timers",
			"vat and tank components",
		],
	},
	"Mixers": {
		"description": "Commercial planetary and spiral mixers for dough and food preparation",
		"subsystems": [
			"motors and motor controls",
			"gearboxes and transmissions",
			"planetary gear assemblies",
			"bowl lift and lock mechanisms",
			"speed controllers and VFDs",
			"safety interlocks and guards",
			"attachment hubs and drives",
			"bearings and bushings",
			"electrical contactors and capacitors",
			"lubrication systems",
		],
	},
	"Refrigeration": {
		"description": "Commercial refrigerators, freezers, walk-ins, and display cases",
		"subsystems": [
			"compressors and start components",
			"evaporator coils and fans",
			"condenser coils and fans",
			"defrost systems (heaters, timers)",
			"thermostats and temperature controls",
			"refrigerant circuits and TXVs",
			"door gaskets and seals",
			"drain systems and heaters",
			"electrical controls and relays",
			"insulation and cabinet components",
		],
	},
	"Dishwashers": {
		"description": "Commercial dishwashers including door-type, conveyor, and undercounter models",
		"subsystems": [
			"wash pumps and motors",
			"booster heaters for sanitizing",
			"spray arms and nozzles",
			"chemical dispensers (detergent, rinse aid)",
			"drain pumps and valves",
			"door mechanisms and solenoids",
			"cycle controllers and timers",
			"water fill valves and sensors",
			"exhaust and ventilation systems",
			"tank heaters and thermostats",
		],
	},
	"Griddles": {
		"description": "Commercial flat-top griddles including gas, electric, and chrome-top models",
		"subsystems": [
			"heating elements or gas burners",
			"thermostats and temperature controls",
			"griddle plates and cooking surfaces",
			"ignition systems (pilot, electronic)",
			"grease management (traps, channels)",
			"control valves and knobs",
			"thermocouples and safety devices",
			"burner manifolds and orifices",
			"surface leveling and mounting",
			"backsplash and splash guards",
		],
	},
}

GENERATION_PROMPT = """You are generating service repair scenarios for {category} equipment in commercial kitchens.

Equipment context: {description}

Key subsystems to cover: {subsystems}

For each scenario, provide:
1. "problem": A conversational problem description as a RESTAURANT WORKER (not a technician) would describe it. Write 2-4 sentences using everyday language, not technical jargon. Include what they noticed, how it affects their work, and any frustration.

   GOOD example: "The oven won't hold temperature anymore - I set it to 350 but the food keeps coming out burnt on one side and raw on the other. My cooks are complaining they can't get consistent results. It's been getting worse over the past week."

   BAD example: "Convection oven temperature fluctuating wildly between 250°F and 450°F despite thermostat set to 350°F."

2. "solution": The detailed repair solution applied (1-2 sentences, include what was done)

3. "parts": A list of 1-3 replacement parts. EACH part MUST include a SKU prefix in this exact format:
   "SKU-XX-###### - Part Name with specifications"

   Where XX is a 2-letter category code (e.g., TC for thermocouple, MT for motor, HE for heating element) and ###### is a 6-digit number.

   Example: "SKU-TC-001834 - Thermocouple Type K 18-inch with 1/4-inch NPT fitting"

Requirements:
- Problems should sound like a restaurant manager or cook describing issues to a repair company
- Use casual language, mention impact on operations, express frustration naturally
- Solutions must logically fix the stated problem (these can remain technical)
- Parts MUST have the SKU-XX-###### prefix format
- Use 1-3 parts per issue (vary the count)
- Cover different subsystems - don't repeat the same type of problem
- Vary the severity (minor adjustments to major repairs)
{existing_clause}

Use the generate_service_issues tool to return your response."""


def extract_json_from_response(text: str) -> str:
	"""Extract JSON from response, handling markdown code blocks."""
	# Try to find JSON in code blocks first
	code_block_match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text)
	if code_block_match:
		return code_block_match.group(1).strip()

	# Try to find a JSON array directly
	array_match = re.search(r"\[[\s\S]*\]", text)
	if array_match:
		return array_match.group(0)

	# Return original text as fallback
	return text.strip()


def generate_issues_for_category(
	client: Anthropic,
	category: str,
	count: int,
	existing_problems: list[str] | None = None,
) -> list[dict]:
	"""Generate service issues for a category using Claude with tool use."""
	context = CATEGORY_CONTEXT[category]

	existing_clause = ""
	if existing_problems:
		existing_clause = f"\n- AVOID duplicating these existing problems:\n{chr(10).join(f'  - {p}' for p in existing_problems[:20])}"

	prompt = GENERATION_PROMPT.format(
		count=count,
		category=category,
		description=context["description"],
		subsystems=", ".join(context["subsystems"]),
		existing_clause=existing_clause,
	)

	# Define the tool for structured output
	tools = [
		{
			"name": "generate_service_issues",
			"description": "Generate a list of service repair scenarios with problems, solutions, and parts",
			"input_schema": ServiceIssueList.model_json_schema(),
		}
	]

	message = client.messages.create(
		model="claude-sonnet-4-20250514",
		max_tokens=4096,
		tools=tools,
		tool_choice={"type": "tool", "name": "generate_service_issues"},
		messages=[{"role": "user", "content": prompt}],
	)

	# Extract tool use response
	for block in message.content:
		if block.type == "tool_use" and block.name == "generate_service_issues":
			try:
				# Validate with Pydantic
				result = ServiceIssueList.model_validate(block.input)
				return [issue.model_dump() for issue in result.issues]
			except Exception as e:
				click.echo(f"  Validation error: {e}", err=True)
				# Try to extract issues directly from the input
				if "issues" in block.input:
					return block.input["issues"]
				return []

	click.echo("  No tool use found in response", err=True)
	return []


def validate_issues(issues: list[dict]) -> list[dict]:
	"""Validate and clean up generated issues."""
	valid = []
	for issue in issues:
		if not all(k in issue for k in ["problem", "solution", "parts"]):
			continue
		if not isinstance(issue["parts"], list) or len(issue["parts"]) < 1:
			continue
		if len(issue["problem"]) < 10 or len(issue["solution"]) < 10:
			continue
		valid.append(issue)
	return valid


@click.command()
@click.option(
	"--category",
	"-c",
	type=click.Choice(list(CATEGORY_CONTEXT.keys())),
	help="Generate for specific category (default: all)",
)
@click.option(
	"--count",
	"-n",
	default=50,
	help="Number of issues to generate per category",
)
@click.option(
	"--output",
	"-o",
	default="generated_data",
	help="Output directory for JSON files",
)
@click.option(
	"--batch-size",
	"-b",
	default=15,
	help="Number of issues per API call (to ensure quality)",
)
@click.option(
	"--merge-to-constants",
	is_flag=True,
	help="After generation, output Python code to paste into constants.py",
)
def main(category, count, output, batch_size, merge_to_constants):
	"""Generate realistic service issue data using Claude AI."""
	api_key = os.environ.get("ANTHROPIC_API_KEY")
	if not api_key:
		click.echo("Error: ANTHROPIC_API_KEY environment variable not set", err=True)
		raise SystemExit(1)

	client = Anthropic(api_key=api_key)

	# Create output directory
	os.makedirs(output, exist_ok=True)

	categories = [category] if category else list(CATEGORY_CONTEXT.keys())
	all_data = {}

	for cat in categories:
		click.echo(f"\nGenerating issues for {cat}...")
		all_issues = []
		existing_problems = []

		# Generate in batches
		remaining = count
		retries = 0
		max_retries = 3

		while remaining > 0 and retries < max_retries:
			batch = min(batch_size, remaining)
			click.echo(f"  Generating batch of {batch} issues...")

			issues = generate_issues_for_category(
				client, cat, batch, existing_problems
			)
			issues = validate_issues(issues)

			if not issues:
				retries += 1
				click.echo(f"  Warning: No valid issues in this batch (retry {retries}/{max_retries})", err=True)
				continue

			retries = 0  # Reset retries on success
			all_issues.extend(issues)
			existing_problems.extend([i["problem"] for i in issues])
			remaining -= len(issues)
			click.echo(f"  Got {len(issues)} valid issues ({len(all_issues)} total)")

		# Deduplicate by problem text
		seen = set()
		unique_issues = []
		for issue in all_issues:
			prob_key = issue["problem"].lower().strip()
			if prob_key not in seen:
				seen.add(prob_key)
				unique_issues.append(issue)

		all_data[cat] = unique_issues
		click.echo(f"  Final: {len(unique_issues)} unique issues for {cat}")

		# Save individual category file
		output_file = os.path.join(output, f"{cat.lower()}.json")
		with open(output_file, "w") as f:
			json.dump(unique_issues, f, indent=2)
		click.echo(f"  Saved to {output_file}")

	# Save combined file
	combined_file = os.path.join(output, "all_issues.json")
	with open(combined_file, "w") as f:
		json.dump(all_data, f, indent=2)
	click.echo(f"\nSaved combined data to {combined_file}")

	# Output Python code if requested
	if merge_to_constants:
		click.echo("\n" + "=" * 60)
		click.echo("Python code to add to constants.py:")
		click.echo("=" * 60 + "\n")
		click.echo("SERVICE_ISSUES = {")
		for cat, issues in all_data.items():
			click.echo(f'\t"{cat}": [')
			for issue in issues:
				parts_str = json.dumps(issue["parts"])
				click.echo(f"\t\t{{")
				click.echo(f'\t\t\t"problem": {json.dumps(issue["problem"])},')
				click.echo(f'\t\t\t"solution": {json.dumps(issue["solution"])},')
				click.echo(f'\t\t\t"parts": {parts_str},')
				click.echo(f"\t\t}},")
			click.echo(f"\t],")
		click.echo("}")


if __name__ == "__main__":
	main()

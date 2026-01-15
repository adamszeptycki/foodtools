#!/usr/bin/env python3
"""Generate service documents for a specific part SKU."""

import click
import os
import random
from src.data_generator import ServiceDocumentDataGenerator
from src.pdf_generator import ServiceDocumentPDFGenerator
from src.constants import MACHINE_CATEGORIES, SERVICE_ISSUES


def find_part_by_sku(sku: str):
	"""
	Find part info by SKU prefix.

	Args:
		sku: The SKU to search for (e.g., "SKU-TC-001234")

	Returns:
		Tuple of (category, issue, part_name) or None if not found
	"""
	sku_lower = sku.lower()
	for category, issues in SERVICE_ISSUES.items():
		for issue in issues:
			for part in issue["parts"]:
				if part.lower().startswith(sku_lower):
					return (category, issue, part)
	return None


def list_available_skus():
	"""List all available SKUs in the system."""
	skus = []
	for category, issues in SERVICE_ISSUES.items():
		for issue in issues:
			for part in issue["parts"]:
				if part.lower().startswith("sku-"):
					sku = part.split(" - ")[0] if " - " in part else part[:15]
					skus.append((sku, category, part))
	return skus


@click.command()
@click.argument("sku", required=False)
@click.option("--count", "-n", default=5, help="Number of documents to generate")
@click.option("--output", "-o", default="output_sku", help="Output directory")
@click.option("--list", "-l", "list_skus", is_flag=True, help="List available SKUs")
@click.option("--verbose", "-v", is_flag=True, help="Verbose output")
def main(sku, count, output, list_skus, verbose):
	"""Generate service documents using a specific part SKU.

	Example: generate_by_sku.py SKU-TC-001234 --count 10
	"""
	# List mode
	if list_skus:
		skus = list_available_skus()
		if not skus:
			click.echo("No SKUs found. Parts may not have SKU prefixes yet.")
			click.echo("Run generate_service_data.py to generate parts with SKUs.")
			return

		click.echo(f"Available SKUs ({len(skus)} total):\n")
		for sku_code, category, part_name in skus[:20]:
			click.echo(f"  {sku_code:<16} [{category}] {part_name[:50]}...")
		if len(skus) > 20:
			click.echo(f"\n  ... and {len(skus) - 20} more")
		return

	# Generate mode - SKU required
	if not sku:
		click.echo("Error: SKU argument required. Use --list to see available SKUs.", err=True)
		raise SystemExit(1)

	result = find_part_by_sku(sku)
	if not result:
		click.echo(f"Error: SKU '{sku}' not found in SERVICE_ISSUES", err=True)
		click.echo("Use --list to see available SKUs", err=True)
		raise SystemExit(1)

	category, issue, part_name = result
	models = MACHINE_CATEGORIES[category]["models"]

	click.echo(f"Found part: {part_name}")
	click.echo(f"Category: {category}")
	click.echo(f"Available models: {', '.join(models)}")
	click.echo(f"\nGenerating {count} documents...")

	os.makedirs(output, exist_ok=True)
	data_gen = ServiceDocumentDataGenerator()
	pdf_gen = ServiceDocumentPDFGenerator(output_dir=output)

	for i in range(count):
		# Generate base record but override with specific part/machine
		data = data_gen.generate_service_record()
		data["machine_type"] = category
		data["machine_model"] = random.choice(models)
		data["problem_description"] = issue["problem"]
		data["solution_applied"] = issue["solution"]
		data["parts_used"] = part_name  # Always use this specific part

		filename = f"sku_{sku.replace('-', '_')}_{i+1:04d}.pdf"
		pdf_gen.generate_pdf(data, filename)

		if verbose:
			click.echo(f"  [{i+1}/{count}] {filename}")
			click.echo(f"    Machine: {data['machine_model']}")
			click.echo(f"    Client: {data['client_name']}")
		else:
			click.echo(f"  Generated: {filename}")

	click.echo(f"\nDone! {count} documents saved to '{output}/'")


if __name__ == "__main__":
	main()

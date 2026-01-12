#!/usr/bin/env python3
"""Generate realistic service document PDFs for FoodTools."""

import click
import os
from pathlib import Path
from src.data_generator import ServiceDocumentDataGenerator
from src.pdf_generator import ServiceDocumentPDFGenerator


@click.command()
@click.option("--count", "-n", default=10, help="Number of documents to generate")
@click.option("--output", "-o", default="output", help="Output directory")
@click.option("--seed", "-s", type=int, help="Random seed for reproducibility")
@click.option("--verbose", "-v", is_flag=True, help="Verbose output")
def generate(count, output, seed, verbose):
	"""Generate realistic service document PDFs for FoodTools."""

	# Create output directory
	os.makedirs(output, exist_ok=True)

	# Initialize generators
	data_gen = ServiceDocumentDataGenerator(seed=seed)
	pdf_gen = ServiceDocumentPDFGenerator(output_dir=output)

	click.echo(f"Generating {count} service documents...")
	click.echo(f"Output directory: {output}")

	if seed:
		click.echo(f"Using random seed: {seed}")

	click.echo("")

	# Generate documents
	for i in range(count):
		# Generate data
		data = data_gen.generate_service_record()

		# Create filename
		filename = f"service_doc_{i+1:04d}.pdf"

		# Generate PDF
		filepath = pdf_gen.generate_pdf(data, filename)

		if verbose:
			click.echo(f"  [{i+1}/{count}] Generated: {filename}")
			click.echo(f"    - Client: {data['client_name']}")
			click.echo(
				f"    - Machine: {data['machine_model']} ({data['machine_type']})"
			)
			click.echo(f"    - Problem: {data['problem_description'][:50]}...")
			click.echo("")

	# Calculate total size
	total_size = sum(f.stat().st_size for f in Path(output).glob("*.pdf"))

	click.echo("")
	click.echo(f"Successfully generated {count} documents in '{output}/'")
	click.echo(f"Total size: {total_size / 1024:.1f} KB")


if __name__ == "__main__":
	generate()

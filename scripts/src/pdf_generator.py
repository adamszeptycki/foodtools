"""Generate professional-looking service document PDFs using Markdown and WeasyPrint."""

import markdown
from weasyprint import HTML, CSS
from datetime import datetime
import os


class ServiceDocumentPDFGenerator:
	"""Generate professional-looking service document PDFs from Markdown."""

	def __init__(self, output_dir="output"):
		"""
		Initialize the PDF generator.

		Args:
			output_dir (str): Directory to save generated PDFs
		"""
		self.output_dir = output_dir
		self.css = self._get_stylesheet()
		self.md = markdown.Markdown(extensions=["tables"])

	def generate_pdf(self, data, filename=None):
		"""
		Generate a service document PDF from data.

		Args:
			data (dict): Service record data from ServiceDocumentDataGenerator
			filename (str, optional): Output filename. Auto-generated if None.

		Returns:
			str: Path to the generated PDF file
		"""
		if filename is None:
			timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
			filename = f"service_doc_{timestamp}.pdf"

		filepath = os.path.join(self.output_dir, filename)

		# Generate markdown content
		md_content = self._generate_markdown(data)

		# Convert markdown to HTML
		html_body = self.md.convert(md_content)
		self.md.reset()  # Reset for next conversion

		# Wrap in full HTML document
		html_content = f"""
		<!DOCTYPE html>
		<html>
		<head>
			<meta charset="utf-8">
			<title>Service Report - {data['work_order']}</title>
		</head>
		<body>
			{html_body}
		</body>
		</html>
		"""

		# Render to PDF
		HTML(string=html_content).write_pdf(filepath, stylesheets=[CSS(string=self.css)])

		return filepath

	def _generate_markdown(self, data):
		"""Generate markdown content from service data."""
		# Format the date
		service_date = data["service_date"]
		if hasattr(service_date, "strftime"):
			date_str = service_date.strftime("%m/%d/%Y")
		else:
			date_str = str(service_date)

		# Format address (replace newlines with comma-space for inline display)
		address = data["client_address"].replace("\n", ", ")

		# Format parts list
		if data["parts_used"]:
			parts = data["parts_used"].split(", ")
			parts_list = "\n".join(f"- {part}" for part in parts)
		else:
			parts_list = "- No parts replaced"

		# Build markdown document
		md_content = f"""# {data['company']}

## SERVICE REPORT

**Work Order:** {data['work_order']} | **Date:** {date_str}

---

## Client Information

| | |
|---|---|
| **Client** | {data['client_name']} |
| **Address** | {address} |
| **Phone** | {data['client_phone']} |

## Equipment Information

| Field | Value |
|-------|-------|
| Machine Type | {data['machine_type']} |
| Model | {data['machine_model']} |
| Serial Number | {data['serial_number']} |

## Service Details

### Problem Description

{data['problem_description']}

### Solution Applied

{data['solution_applied']}

## Parts Used

{parts_list}

## Technician Information

| | |
|---|---|
| **Technician Name** | {data['technician']['name']} |
| **Technician ID** | {data['technician']['id']} |
| **Certification** | {data['technician']['cert']} |
| **Arrival Time** | {data['arrival_time']} |
| **Labor Hours** | {data['labor_hours']} |

---

**Technician Signature:** _______________________________ **Date:** _______________

---

*{data['company']} | 24/7 Service | (555) 123-4567*

*www.foodservicetech.com | service@foodservicetech.com*
"""
		return md_content

	def _get_stylesheet(self):
		"""Return CSS stylesheet for PDF rendering."""
		return """
		@page {
			size: letter;
			margin: 0.75in;
		}

		body {
			font-family: Helvetica, Arial, sans-serif;
			font-size: 10pt;
			line-height: 1.4;
			color: #333;
		}

		h1 {
			font-size: 18pt;
			margin-bottom: 0.25em;
			color: #222;
		}

		h2 {
			font-size: 14pt;
			margin-top: 1.25em;
			margin-bottom: 0.5em;
			padding-bottom: 0.25em;
			border-bottom: 1px solid #ccc;
		}

		h3 {
			font-size: 11pt;
			margin-top: 1em;
			margin-bottom: 0.25em;
		}

		p {
			margin: 0.5em 0;
		}

		table {
			width: 100%;
			border-collapse: collapse;
			margin: 0.5em 0;
		}

		th, td {
			border: 1px solid #ddd;
			padding: 0.4em 0.6em;
			text-align: left;
			vertical-align: top;
		}

		th {
			background-color: #f5f5f5;
			font-weight: bold;
		}

		hr {
			border: none;
			border-top: 1px solid #ccc;
			margin: 1em 0;
		}

		ul {
			margin: 0.5em 0;
			padding-left: 1.5em;
		}

		li {
			margin: 0.25em 0;
		}

		em {
			font-style: italic;
			color: #666;
			font-size: 9pt;
		}
		"""

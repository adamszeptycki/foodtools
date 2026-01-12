"""Generate professional-looking service document PDFs using ReportLab."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from datetime import datetime
import os


class ServiceDocumentPDFGenerator:
	"""Generate professional-looking service document PDFs."""

	def __init__(self, output_dir="output"):
		"""
		Initialize the PDF generator.

		Args:
			output_dir (str): Directory to save generated PDFs
		"""
		self.output_dir = output_dir
		self.page_width, self.page_height = letter
		self.margin = 0.75 * inch

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
		c = canvas.Canvas(filepath, pagesize=letter)

		# Draw document sections
		self._draw_header(c, data)
		self._draw_client_info(c, data)
		self._draw_machine_info(c, data)
		self._draw_service_details(c, data)
		self._draw_parts_section(c, data)
		self._draw_technician_section(c, data)
		self._draw_footer(c, data)

		c.save()
		return filepath

	def _draw_header(self, c, data):
		"""Draw company header and work order information."""
		# Company name
		c.setFont("Helvetica-Bold", 20)
		c.drawString(self.margin, self.page_height - self.margin, data["company"])

		# Service report title
		c.setFont("Helvetica-Bold", 14)
		c.drawCentredString(
			self.page_width / 2, self.page_height - self.margin - 0.5 * inch, "SERVICE REPORT"
		)

		# Work order and date
		c.setFont("Helvetica", 10)
		c.drawRightString(
			self.page_width - self.margin,
			self.page_height - self.margin,
			f"Work Order: {data['work_order']}",
		)
		c.drawRightString(
			self.page_width - self.margin,
			self.page_height - self.margin - 0.15 * inch,
			f"Date: {data['service_date'].strftime('%m/%d/%Y')}",
		)

		# Horizontal line
		y = self.page_height - self.margin - 0.8 * inch
		c.line(self.margin, y, self.page_width - self.margin, y)

	def _draw_client_info(self, c, data):
		"""Draw client information section."""
		y_start = self.page_height - self.margin - 1.2 * inch

		c.setFont("Helvetica-Bold", 11)
		c.drawString(self.margin, y_start, "CLIENT INFORMATION")

		c.setFont("Helvetica", 10)
		y = y_start - 0.25 * inch
		c.drawString(self.margin, y, f"Client Name: {data['client_name']}")
		y -= 0.2 * inch

		# Handle multi-line address
		address_lines = data["client_address"].split("\n")
		c.drawString(self.margin, y, f"Address: {address_lines[0]}")
		for line in address_lines[1:]:
			y -= 0.15 * inch
			c.drawString(self.margin + 0.7 * inch, y, line)

		y -= 0.2 * inch
		c.drawString(self.margin, y, f"Phone: {data['client_phone']}")

	def _draw_machine_info(self, c, data):
		"""Draw machine information section."""
		y_start = self.page_height - self.margin - 3.5 * inch

		c.setFont("Helvetica-Bold", 11)
		c.drawString(self.margin, y_start, "EQUIPMENT INFORMATION")

		# Create table for machine info
		c.setFont("Helvetica", 10)
		y = y_start - 0.3 * inch

		info_data = [
			["Machine Type:", data["machine_type"]],
			["Model:", data["machine_model"]],
			["Serial Number:", data["serial_number"]],
		]

		for label, value in info_data:
			c.setFont("Helvetica-Bold", 10)
			c.drawString(self.margin, y, label)
			c.setFont("Helvetica", 10)
			c.drawString(self.margin + 1.5 * inch, y, value)
			y -= 0.2 * inch

	def _draw_service_details(self, c, data):
		"""Draw service details section."""
		y_start = self.page_height - self.margin - 5.2 * inch

		c.setFont("Helvetica-Bold", 11)
		c.drawString(self.margin, y_start, "SERVICE DETAILS")

		c.setFont("Helvetica", 10)
		y = y_start - 0.25 * inch

		# Problem description
		c.setFont("Helvetica-Bold", 10)
		c.drawString(self.margin, y, "Problem Description:")
		y -= 0.2 * inch
		c.setFont("Helvetica", 10)

		# Wrap text if needed
		problem_text = data["problem_description"]
		max_width = self.page_width - 2 * self.margin
		wrapped_problem = self._wrap_text(c, problem_text, max_width)
		for line in wrapped_problem:
			c.drawString(self.margin + 0.2 * inch, y, line)
			y -= 0.15 * inch

		y -= 0.15 * inch

		# Solution applied
		c.setFont("Helvetica-Bold", 10)
		c.drawString(self.margin, y, "Solution Applied:")
		y -= 0.2 * inch
		c.setFont("Helvetica", 10)

		wrapped_solution = self._wrap_text(c, data["solution_applied"], max_width)
		for line in wrapped_solution:
			c.drawString(self.margin + 0.2 * inch, y, line)
			y -= 0.15 * inch

	def _draw_parts_section(self, c, data):
		"""Draw parts used section."""
		y_start = self.page_height - self.margin - 7.5 * inch

		c.setFont("Helvetica-Bold", 11)
		c.drawString(self.margin, y_start, "PARTS USED")

		c.setFont("Helvetica", 10)
		y = y_start - 0.25 * inch

		if data["parts_used"]:
			parts = data["parts_used"].split(", ")
			for i, part in enumerate(parts, 1):
				c.drawString(self.margin + 0.2 * inch, y, f"{i}. {part}")
				y -= 0.2 * inch
		else:
			c.drawString(self.margin + 0.2 * inch, y, "No parts replaced")

	def _draw_technician_section(self, c, data):
		"""Draw technician information and signature."""
		y_start = 2.5 * inch

		c.setFont("Helvetica-Bold", 11)
		c.drawString(self.margin, y_start, "TECHNICIAN INFORMATION")

		c.setFont("Helvetica", 10)
		y = y_start - 0.3 * inch

		tech = data["technician"]
		c.drawString(self.margin, y, f"Technician Name: {tech['name']}")
		y -= 0.2 * inch
		c.drawString(self.margin, y, f"Technician ID: {tech['id']}")
		y -= 0.2 * inch
		c.drawString(self.margin, y, f"Certification: {tech['cert']}")
		y -= 0.3 * inch

		# Service time information
		c.drawString(self.margin, y, f"Arrival Time: {data['arrival_time']}")
		c.drawString(self.margin + 2.5 * inch, y, f"Labor Hours: {data['labor_hours']}")

		# Signature line
		y -= 0.5 * inch
		c.drawString(self.margin, y, "Technician Signature:")

		# Draw signature line
		y -= 0.3 * inch
		c.line(self.margin + 1.5 * inch, y, self.margin + 4 * inch, y)

		# Date line
		c.drawString(self.margin + 4.5 * inch, y + 0.3 * inch, "Date:")
		c.line(self.margin + 5 * inch, y, self.margin + 6.5 * inch, y)

	def _draw_footer(self, c, data):
		"""Draw document footer."""
		c.setFont("Helvetica-Oblique", 8)
		c.drawCentredString(
			self.page_width / 2,
			0.5 * inch,
			f"{data['company']} | 24/7 Service | (555) 123-4567",
		)
		c.drawCentredString(
			self.page_width / 2,
			0.35 * inch,
			"www.foodservicetech.com | service@foodservicetech.com",
		)

	def _wrap_text(self, c, text, max_width):
		"""
		Wrap text to fit within max_width.

		Args:
			c: Canvas object
			text (str): Text to wrap
			max_width (float): Maximum width in points

		Returns:
			list: List of text lines that fit within max_width
		"""
		words = text.split()
		lines = []
		current_line = []

		for word in words:
			test_line = " ".join(current_line + [word])
			if c.stringWidth(test_line, "Helvetica", 10) <= max_width - 0.4 * inch:
				current_line.append(word)
			else:
				if current_line:
					lines.append(" ".join(current_line))
				current_line = [word]

		if current_line:
			lines.append(" ".join(current_line))

		return lines

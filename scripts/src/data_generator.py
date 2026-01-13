"""Generate realistic service document data using Faker."""

from faker import Faker
import random
from datetime import datetime, timedelta
from .constants import MACHINE_CATEGORIES, SERVICE_ISSUES, TECHNICIANS, COMPANIES


class ServiceDocumentDataGenerator:
	"""Generate realistic service document data for testing."""

	def __init__(self, seed=None):
		"""Initialize the generator with optional seed for reproducibility."""
		self.fake = Faker()
		if seed is not None:
			Faker.seed(seed)
			random.seed(seed)

	def generate_service_record(self):
		"""
		Generate a complete service record with all required fields.

		Returns:
			dict: Service record data matching the schema fields:
				- machine_model (str)
				- machine_type (str)
				- problem_description (str)
				- solution_applied (str)
				- parts_used (str, optional)
				- client_name (str)
				- service_date (date)
				Plus additional fields for the document layout.
		"""
		# Select machine category and details
		category = random.choice(list(MACHINE_CATEGORIES.keys()))
		machine_data = MACHINE_CATEGORIES[category]

		model = random.choice(machine_data["models"])

		# Pick a linked problem-solution-parts entry for consistency
		service_issue = random.choice(SERVICE_ISSUES[category])
		problem = service_issue["problem"]
		solution = service_issue["solution"]

		# 70% chance of parts being used - pick from this issue's valid parts
		parts_used = None
		if random.random() < 0.7:
			available_parts = service_issue["parts"]
			num_parts = random.randint(1, min(3, len(available_parts)))
			parts_used = ", ".join(random.sample(available_parts, num_parts))

		# Generate service metadata
		service_date = self.fake.date_between(start_date="-2y", end_date="today")
		technician = random.choice(TECHNICIANS)
		company = random.choice(COMPANIES)

		# Generate client information
		client_name = self.fake.company()
		client_address = self.fake.address()
		client_phone = self.fake.phone_number()

		# Generate additional details
		serial_number = f"SN{self.fake.random_number(digits=8, fix_len=True)}"
		work_order = f"WO-{self.fake.random_number(digits=6, fix_len=True)}"

		# Service time details
		arrival_time = self.fake.time(pattern="%H:%M")
		duration = random.randint(30, 240)  # 30 min to 4 hours

		return {
			# Required fields for extraction (match database schema)
			"machine_model": model,
			"machine_type": category,
			"problem_description": problem,
			"solution_applied": solution,
			"parts_used": parts_used,
			"client_name": client_name,
			"service_date": service_date,
			# Additional document details
			"serial_number": serial_number,
			"work_order": work_order,
			"technician": technician,
			"company": company,
			"client_address": client_address,
			"client_phone": client_phone,
			"arrival_time": arrival_time,
			"duration_minutes": duration,
			"labor_hours": round(duration / 60, 2),
		}

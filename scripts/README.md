# FoodTools PDF Generator

Generate realistic service document PDFs for testing the FoodTools machine service document management system.

## Overview

This tool creates professional-looking service documents for food service equipment (ovens, fryers, mixers, refrigeration, dishwashers, and griddles) with realistic problems, solutions, and parts data. The generated PDFs are compatible with the FoodTools AI extraction pipeline.

## Quick Start

```bash
# Install dependencies
uv sync

# Generate 10 test documents
uv run generate_documents.py

# Generate 50 documents with verbose output
uv run generate_documents.py -n 50 -v
```

## Features

- Professional PDF service documents with proper formatting
- 6 equipment categories with realistic models
- Common problems and solutions for each equipment type
- Randomized client and technician information
- Compatible with FoodTools AI extraction system
- Reproducible generation with seed option

## Equipment Categories

- **Ovens**: ConvectionPro, RapidBake, TurboHeat, CombiSteam, DeckMaster
- **Fryers**: DeepFry Pro, TurboCrisp, OilGuard, FryMaster, CrispKing
- **Mixers**: PlanetaryMix, DoughMaster, SpiralPro, VersaMix, HeavyDuty
- **Refrigeration**: ChillMaster, WalkIn Pro, ReachIn Elite, UndercounterCool
- **Dishwashers**: SaniSpray, RackMaster, UndercounterClean, DoorType
- **Griddles**: FlatTop Pro, ElectricGrill, GasGriddle, ChromeTop

## CLI Options

```bash
uv run generate_documents.py [OPTIONS]
```

### Options

- `--count, -n`: Number of documents to generate (default: 10)
- `--output, -o`: Output directory (default: output/)
- `--seed, -s`: Random seed for reproducible generation
- `--verbose, -v`: Show detailed generation information

### Examples

```bash
# Generate 25 documents
uv run generate_documents.py -n 25

# Generate with specific seed for reproducibility
uv run generate_documents.py -n 10 --seed 42

# Generate to custom directory with verbose output
uv run generate_documents.py -n 20 -o ../test-pdfs -v

# Generate large batch for testing
uv run generate_documents.py -n 100
```

## Output

Generated PDFs are saved to the `output/` directory (or custom directory specified with `-o`) with sequential filenames:
- `service_doc_0001.pdf`
- `service_doc_0002.pdf`
- `service_doc_0003.pdf`
- etc.

Each document contains:
- Company header with work order number and date
- Client information (name, address, phone)
- Equipment information (type, model, serial number)
- Service details (problem description and solution)
- Parts used (if applicable)
- Technician information and signature line
- Company footer with contact information

## Document Fields

The generated documents include all fields required by the FoodTools extraction schema:

- **machine_model**: Equipment model name
- **machine_type**: Category (Ovens, Fryers, etc.)
- **problem_description**: Detailed problem description
- **solution_applied**: Solution and work performed
- **parts_used**: Comma-separated list of parts (optional)
- **client_name**: Client company name
- **service_date**: Date of service (last 2 years)

## Testing with FoodTools

1. Start the FoodTools development server:
   ```bash
   cd /Users/justme/Developer/JetBridge/demos/foodtools
   pnpm dev
   ```

2. Navigate to http://localhost:3000/dashboard/documents

3. Upload PDFs from the `scripts/output/` directory

4. Monitor processing status in the dashboard

5. Test semantic search at http://localhost:3000/dashboard/search with queries like:
   - "oven not heating"
   - "fryer temperature problems"
   - "mixer gearbox noise"
   - "refrigeration leak"

## Project Structure

```
scripts/
├── generate_documents.py       # Main CLI script
├── pyproject.toml              # UV project configuration
├── README.md                   # This file
├── .gitignore                  # Ignore PDFs and Python artifacts
├── output/                     # Generated PDFs (gitignored)
└── src/
    ├── __init__.py
    ├── constants.py            # Machine types, problems, solutions
    ├── data_generator.py       # Faker-based data generation
    └── pdf_generator.py        # ReportLab PDF creation
```

## Dependencies

- **reportlab**: PDF generation
- **faker**: Realistic fake data
- **click**: CLI framework
- **pillow**: Image handling (for future logo support)

## Development

### Adding New Machine Types

Edit `src/constants.py` and add to `MACHINE_CATEGORIES`:

```python
"YourCategory": {
    "models": ["Model1", "Model2"],
    "common_problems": ["Problem1", "Problem2"],
    "solutions": ["Solution1", "Solution2"],
    "parts": ["Part1", "Part2"],
}
```

### Customizing Document Layout

Edit `src/pdf_generator.py` to modify the `ServiceDocumentPDFGenerator` class methods for different layouts, fonts, or styling.

## License

Part of the FoodTools project.

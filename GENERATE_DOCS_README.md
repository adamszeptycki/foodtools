# FoodTools Service Document PDF Generator

## What Was Built

A complete Python-based PDF generator that creates realistic service documents for food service equipment testing.

### Project Structure
```
scripts/
├── generate_documents.py       # CLI script
├── pyproject.toml              # UV dependencies
├── README.md                   # Documentation
├── .gitignore                  # Excludes PDFs/artifacts
├── output/                     # Generated PDFs
│   ├── service_doc_0001.pdf
│   ├── ...
│   └── service_doc_0020.pdf
└── src/
    ├── __init__.py
    ├── constants.py            # Machine types & data
    ├── data_generator.py       # Faker data generation
    └── pdf_generator.py        # ReportLab PDF creation
```

### Features Implemented

- **6 Equipment Categories**: Ovens, Fryers, Mixers, Refrigeration, Dishwashers, Griddles
- **Realistic Data**: Uses Faker for client names, addresses, phone numbers
- **Professional PDFs**: Letter-size documents with proper formatting
- **Extraction-Ready**: All fields match your database schema
- **CLI Options**: Count, output directory, seed, verbose mode

### Generated Test Documents

The system has been tested with 20 sample PDFs (51.8 KB total) using seed 42 for reproducibility. Each contains:
- Company header with work order number
- Client information
- Equipment details (type, model, serial)
- Problem description and solution
- Parts used (when applicable)
- Technician information and signature line

## Usage Examples

```bash
# From scripts/ directory

# Generate 10 documents (default)
uv run generate_documents.py

# Generate 50 with verbose output
uv run generate_documents.py -n 50 -v

# Reproducible generation with seed
uv run generate_documents.py -n 25 --seed 12345

# Custom output directory
uv run generate_documents.py -o ../test-docs
```

## Equipment Categories & Data

### Machine Types
- **Ovens**: ConvectionPro 5000, RapidBake 3000, TurboHeat X-200, CombiSteam Elite, DeckMaster 480
- **Fryers**: DeepFry Pro 450, TurboCrisp 2000, OilGuard Elite, FryMaster XL-4000, CrispKing 300
- **Mixers**: PlanetaryMix 60, DoughMaster 80Q, SpiralPro 120, VersaMix 40, HeavyDuty 100
- **Refrigeration**: ChillMaster 2000, WalkIn Pro Series, ReachIn Elite 3-Door, UndercounterCool 48, DisplayCase Premium
- **Dishwashers**: SaniSpray 3000, RackMaster Conveyor, UndercounterClean Pro, DoorType HT-60, FlightType Industrial
- **Griddles**: FlatTop Pro 48, ElectricGrill 36, GasGriddle HeavyDuty, ChromeTop Elite, ThermoStatic 60

### Realistic Problems & Solutions
Each category includes 10+ realistic problems and matching solutions:
- Temperature issues
- Mechanical failures
- Electrical problems
- Leaks and seals
- Motor/fan problems
- Control system failures

### Parts Database
Common replacement parts for each equipment type:
- Heating elements, thermostats, sensors
- Motors, fans, pumps
- Valves, solenoids, relays
- Gaskets, seals, bearings
- Control boards, timers

## Testing with FoodTools System

### 1. Start Development Server
```bash
# From project root
pnpm dev
```

### 2. Upload Documents
- Navigate to http://localhost:3000/dashboard/documents
- Upload PDFs from `scripts/output/`
- Monitor processing status in the dashboard
- Check extraction results

### 3. Test Semantic Search
Go to http://localhost:3000/dashboard/search and try queries like:
- "oven not heating"
- "fryer temperature issues"
- "mixer gearbox noise"
- "refrigeration leak"
- "dishwasher pump failure"

### 4. Verify Extraction
```bash
# Check database for extracted data
pnpm --filter @foodtools/core db:studio
```

Look at the `machineFixes` table to verify:
- `machineModel` extracted correctly
- `machineType` matches categories
- `problemDescription` captured
- `solutionApplied` captured
- `partsUsed` extracted (when present)
- `clientName` extracted
- `serviceDate` parsed

## Generate More Documents

### Quick Commands
```bash
cd scripts

# Small test set
uv run generate_documents.py -n 10 -v

# Medium batch
uv run generate_documents.py -n 50

# Large test dataset
uv run generate_documents.py -n 100

# Reproducible test set for CI/testing
uv run generate_documents.py -n 25 --seed 42
```

### Output
PDFs are saved to `scripts/output/` with sequential filenames:
- Average size: ~2.6 KB per document
- Format: Letter size (8.5" x 11") PDF
- Text is selectable (not scanned images)
- Professional formatting with sections

## Document Fields

Generated documents include all fields required by the FoodTools extraction schema:

| Field | Type | Example |
|-------|------|---------|
| `machine_model` | string | "ConvectionPro 5000" |
| `machine_type` | string | "Ovens" |
| `problem_description` | string | "Temperature not reaching setpoint" |
| `solution_applied` | string | "Replaced thermocouple sensor and recalibrated..." |
| `parts_used` | string | "Thermocouple Type K 24-inch, Control board PCB-5000" |
| `client_name` | string | "Rosales-Good" |
| `service_date` | date | 2024-06-15 |

Plus additional document fields:
- Serial number (SN########)
- Work order (WO-######)
- Technician details (name, ID, certification)
- Service company
- Client contact info
- Service time and labor hours

## Development

### Adding New Machine Types
Edit `scripts/src/constants.py` and add to `MACHINE_CATEGORIES`:

```python
"YourCategory": {
    "models": ["Model1", "Model2"],
    "common_problems": ["Problem1", "Problem2"],
    "solutions": ["Solution1", "Solution2"],
    "parts": ["Part1", "Part2"],
}
```

### Customizing Document Layout
Edit `scripts/src/pdf_generator.py` to modify:
- Page layout and margins
- Fonts and styling
- Section arrangement
- Header/footer content

### Adding Logos or Images
1. Add image files to `scripts/templates/`
2. Modify `_draw_header()` in `pdf_generator.py`:
```python
from reportlab.lib.utils import ImageReader
logo = ImageReader("templates/logo.png")
c.drawImage(logo, x, y, width=1*inch, height=0.5*inch)
```

## Technical Details

### Dependencies
- **reportlab** (4.4.7): PDF generation
- **faker** (40.1.0): Realistic fake data
- **click** (8.3.1): CLI framework
- **pillow** (12.1.0): Image handling

### Python Requirements
- Python 3.11+
- UV package manager

### Installation
```bash
cd scripts
uv sync  # Install all dependencies
```

## Success Metrics

- ✅ Successfully generates PDFs with professional layout
- ✅ Data matches existing schema fields
- ✅ Documents can be uploaded and processed by FoodTools
- ✅ AI extraction successfully parses all key fields
- ✅ Semantic search finds relevant documents
- ✅ UV environment setup works cleanly
- ✅ CLI is intuitive and well-documented

## Troubleshooting

### PDF Generation Fails
```bash
# Ensure dependencies are installed
cd scripts
uv sync

# Check Python version
python --version  # Should be 3.11+
```

### Output Directory Not Found
The script creates the output directory automatically. If issues persist:
```bash
mkdir -p scripts/output
```

### Import Errors
Make sure you're running from the scripts directory:
```bash
cd scripts
uv run generate_documents.py
```

## File Locations

- **Generator script**: `/Users/justme/Developer/JetBridge/demos/foodtools/scripts/generate_documents.py`
- **Constants**: `/Users/justme/Developer/JetBridge/demos/foodtools/scripts/src/constants.py`
- **Data generator**: `/Users/justme/Developer/JetBridge/demos/foodtools/scripts/src/data_generator.py`
- **PDF generator**: `/Users/justme/Developer/JetBridge/demos/foodtools/scripts/src/pdf_generator.py`
- **Output directory**: `/Users/justme/Developer/JetBridge/demos/foodtools/scripts/output/`
- **Documentation**: `/Users/justme/Developer/JetBridge/demos/foodtools/scripts/README.md`

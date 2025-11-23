# Cigarette-Forecasting-and-Ordering

This repository contains Python scripts designed to analyze cigarette sales data, forecast demand, and generate order forms with barcode integration. The project processes sales data to identify when products require restocking and outputs order information in Excel format.

## Features

- Reads cigarette sales data from CSV files and processes it into structured dataframes.
- Calculates weekly total cartons sold and average weekly sales per cigarette product.
- Flags products that require ordering based on sales thresholds.
- Generates order forms exported to Excel spreadsheets.
- Barcode generation for cigarette products using UPC codes.

## Tech Stack

- Python 3
- pandas for data manipulation
- numpy for numerical operations
- python-barcode for barcode generation

## Getting Started

### Prerequisites

- Python 3.x installed
- pip package manager

### Installation

1. Clone the repository:

```bash
git clone https://github.com/justin-napolitano/Cigarette-Forecasting-and-Ordering.git
cd Cigarette-Forecasting-and-Ordering
```

2. Install dependencies:

```bash
pip install pandas numpy python-barcode
```

3. Place the sales data CSV file `CigSales.csv` in the repository root or update the path in `cigarette_sales_order_form.py` accordingly.

### Running

- To generate order forms and analyze sales data, run:

```bash
python cigarette_sales_order_form.py
```

- To generate barcode images for cigarette UPC codes, run:

```bash
python bar_code.py
```

## Project Structure

- `cigarette_sales_order_form.py`: Main script for reading sales data, performing analysis, and exporting order forms.
- `bar_code.py`: Script for generating barcode images from UPC codes.
- `README.md`: This documentation file.
- `CigSales.csv` (assumed): CSV file containing cigarette sales data (not included in repo).

## Future Work / Roadmap

- Add command-line arguments for input/output file paths and parameters.
- Implement automated scheduling for regular sales data processing.
- Enhance order form generation with more detailed reporting.
- Integrate with inventory management systems.
- Expand barcode generation to batch process multiple products.
- Add unit tests and validation for data processing steps.

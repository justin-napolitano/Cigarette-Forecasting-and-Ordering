---
slug: github-cigarette-forecasting-and-ordering-note-technical-overview
id: github-cigarette-forecasting-and-ordering-note-technical-overview
title: Cigarette-Forecasting-and-Ordering
repo: justin-napolitano/Cigarette-Forecasting-and-Ordering
githubUrl: https://github.com/justin-napolitano/Cigarette-Forecasting-and-Ordering
generatedAt: '2025-11-24T18:32:33.850Z'
source: github-auto
summary: >-
  This repo analyzes cigarette sales data, forecasts demand, and generates order
  forms with barcodes. It processes sales data in CSV files to flag items
  needing restocking and outputs order info in Excel format.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: note
entryLayout: note
showInProjects: false
showInNotes: true
showInWriting: false
showInLogs: false
---

This repo analyzes cigarette sales data, forecasts demand, and generates order forms with barcodes. It processes sales data in CSV files to flag items needing restocking and outputs order info in Excel format.

## Key Components

- **Data Processing**: Uses `pandas` to read and structure sales data.
- **Sales Analysis**: Calculates weekly sales and flags low-stock products.
- **Export**: Generates order forms in Excel.
- **Barcode Generation**: Creates barcodes for products using UPC codes.

## Getting Started

1. Clone the repo:

   ```bash
   git clone https://github.com/justin-napolitano/Cigarette-Forecasting-and-Ordering.git
   cd Cigarette-Forecasting-and-Ordering
   ```

2. Install dependencies:

   ```bash
   pip install pandas numpy python-barcode
   ```

3. Place your `CigSales.csv` in the repo root.

### Run the Scripts

- Analyze data and generate orders:

   ```bash
   python cigarette_sales_order_form.py
   ```

- Generate barcodes:

   ```bash
   python bar_code.py
   ```

### Gotchas

Make sure your CSV file is formatted correctly, or the scripts might break.

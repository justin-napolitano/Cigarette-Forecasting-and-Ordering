---
slug: "github-cigarette-forecasting-and-ordering"
title: "Cigarette-Forecasting-and-Ordering"
repo: "justin-napolitano/Cigarette-Forecasting-and-Ordering"
githubUrl: "https://github.com/justin-napolitano/Cigarette-Forecasting-and-Ordering"
generatedAt: "2025-11-23T08:26:10.646958Z"
source: "github-auto"
---


# Cigarette-Forecasting-and-Ordering: Technical Overview

This project addresses the operational need to forecast cigarette sales and automate ordering based on sales data. It leverages Python for data processing and barcode generation to streamline inventory management decisions.

## Motivation

Retailers and distributors require accurate forecasting to maintain optimal inventory levels, minimizing stockouts and overstock. Cigarette sales can fluctuate weekly, making manual tracking inefficient and error-prone. This project automates the analysis of sales data to identify when products fall below expected sales thresholds, triggering restocking orders.

## Problem Statement

Given raw sales data, the challenge is to:

- Aggregate sales by product and store on a weekly basis.
- Calculate average weekly sales to establish baseline demand.
- Compare current sales against these averages to determine if reordering is necessary.
- Generate order forms that include product barcodes for easy identification and processing.

## Implementation Details

### Data Processing

The core script, `cigarette_sales_order_form.py`, reads sales data from a CSV file into a pandas DataFrame. Key steps include:

- Parsing the `Date` column into datetime objects and setting it as the index.
- Computing `Total Cartons Sold` by multiplying `Quantity Sold` by `Sell Unit Quantity`.
- Extracting the week number from the timestamp to group sales data weekly.
- Grouping data by week, store, cigarette name, UPC, item number, and sell unit quantity to aggregate sales.
- Normalizing total cartons sold by dividing by 10 (likely a unit conversion).
- Calculating the average cartons sold weekly per cigarette product.
- Adding an `Order` boolean flag to indicate if sales exceed average demand, signaling a reorder.

The logic for ordering is:

```python
Order = (Average Cartons Sold Weekly <= Total Cartons Sold) and (Total Cartons Sold >= 1)
```

This implies orders are placed when current sales meet or exceed average sales, with a minimum sales threshold.

### Barcode Generation

The `bar_code.py` script uses the `python-barcode` library to generate UPC barcodes:

- A hardcoded UPC code string is used as input.
- The barcode object is created and rendered in ASCII for console output.
- The barcode is saved as an image file (`upc13`), facilitating inclusion in order forms or labels.

### Assumptions and Limitations

- The sales data CSV (`CigSales.csv`) is assumed to be formatted with columns including `Date`, `Quantity Sold`, `Sell Unit Quantity`, `Store`, `Cigarette Name`, `Cigarette UPC`, and `Item Number`.
- The project currently lacks parameterization; file paths and thresholds are hardcoded.
- There is no error handling or data validation implemented.
- Output is limited to console prints and DataFrame manipulations; exporting to Excel is mentioned but not fully shown.

## Practical Considerations

For operational use, enhancements would include:

- Parameterizing input/output paths and thresholds via command-line arguments or configuration files.
- Automating export of flagged orders into formatted Excel spreadsheets.
- Batch processing of multiple UPC codes for barcode generation.
- Integration with inventory or ERP systems for seamless order placement.
- Adding logging and error handling for robustness.

## Summary

This project provides a foundational framework for cigarette sales forecasting and ordering automation. It demonstrates practical use of pandas for time-series aggregation and numpy for conditional flagging. Barcode generation is integrated to support downstream processing. While functional, the code requires further development to be production-ready, including configurability, error handling, and comprehensive output generation.
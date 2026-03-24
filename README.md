# Startup Funding Analysis

A Streamlit web application for analyzing Indian startup funding data. The dashboard provides three views: overall market analysis, startup-level details, and investor-level details.

## Project Structure

```
.
├── app.py
├── main.py
├── Startup_clean.csv
├── startup_funding.csv
└── requirements.txt
```

## Data

**startup_funding.csv** — Raw dataset with the following columns:
- Sr No, Date, Startup Name, Industry Vertical, SubVertical, City Location, Investors Name, Investment Type, Amount in USD, Remarks

**Startup_clean.csv** — Cleaned version used by the app with renamed and preprocessed columns:
- Sr No, date, start up, vertical, SubVertical, City, Investors, Round, Amount, Remarks
- Amount is converted to INR (Cr)
- Date is parsed and split into `month` and `year` columns

## Features

### Overall Analysis
- Total amount invested across all startups
- Maximum funding received by a single startup
- Average funding per startup
- Total number of unique startups funded
- Month-over-Month (MoM) chart showing either total funding amount or count of deals

### Startup View
- Sidebar dropdown to select a startup from the dataset

### Investor View
- Most recent 5 investments by the selected investor
- Bar chart of biggest investments by startup
- Pie chart of sector-wise investment distribution
- Year-over-Year (YoY) investment trend line chart

## Installation

Install dependencies using:

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
streamlit
matplotlib
pandas
numpy
```

## Usage

```bash
streamlit run app.py
```

The app opens in wide layout mode. Use the sidebar to switch between **Overall Analysis**, **Startup**, and **Investor** views. For the Investor view, select an investor from the dropdown and click **Find Investor Details**.

## Notes

- The app reads `Startup_clean.csv` from the working directory. Ensure the file is present before running.
- Missing investor names in the dataset are filled with `Undisclosed`.
- Investor search uses substring matching, so selecting an investor from the dropdown will match all records where that investor's name appears.

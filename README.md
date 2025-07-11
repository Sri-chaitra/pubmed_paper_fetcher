# 📄 PubMed Paper Fetcher

A Python command-line tool to fetch research papers from PubMed based on a user-specified query, filter papers with at least one author affiliated with a pharmaceutical or biotech company, and export the results as a CSV file.

---

## ✨ Features

✅ Fetch papers using PubMed's API with flexible query syntax  
✅ Identify non-academic authors and company affiliations using heuristics  
✅ Output results to console or CSV file  
✅ Typed Python code for clarity and robustness  
✅ Modular design for reuse and packaging

---

## 🚀 Installation

This project uses **Poetry** for dependency management.

Clone the repository:
git clone https://github.com/Sri-chaitra/pubmed_paper_fetcher.git
cd pubmed_paper_fetcher

## Install dependencies:

poetry install

## Usage

You can run the command-line tool using Poetry:

poetry run get-papers-list "your query here"

##  Options

-h, --help
Show usage instructions.

-d, --debug
Print debug information during execution.

-f, --file <filename>
Save output to the specified CSV file (default: prints to console).

## Example

Fetch papers about cancer immunotherapy, print debug info, and save results to results.csv:

poetry run get-papers-list "cancer immunotherapy" -d -f results.csv

## Output CSV Columns

The generated CSV will include:

PubmedID: Unique identifier for the paper

Title: Title of the paper

Publication Date: Year of publication

Non-academic Author(s): Authors affiliated with non-academic institutions

Company Affiliation(s): Names of companies

Corresponding Author Email: If available

## 🗂️ Project Structure

```
.
├── CLI.py                  # Entry point CLI script
├── pyproject.toml          # Poetry config
├── papers_fetcher/         # Python module
│   ├── __init__.py
│   ├── fetcher.py          # PubMed fetching logic
│   ├── filters.py          # Filtering heuristics
│   └── models.py           # Typed data models
└── README.md               # This file
```
        

## Dependencies

Biopython – For PubMed API access

Pydantic – For data validation and typing


##  Development & Testing

If you modify the project, reinstall dependencies:

poetry install


## License

MIT License


## Acknowledgments

This project was built using:

Python 3.9+

Poetry for packaging

GitHub for version control


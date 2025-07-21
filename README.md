# PubMed CLI Search Tool

This is a Python command-line program to search PubMed papers by keyword, print results, and save them to CSV.

## 📌 Features

- Search any keyword in PubMed
- Fetch top 5 papers
- Prints Title, Abstract, Authors
- Saves output to a CSV file

## 🛠️ Requirements

- Python 3.7+
- requests

## 💻 Installation

1. Clone the repo:

```
git clone https://github.com/asmathjabeen/pubmed_cli_project.git
cd pubmed_cli_project
```

2. Create virtual environment and install packages:

```
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

pip install requests
```

## 🚀 Usage

```
python pubmed_search.py "your search query"
```

Example:

```
python pubmed_search.py "heart disease"
```

## 📂 Output

- Prints results to console
- Saves to <query>\_papers.csv

## 🙏 Author

Shaik Asmath Jabeen | asmath9696@gmail.com

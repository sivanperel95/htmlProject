# htmlProject

```markdown
# Document Validation System

This project is designed to parse HTML documents, extract relevant data, save it into a MongoDB database, and validate the documents against specific criteria to identify discrepancies.

## Features

- Parse HTML files to extract document data.
- Save extracted data into MongoDB.
- Validate documents based on title length, date criteria, and sum of numerical values in the first row of tables.
- Log discrepancies for further analysis.

## Setup

### Requirements

- Python 3.8+
- MongoDB
- Beautiful Soup 4
- PyMongo

### Installation

**Clone the Repository**

```sh
git clone https://your-repository-url.git
cd your-project-directory
```

**Set up a Virtual Environment**

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

**Install Dependencies**

```sh
pip install -r requirements.txt
```

**Configuration**

Ensure MongoDB is running on your system. Update the MongoDB URI in the `MongoDBDataLayer` class if necessary.

### Usage

1. Place your HTML files in a directory named `documents`.

2. Run the main script:

```sh
python main.py
```

This will parse the HTML files, save the extracted data into MongoDB, and validate each document based on the defined criteria.

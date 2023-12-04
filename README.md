# stack-webscrape
Web crawler that extracts and processes first 30 entries from https://new.ycombinator.com/

## Installation

This guide will walk you through the process of setting up a virtual environment in Windows for your Python project using the provided `requirements.txt` file. 
A virtual environment ensures that your project's dependencies are isolated from the system-wide Python environment.

### Prerequisites

Make sure you have Python installed on your system. You can download the latest version of Python from the official website: [python.org/downloads](https://www.python.org/downloads/).

### Step 1: Create a Virtual Environment

Open a terminal or command prompt and navigate to the root directory of your project where the `requirements.txt` file is located.

```bash
python -m venv venv
```

### Step 2: Activate the Virtual Environment

Activate the virtual environment to ensure you are using the correct dependencies for your project.

```bash
venv\Scripts\activate
```

### Step 3: Install the Required Packages
```bash
pip install -r requirements.txt
```

## Running the code
```bash
python main.py
```

## Updating the `requirements.txt`
If new libraries are added the requirements.txt must be updated.
To do that we must have the `venv` activated. 
```bash
pip freeze > requirements.txt
```

## Formatting the files
Before committing we use an opinionated formatter to maintain style within .py files.
```bash
black .
```

# Testing
You can run `py.test tests -vv -s`

## By file
`pytest tests/test_analisis.py`

`pytest tests/test_cache.py`

## Options
Option -x

Option -s

Option -vv

`pytest tests/test_analisis.py -vv -s -x`
`pytest tests/test_cache.py -vv -s -x`

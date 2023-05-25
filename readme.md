# pytest-read-json-example

This repository provides an example of how to read JSON data in Pytest using various methods. It demonstrates five different techniques to Read JSON Data in Pytest

## Requirements

- Python 
- Pytest
- Black

## How to Run the Unit Tests

 - Clone the GitHub repository:
```bash 
	git clone [https://github.com/ericsalesdeandrade/pytest-read-json-example.git](https://github.com/ericsalesdeandrade/pytest-read-json-example.git)
```
	
 - Navigate to the project directory:
```bash 
		cd pytest-read-json-example
```
 - Create a virtual environment, activate it and install the requirements:
``` bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
To run the tests execute the following command
```bash
pytest tests/unit/test_read_json.py -v -s --input-json='{"name": "Ravi", "age": 90, "city": "New Delhi"}'
```
		 


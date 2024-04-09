# OpenCv Api
Welcome to opencv api.

## Prerequisites
```bash
    Python version 3.5 and above
```
## Getting Started
## Clone the repository
```bash
git clone https://github.com/Rhode01/feature_extraction_with_openCv_api.git 
cd feature_extraction_with_openCv_api
```
## Creating Virtual Env
```bash
python -m venv myvenv
```
### installing dependencies
This command will install the required packages specified in the requirements.txt
```bash
pip install > requirements.txt
```
### Starting the server

```bash
uvicorn main:app --reload
```
### using the Api
Using the API
Once the server is running, open your browser and navigate to localhost:8000/docs.
Here, you'll find the Swagger UI documentation for the API, allowing you to make requests.
Provide the path to the picture that you want to map its features using a JSON request like:

```bash
{
    "path": "The link to the picture"
}

```




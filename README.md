#OpenCv Api
Welcome to opencv api.

#Prerequisites
```bash
    Python version 3.5 and above
```
#Getting Started
##Clone the repository
```bash
git clone https://github.com/Rhode01/feature_extraction_with_openCv_api.git 
cd feature_extraction_with_openCv_api
```
##Creating Virtual Env
```bash
python -m venv myvenv
```
###installing dependencies
This command will install the required packages specified in the requirements.txt
```bash
pip install > requirements.txt
```

# feature_extraction_with_openCv_api
To use the api please install the libraries in the requirements.txt file.
After installing the libralies start your uvicorn server by: uvicorn main:app --reload
if using uvicorn main:app --reload is not going to work, use python -m main:app --reload
Open your browser and navigate to localhost:8000/docs where you can now make your post request to the api
Provide the path to the picture that you want to map its feature using a json request like
{
"path": "The link to the picture"
}

#How to use the api
 ```bash ```



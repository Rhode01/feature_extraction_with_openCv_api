# feature_extraction_with_openCv_api
To use the api please install the libraries in the requirements.txt file.
After installing the libralies start your uvicorn server by: uvicorn main:app --reload
if using uvicorn main:app --reload is not going to work, use python -m main:app --reload
Open your browser and navigate to localhost:8000/docs where you can now make your post request to the api
Provide the path to the picture that you want to map its feature using a json request like
{
"path": "The link to the picture"
}

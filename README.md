# feature_extraction_with_openCv_api
to use the api please install the libraries in the requirements.txt file.
after installing the libralies start your uvicorn server by: uvicorn main:app --reload
open your browser and navigate to localhost:8000/docs where you can now make your post request to the api
provide the path to the picture that you want to map its feature using a json request like
{
"path": "The link to the picture"
}

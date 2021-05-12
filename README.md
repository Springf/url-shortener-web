## URL Shortener Web
This is a local flask web application to demo the functions of URL shortener core API.
In this web demo it implemented a sqlite backend store to store the URLs.
This is just a local demo app and not meant for any real world usage.

## Project Structure
```
+-- core
| git submodule point to the url-shortener-core
+-- static
| static files like js/css for frontend UI
+-- store
|  sqlite_store.py #in memory implementation of backend store
+-- templates
| html template to render the frontend UI
+-- tests
|   unit test cases files
server.py #the flask app that handles the web requests
```

## Setup
The code is tested with python 3.8+.

To setup the project, assuming python is installed.

Clone the project and update submodules, then create python venv:
```
git clone https://github.com/Springf/url-shortener-web.git
cd url-shortener
git submodule init
git submodule update
python -m venv venv
```
Activate the venv:

Windows: `venv\Scripts\activate.bat`

Linux: `source venv/bin/activate`

Install the package: `pip install -r requirements.txt`

## Test

Run unit tests: `pytest tests`

## Run
Linux: `./run.sh`
Windows: `run.bat`
Navigate to http://localhost:5000 to play.

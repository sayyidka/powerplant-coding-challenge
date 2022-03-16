# Wadieh Karbal's powerplants challenge implementation

## (Optional) Create a virtual environment ##
Install virtualenv package by running :  
`pip install virtualenv`

Create a virtual environment in the root folder by running :  
`python3 -m venv venv`  

It will create a "venv" folder in the root directory.

Now you can create a virtual environment by running one the following commands :  

On Windows : `source venv\Scripts\activate`  

On Linux/MacOS : `source env/bin/activate`  

If the virtual environment is successfully created, you should see the `(venv)` mention in the terminal.

## Install and run locally ##
Install the dependencies by running in the root folder :  
`pip install -r requirements.txt `

Run the application on the production server :  
`python app.py`  

The API will be listening on the port 8888 from localhost at :
`http://127.0.0.1:8888/productionplan`  


## Run with Docker ##
Install [Docker](https://www.docker.com/) depending on your OS.

In the root folder, build the application image by running the following command :  
`docker build --tag powerplant .` 

It will create an image called "powerplant" (you can choose another name).

Create and start a Docker container based on the powerplant image :  
`docker run -d -p 8888:8888 powerplant`  

It will start the application in a container available on port 8888. API will be listening at :  
`http://127.0.0.1:8888/productionplan` 

## Test ##
Run tests with the following command in the root folder :  
`python -m unittest discover tests`  

It will run the tests included in the "tests" folder.




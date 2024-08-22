# My Library Application

This is the documentation of "My library" application. My library is a simple GUI based on Python's Tkinter which shows content of a library based on a JSON file. It is also possible to expand the library by adding books based on entry fields in the GUI.

## Starting the application

The application is optimized to run inside a docker container but can be executed also locally. The instructions for both methods are listed below.

### Running the application without Docker

In order to run the application, the following software components are required: 
* Python 3.x --> Python 3.12 has been used in the development.
* Tkinter for Python. A Python library for GUI development.
* Json for Python. A Python library for handling JSON type files and data.

When all the above mentioned components are installed, the GUI can be started as follows:
```
python my_library_db.py <name_of_the_file>.json
```
In this case the JSON file with the library content is library.json and therefore the command is:
```
python my_library_db.py library.json
```
### Running the application with Docker

A Docker container has been implemented for the application in order to run with a simple setup in an exactly same OS and enviroment every time. The container is Linux based on includes Python virtual environment and all the needed libraries to run the application. Before running the actual application X Server is needed to be started in order to enable display for the containerized solution. This can be done as follows in Windows and Linux:
* In Windows, install VcXsrv and and follow the instructions of the following link until "You have now started your X Server.": https://scicomp.aalto.fi/triton/quickstart/installxonwindows/
* In Linux, enable xhost.

Finally, execute Docker compose and the GUI should be opened if everything goes as expected:
```
docker-compose up
```

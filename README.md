# My Library Application

This is the documentation of "My Library" application. My library is a simple GUI based on Python's Tkinter which shows content of a library based on a JSON file. It is also possible to expand the library by adding books based on entry fields in the GUI.

## Description of the application

"My Library" application is a simple GUI for printing library content from a JSON file. The GUI includes buttons to print the library content to a large text box and for adding a new book (or entry) into the JSON file. There are four entry fields where data needs to be written in a correct format:
* `Book title` - Name of the book.
* `Book author` - The person who wrote the book.
* `ISBN` - 13 number digit for the book --> Error message will appear if the number is written in wrong format.
* `Publishing year` - The year when the book was published --> Four digits is required in this case. Otherwise, error message will appear.
The application is optimized to run inside a docker container but can be executed also locally. The instructions for both methods are listed below.

<b>Note! The application is built in a way that it only accepts JSON file of a certain structure as an input. It will not work if the file type is different or if the JSON structure is not similar as in the example, `library.json`.</b>

### Running the application without Docker

In order to run the application, the following software components are required: 
* `Python 3.x` --> Python `3.12.3` has been used in the development.
* `Tkinter` for Python. A Python library for GUI development. Version `8.6` was used in the development.
* `Json` and `sys` libraries were also used in the application.

When all the above mentioned components are installed, the GUI can be started as follows:
```
python my_library_db.py <name_of_the_file>.json
```
In this case the JSON file with the library content is library.json and therefore the command is:
```
python my_library_db.py library.json
```

In case of a use of an another file, than the default `library.json` in the Python command can be just replaced with a similar file.

### Running the application with Docker

A Docker container has been implemented for the application in order to run with a simple setup in an exactly same OS and enviroment every time. The container is Linux based on includes Python virtual environment and all the needed libraries to run the application. Before running the actual application, Docker (and Docker compose) needs to be installed for building and starting the container and X Server is needed to be installed and started in order to enable display for the containerized solution. This has been verified to be working in Windows OS and can be done as follows:
  * Install VcXsrv and and follow the instructions of the following link until "You have now started your X Server.": 
    https://scicomp.aalto.fi/triton/quickstart/installxonwindows/
    
<b>Note! It should be possible to use the containerized solution also in Mac and Linux based OS. However, it has not been tested during the development of this application.</b>

Finally, execute Docker compose and the GUI should be opened if everything goes as expected:
```
docker-compose up
```
In case of a use of an another file, than the default `library.json` in the containerized solution is set as an environment variable to `.env` file. To use another file, just replace the following line in the file:
```
JSON_FILE=library.json >> JSON_FILE=<name_of_another_file>
```

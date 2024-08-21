# My Library Application

This is the documentation of "My library" application. My library is a simple GUI based on Python's Tkinter which shows content of a library based on a JSON file. It is also possible to expand the library by adding books based on entry fields in the GUI.

## Starting the application

The application is optimized to run inside a docker container. For this, only docker is needed to be installed in the workstation where the GUI is used. The GUI can be started with the following command:

### Some useful commands without compose

* Building the container:
```
docker build -t mylib .
```
* Environment variable for display:
```
export DISPLAY=127.0.0.1:0.0
```
* Running the container:
```
docker run -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix mylib
```
### With compose

Before running docker compose, enable X Server
* In Windows, start VcXsrv.
* In Linux, enable xhost.
```
docker-compose up
```

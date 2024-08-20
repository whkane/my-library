# Build the image
docker build -t mylib .

export DISPLAY=127.0.0.1:0.0

docker run -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix mylib
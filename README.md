# code-solutions
A compilation of my code solutions to coding challenges

## run containerized
```
docker run -it --name pydev --rm \
    --volume $(pwd):/usr/src/app \
    --net=host python:3-slim \
    bash
```

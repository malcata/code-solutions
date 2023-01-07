# code-solutions
A compilation of my code solutions to coding challenges

# Improvements

Overload the continuous integration pipeline to guarantee the following:
[ ] the code runs 
[ ] follows a consistent code style guide
[ ] follows quality best practices (static code analysis) 
[ ] delivers the expected results (asserts?)

## run containerized
```
docker run -it --name pydev --rm \
    --volume $(pwd):/usr/src/app \
    --net=host python:3-slim \
    bash
```

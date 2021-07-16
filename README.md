# Shipping Python Code

Collection of different types of projects and the procedures for properly run them in containers.


## Flask Simple Webapp

Just a simple 'Hello, World!' web page.

### Lessons Learned

> Build images with `Dockerfile`

    $ vim flask-app/Dockerfile

```dockerfile
# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
```

> Build the declared image and naming it `python-flask`

    $ cd flask-app/
    $ docker build --tag python-flask .

> Running the container

    $ docker run --detach --publish 5000:5000 --name web-app python-flask
## flask-app

Packing a simple `flask` application into a docker container

### Build image and running the code

With docker installed, just run the following commands in bash.

    $ docker build --tag python-flask .
    $ docker run --publish 5000:5000 python-flask

To test your application just open a browser and type:

    http://localhost:5000

Another option is to use `curl` in the command line.

    $ curl http://localhost:5000
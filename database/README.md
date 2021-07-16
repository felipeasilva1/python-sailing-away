# Database MySQL

Single instance `MySQL` database for web applications or data engineering.

The image used in this project is the official `MySQL` docker image.

## Setup

> creating docker volumes for `MySQL` data and configuration

    $ docker volume create mysql-data
    $ docker volume create mysql-config

> creating network for interconnection between containers

    $ docker network create mysql-net

Before running the container let's create a file containing our database root password that we'll need later.

    $ echo <insert_your_password_here> > /tmp/secret.txt

Now, let's proceed.

> running the container

    $ docker run --detach \
    --volume mysql-data:/var/lib/mysql \
    --volume mysql-config:/etc/mysql \
    --publish 3306:3306 \
    --network mysql-net \
    --env MYSQL_ROOT_PASSWORD=$(cat /tmp/secret.txt) \
    mysql

> running a interective mysql client session

    $ docker exec --tty --interactive mysql-db mysql -u root -p

You may shorten the `--tty --interactive` to `-it` but i like the long version of arguments for clarity and it's a good practice to remember these types of syntax. 
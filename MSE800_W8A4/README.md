# Week 8 - Activity 4: Docker - multi-container

-   Author: Benjelyn Reves Patiag
-   Date Created: 10 Feb 2026
-   Description: Run a project (either a Car Rental System or a CV
    Analysis project) using a multi-container architecture

# Run Project Using Docker (Multi-Container + SQLite)

This project use **Docker** to run a Python app with **SQLite
database**.\
It use **two containers**: - Python application - SQLite database viewer
(browser)

------------------------------------------------------------------------

## What You Need

-   Docker Desktop installed
-   Docker is running
-   Project folder opened in VS Code

------------------------------------------------------------------------

## Project Structure

-   `main.py` - start program
-   `Dockerfile` - build Python app
-   `docker-compose.yml` - run multi containers
-   `app/data/car_rental.db` - SQLite database file

------------------------------------------------------------------------

## How To Run

Open terminal in project folder and run:

``` bash
docker compose up -d --build
```

## This Will Do

-   Build the app
-   Start all containers
-   Run program in background

------------------------------------------------------------------------

## View Database

You can see SQLite tables and data here:\
http://localhost:8080/
or\
http://127.0.0.1:8080/

------------------------------------------------------------------------

## Stop Project

To stop containers, run:

``` bash
docker compose down
```

------------------------------------------------------------------------

## Optional Docker Commands (For Debugging or Manual Run)

These steps are **optional**. Use them only if you want to manually run
or inspect containers.

### Run the Application Manually

``` bash
docker exec -it car_rental_app python main.py
```

**Explanation:**\
Runs the Python program inside the running container.

------------------------------------------------------------------------

### Check Running Containers

``` bash
docker ps
```

**Explanation:**\
Displays all running Docker containers.

------------------------------------------------------------------------

### Enter the sqliteweb Container

``` bash
docker exec -it car_rental_sqliteweb sh
```

**Explanation:**\
Opens terminal access inside the SQLite Web container.

------------------------------------------------------------------------

### Enter the App Container

``` bash
docker exec -it car_rental_app sh
```

**Explanation:**\
Opens terminal access inside the Python application container.

------------------------------------------------------------------------

# Docker Official Command References

If you want to see the complete list of Docker commands, refer to the
official documentation:

## Docker CLI Reference

https://docs.docker.com/reference/cli/docker/

Includes commands like: - docker run - docker build - docker ps - docker
exec - docker images - docker logs - docker compose

------------------------------------------------------------------------

## Docker Compose Reference

https://docs.docker.com/reference/cli/docker/compose/

Includes: - docker compose up - docker compose down - docker compose
build - docker compose logs - docker compose exec

------------------------------------------------------------------------

## Docker Cheat Sheet (Official PDF)

https://docs.docker.com/get-started/docker_cheatsheet.pdf

------------------------------------------------------------------------

## View Help Directly From Terminal

``` bash
docker --help
docker compose --help
docker run --help
```

These commands show detailed usage instructions.

------------------------------------------------------------------------


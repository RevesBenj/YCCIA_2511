# Week 8 - Activity 4: Docker \_ multi-container

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

-   Build the app\
-   Start all containers\
-   Run program in background

------------------------------------------------------------------------

## View Database

You can see SQLite tables and data here:\
Open browser and go to:\
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

### 1. Run the Application Manually Inside Container

``` bash
docker exec -it car_rental_app python main.py
```

**Explanation:**\
This command enters the running app container and executes the Python
program manually.\
Useful if you want to restart or test the app without restarting all
containers.

------------------------------------------------------------------------

### 2. Check Running Containers

``` bash
docker ps
```

**Explanation:**\
Shows all currently running Docker containers.\
You can confirm if `car_rental_app` and `car_rental_sqliteweb` are
running.

------------------------------------------------------------------------

### 3. Enter the sqliteweb Container

``` bash
docker exec -it car_rental_sqliteweb sh
```

**Explanation:**\
Opens a terminal session inside the SQLite Web container.\
You can inspect files or debug inside the container.

------------------------------------------------------------------------

### 4. Enter the App Container

``` bash
docker exec -it car_rental_app sh
```

**Explanation:**\
Opens a terminal session inside your Python application container.\
You can check environment variables, verify database path, or run
commands manually.

------------------------------------------------------------------------

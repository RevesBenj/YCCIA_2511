# Week 8 - Activity 4: Docker _ multi-container
- Author: Benjelyn Reves Patiag
- Date Created: 10 Feb 2026
- Description: Run a project (either a Car Rental System or a CV Analysis project) using a multi-container architecture 



# Run Project Using Docker (Multi-Container + SQLite)

This project use **Docker** to run a Python app with **SQLite database**.  
It use **two containers**:
- Python application
- SQLite database viewer (browser)

---

## What You Need
- Docker Desktop installed
- Docker is running
- Project folder opened in VS Code

---

## Project Structure
- `main.py` - start program
- `Dockerfile` - build Python app
- `docker-compose.yml` - run multi containers
- `app/data/car_rental.db` - SQLite database file

---

## How To Run

Open terminal in project folder and run:
```bash
docker compose up -d --build


## This Will Do

- Build the app  
- Start all containers  
- Run program in background  

---

## View Database
You can see SQLite tables and data here:
Open browser and go to:http://localhost:8080 or http://127.0.0.1:8080/



---

## Stop Project

To stop containers, run:

```bash
docker compose down

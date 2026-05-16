# Protected Image Delivery System

Mini project demonstrating controlled image delivery using:

- Flask
- Nginx
- Docker Compose
- Reverse Proxy

## Architecture

Browser
↓
Nginx
↓
Flask
↓
Private Storage

## Features

- Hidden image storage
- Access validation before serving files
- Reverse proxy architecture
- Dockerized deployment
- Internal image delivery logic

## Run

```bash
docker compose up --build
```

Open:

http://localhost:8080

## Project structure

project/
├── app/
├── nginx/
├── data/
├── docker-compose.yml
└── README.md

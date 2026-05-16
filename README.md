# Protected Image Delivery System

A mini-project demonstrating controlled image delivery using a reverse proxy architecture.

## Technologies

- Flask
- Nginx
- Docker Compose
- Docker
- Reverse Proxy

---

## Architecture

```text
Browser
    ↓
Nginx
    ↓
Flask Application
    ↓
Private Image Storage
```

---

## How it works

1. User opens the web page
2. Request reaches Nginx
3. Nginx forwards the request to Flask
4. Flask validates access rules
5. Flask retrieves the image from protected storage
6. Browser displays the image

---

## Features

- Hidden image storage
- Access validation before serving files
- Reverse proxy architecture
- Dockerized deployment
- Protected media delivery
- Separation of application and storage logic

---

## Project Structure

```text
protected-image-delivery/
├── app/
│   ├── Dockerfile
│   └── main.py
│
├── nginx/
│   └── nginx.conf
│
├── data/
│   └── images/
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## Run Project

Clone repository:

```bash
git clone https://github.com/romanchernukha8-ctrl/protected-image-delivery.git
```

Go to project folder:

```bash
cd protected-image-delivery
```

Start containers:

```bash
docker compose up --build
```

Open in browser:

```text
http://localhost:8080
```

---

## Future Improvements

- JWT authentication
- Signed URLs
- X-Accel-Redirect
- HTTPS support
- Object storage (S3 / MinIO)
- Rate limiting
- User roles and permissions

---

## Learning Goals

This project demonstrates:

- Reverse proxy concepts
- Container networking
- Dockerized application deployment
- Backend-controlled file access
- Protected media delivery

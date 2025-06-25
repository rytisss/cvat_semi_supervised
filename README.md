# ⚙️ CVAT with Semi-Supervised Annotation Pipelines

A customized [CVAT (Computer Vision Annotation Tool)](https://www.cvat.ai/) setup with integrated semi-supervised annotation workflows. This repository enables scalable and efficient data labeling using AI-assisted annotation models — ideal for accelerating image and video annotation in computer vision projects.

---

## 🚀 Core Installation

Follow the steps below to install and run CVAT using Docker.

### 1️⃣ Clone the CVAT Repository

Clone the official CVAT repository from GitHub (latest `develop` branch):

```bash
git clone https://github.com/cvat-ai/cvat
cd cvat
```

### 2️⃣ Start CVAT with Docker

Start CVAT and its dependencies (PostgreSQL, Redis) using Docker Compose:

```bash
docker compose up -d
```

### 3️⃣ Create a Superuser

Create a superuser to gain full access:

```bash
docker exec -it cvat_server bash -ic 'python3 ~/manage.py createsuperuser'
```

This superuser can manage permissions and access the admin panel.

### 4️⃣ Access the CVAT Interface

Open CVAT in your browser at:

[http://localhost:8080/tasks](http://localhost:8080/tasks)

### 🛑 Stop CVAT

To stop all running containers:

```bash
docker compose down
```

---

## 🤖 Semi-Automatic & Automatic Annotation Setup

To enable AI-assisted annotation, you'll need to install `nuctl`, the Nuclio CLI, and run CVAT with serverless support.

### 📥 Install `nuctl` (v1.13.0)

> **Note:** Make sure the `nuctl` version matches the one defined in `docker-compose.serverless.yml` (v1.13.0).

#### Linux

```bash
wget https://github.com/nuclio/nuclio/releases/download/1.13.0/nuctl-1.13.0-linux-amd64
chmod +x nuctl-1.13.0-linux-amd64
sudo ln -sf $(pwd)/nuctl-1.13.0-linux-amd64 /usr/local/bin/nuctl
```

---

### 🚢 Launch CVAT with Serverless Annotation Support

From the CVAT root directory, start all services with serverless functions enabled:

```bash
docker compose -f docker-compose.yml -f docker-compose.dev.yml -f components/serverless/docker-compose.serverless.yml up -d --build
```

### 🛑 Stop CVAT with Serverless

To shut down all containers (including serverless ones):

```bash
docker compose -f docker-compose.yml -f docker-compose.dev.yml -f components/serverless/docker-compose.serverless.yml down
```

---



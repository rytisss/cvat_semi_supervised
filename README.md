# CVAT with semi-supervised annotation pipelines
A customized CVAT (Computer Vision Annotation Tool) setup with integrated semi-supervised annotation workflows. This repository enables scalable, efficient data labeling using AI-assisted annotation models. Ideal for accelerating image and video annotation tasks in computer vision projects.  

## 🚀 Core Installation

This project relies on the [CVAT (Computer Vision Annotation Tool)](https://www.cvat.ai/) for annotation capabilities. Follow the steps below to download and set it up using Docker.

### 1️⃣ Clone the CVAT Repository

Clone the official CVAT repository from GitHub. This command will clone the latest `develop` branch:

```bash
git clone https://github.com/cvat-ai/cvat
cd cvat
```

### 2️⃣ Start CVAT with Docker

Use Docker Compose to start the necessary containers. This will download CVAT and required services such as PostgreSQL and Redis.

```bash
docker compose up -d
```

### 3️⃣ Create a Superuser (First-Time Setup)

When you register your first user, they will not have permissions to view tasks or perform administrative actions. To manage permissions, create a superuser using the command below:

```bash
docker exec -it cvat_server bash -ic 'python3 ~/manage.py createsuperuser'
```

The superuser will have access to the admin panel and can assign appropriate roles and groups to other users.

### 4️⃣ Open CVAT

In your browser, go to [http://localhost:8080/tasks](http://localhost:8080/tasks) to access the CVAT interface.

### 🛑 Stop CVAT

To stop all running CVAT containers, use the following command:

```bash
docker compose down
```

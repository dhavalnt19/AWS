# 🚀 AWS Docker CI/CD Pipeline

**GitHub Actions + Amazon ECR + EC2 (Full Hands-On Project)**

---

## 📌 Project Overview

This project demonstrates a **complete CI/CD pipeline** where:

* Code is pushed to GitHub
* Docker image is built automatically
* Image is pushed to Amazon ECR
* EC2 pulls and runs the container

---

## 🏗️ Architecture Flow

1. Developer pushes code → GitHub
2. GitHub Actions triggers workflow
3. Docker image is built
4. Image pushed to ECR
5. EC2 pulls latest image
6. Container runs on port 80

---

## 🧰 Tech Stack

* AWS EC2
* AWS ECR
* Docker
* GitHub Actions
* Python (sample app)

---

## 📁 Project Structure

```
aws-docker-cicd/
│── app/
│   └── app.py
│── requirements.txt
│── Dockerfile
│── .github/workflows/deploy.yml
│── README.md
```

---

## ⚙️ STEP 1: Create IAM User

### 🔹 Create User

* Go to AWS Console → IAM
* Create user: `github-actions-user`
* Enable **Programmatic access**

### 🔹 Attach Policy

* Attach:

  * AmazonEC2ContainerRegistryFullAccess

### 🔹 Output (IMPORTANT)

```
Access Key ID: AKIA************
Secret Access Key: ************
```

---

## 📦 STEP 2: Create ECR Repository

### 🔹 Command

```
aws ecr create-repository --repository-name my-app
```

### 🔹 Output

```
{
  "repository": {
    "repositoryUri": "123456789012.dkr.ecr.ap-south-1.amazonaws.com/my-app"
  }
}
```

👉 Save this URI (used everywhere)

---

## 🖥️ STEP 3: Launch EC2 Instance

### 🔹 Configuration

* OS: Ubuntu
* Instance: t2.micro
* Security Group:

  * SSH (22)
  * HTTP (80)

### 🔹 Output

```
Public IP: 13.233.xxx.xxx
```

---

## 🔧 STEP 4: Install Docker on EC2

### 🔹 Commands

```
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu
```

### 🔹 Verify

```
docker --version
```

### 🔹 Output

```
Docker version 24.x.x
```

---

## 🔑 STEP 5: Configure AWS CLI + Login to ECR

### 🔹 Install AWS CLI

```
sudo apt install awscli -y
```

### 🔹 Configure

```
aws configure
```

Input:

```
AWS Access Key ID: ********
AWS Secret Access Key: ********
Region: ap-south-1
```

### 🔹 Login to ECR

```
aws ecr get-login-password --region ap-south-1 | \
docker login --username AWS --password-stdin 123456789012.dkr.ecr.ap-south-1.amazonaws.com
```

### 🔹 Output

```
Login Succeeded
```

---

## 🐳 STEP 6: Create Sample App

### 📄 app/app.py

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "CI/CD Pipeline Working 🚀"

app.run(host='0.0.0.0', port=5000)
```

---

### 📄 requirements.txt

```
flask
```

---

## 🐳 STEP 7: Dockerfile

```
FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app/app.py"]
```

---

## 🧪 STEP 8: Test Docker Locally (EC2)

### 🔹 Build Image

```
docker build -t my-app .
```

### 🔹 Output

```
Successfully built abc123
```

---

### 🔹 Run Container

```
docker run -d -p 80:5000 my-app
```

---

### 🔹 Check Running Container

```
docker ps
```

### 🔹 Output

```
CONTAINER ID   IMAGE     STATUS      PORTS
abc123         my-app    Up          0.0.0.0:80->5000/tcp
```

---

### 🔹 Test in Browser

```
http://<EC2-PUBLIC-IP>
```

### 🔹 Output

```
CI/CD Pipeline Working 🚀
```

---

## 🔐 STEP 9: GitHub Secrets

Go to:
GitHub → Repo → Settings → Secrets

Add:

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION=ap-south-1
ECR_REPOSITORY=123456789012.dkr.ecr.ap-south-1.amazonaws.com/my-app
EC2_HOST=<your-ec2-ip>
EC2_USER=ubuntu
EC2_SSH_KEY=<your-private-key>
```

---

## 🔄 STEP 10: GitHub Actions Workflow

### 📄 .github/workflows/deploy.yml

```
name: CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout
      uses: actions/checkout@v3

    - name: AWS Login
      uses: aws-actions/configure-aws-credentials@v2
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: ${{ secrets.AWS_REGION }}

    - name: ECR Login
      uses: aws-actions/amazon-ecr-login@v1

    - name: Build Image
      run: docker build -t my-app .

    - name: Tag Image
      run: docker tag my-app:latest ${{ secrets.ECR_REPOSITORY }}:latest

    - name: Push Image
      run: docker push ${{ secrets.ECR_REPOSITORY }}:latest

    - name: Deploy to EC2
      uses: appleboy/ssh-action@v0.1.6
      with:
        host: ${{ secrets.EC2_HOST }}
        username: ${{ secrets.EC2_USER }}
        key: ${{ secrets.EC2_SSH_KEY }}
        script: |
          docker pull ${{ secrets.ECR_REPOSITORY }}:latest
          docker stop app || true
          docker rm app || true
          docker run -d -p 80:5000 --name app ${{ secrets.ECR_REPOSITORY }}:latest
```

---

## 🚀 STEP 11: Push Code

```
git add .
git commit -m "setup cicd pipeline"
git push origin main
```

---

## 📊 STEP 12: GitHub Actions Output

### 🔹 Successful Logs

```
Build Image ✔
Push to ECR ✔
Deploy to EC2 ✔
```

---

## 🌐 FINAL OUTPUT

Open:

```
http://<EC2-PUBLIC-IP>
```

### ✅ Output

```
CI/CD Pipeline Working 🚀
```

---

## 🧪 EXTRA TEST CASES

### 🔹 Update Code

Change:

```
return "Version 2 🚀"
```

Push again:

```
git commit -am "update app"
git push
```

### 🔹 Output

```
Version 2 🚀
```

---

## 🛠️ Troubleshooting

### ❌ Docker Permission Error

```
sudo chmod 666 /var/run/docker.sock
```

---

### ❌ Container Not Running

```
docker logs app
```

---

### ❌ ECR Push Failed

* Check IAM permissions
* Verify region

---

## 🔥 Advanced Improvements

* HTTPS with Nginx
* Auto-scaling (ECS)
* Blue/Green Deployment
* Monitoring (CloudWatch)

---

## 📌 Conclusion

✔ Automated CI/CD pipeline
✔ Dockerized application
✔ Real-world AWS DevOps project

---

## ⭐ Author

Dhaval Talekar


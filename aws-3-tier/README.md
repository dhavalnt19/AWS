# 🚀 AWS 3-Tier Architecture Project  
(VPC + ALB + EC2 + RDS)

---

## 📌 Project Overview

This project demonstrates a **production-ready 3-tier architecture** on AWS:

- **Presentation Layer** → Application Load Balancer (ALB)
- **Application Layer** → EC2 (Auto Scaling Group)
- **Database Layer** → Amazon RDS (MySQL)

---

## 🏗️ Architecture

- Users → ALB → EC2 → RDS
- Public Subnets → ALB
- Private Subnets → EC2 & RDS
- Secure communication using Security Groups

---

## 🧰 AWS Services Used

- Amazon VPC
- Public & Private Subnets
- Internet Gateway
- NAT Gateway
- Application Load Balancer (ALB)
- EC2 Instances
- Auto Scaling Group
- Amazon RDS (MySQL)
- IAM Roles
- Security Groups

---

## 📁 Project Structure


aws-3tier-architecture/
│
├── app/
│ ├── index.php
│ ├── db.php
│ └── config.php
│
├── scripts/
│ └── user-data.sh
│
├── screenshots/
│
├── architecture-diagram.png
│
└── README.md





---

## ⚙️ Step-by-Step Implementation

---

### 🔹 Step 1: Create VPC

- CIDR Block: `10.0.0.0/16`

Create Subnets:

| Type    | CIDR           |
|--------|----------------|
| Public 1 | 10.0.1.0/24 |
| Public 2 | 10.0.2.0/24 |
| Private 1 | 10.0.3.0/24 |
| Private 2 | 10.0.4.0/24 |

---

### 🔹 Step 2: Configure Internet & NAT Gateway

- Create **Internet Gateway**
- Attach it to VPC

- Create **NAT Gateway** in Public Subnet

#### Route Tables:

**Public Route Table**

0.0.0.0/0 → NAT Gateway





---

### 🔹 Step 3: Security Groups

#### ALB Security Group
- Allow: HTTP (80) from `0.0.0.0/0`

#### EC2 Security Group
- Allow: HTTP (80) from ALB SG only

#### RDS Security Group
- Allow: MySQL (3306) from EC2 SG only

---

### 🔹 Step 4: Launch EC2 Instances

- AMI: Amazon Linux 2
- Instance Type: t2.micro (Free Tier)

#### User Data Script (`scripts/user-data.sh`)

```bash
#!/bin/bash
yum update -y
yum install -y httpd php php-mysqlnd
systemctl start httpd
systemctl enable httpd



Step 5: Create RDS Database
Engine: MySQL
Instance Type: db.t3.micro
Storage: 20GB
Public Access: ❌ Disabled
Subnet: Private Subnets only
🔹 Step 6: Create Application Load Balancer
Type: Internet-facing
Listener: HTTP (80)
Attach Public Subnets
Target Group:
Target Type: Instances
Register EC2 instances
🔹 Step 7: Configure Auto Scaling Group
Minimum: 2 instances
Maximum: 4 instances
Attach to ALB Target Group

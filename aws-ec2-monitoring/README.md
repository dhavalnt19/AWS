# 🚀 AWS EC2 Monitoring with CloudWatch + SNS Alerts

## 📌 Project Overview

This project demonstrates how to monitor an AWS EC2 instance using **Amazon CloudWatch** and send alerts using **Amazon SNS** when CPU utilization exceeds a threshold.

---

## 🏗️ Architecture

EC2 Instance → CloudWatch Metrics → CloudWatch Alarm → SNS → Email Notification

---

## 🛠️ AWS Services Used

* Amazon EC2
* Amazon CloudWatch
* Amazon SNS

---

## ⚙️ Step 1: Launch EC2 Instance

1. Go to AWS Console → EC2
2. Click **Launch Instance**
3. Choose:

   * AMI: Amazon Linux 2
   * Instance Type: t2.micro (Free Tier)
4. Configure:

   * Allow SSH (Port 22)
5. Launch instance and download key pair

📸 Add Screenshot:
![EC2](screenshots/ec2-instance.png)

---

## 🔐 Step 2: Connect to EC2

```bash
chmod 400 key.pem
ssh -i key.pem ec2-user@<PUBLIC-IP>
```

---

## 📊 Step 3: Install Stress Tool

```bash
sudo yum update -y
sudo yum install stress -y
```

Create script:

```bash
nano stress.sh
```

Paste:

```bash
#!/bin/bash
stress --cpu 2 --timeout 300
```

Run:

```bash
chmod +x stress.sh
./stress.sh
```

---

## 📈 Step 4: Create CloudWatch Alarm

1. Go to CloudWatch → Alarms
2. Click **Create Alarm**
3. Select metric:

   * EC2 → Per-Instance Metrics → CPUUtilization
4. Set:

   * Threshold: Greater than 70%
   * Period: 1 minute

📸 Add Screenshot:
![CloudWatch](screenshots/cloudwatch-metric.png)

---

## 🔔 Step 5: Create SNS Topic

1. Go to SNS → Topics → Create Topic
2. Name: `EC2-Alerts`
3. Create Subscription:

   * Protocol: Email
   * Enter your email
4. Confirm email subscription

📸 Add Screenshot:
![SNS](screenshots/sns-email.png)

---

## 🚨 Step 6: Attach SNS to Alarm

* In CloudWatch Alarm:

  * Select SNS Topic created
  * Save Alarm

📸 Add Screenshot:
![Alarm](screenshots/alarm-created.png)

---

## 🧪 Step 7: Test Alert

Run:

```bash
./stress.sh
```

Expected:

* CPU spikes
* Alarm triggers
* Email notification received ✅

---

## 📬 Example Alert Email

```
ALARM: CPUUtilization > 70%
Instance: i-xxxxxxxx
Status: Triggered
```

---

## 📊 Expected Output

| Component    | Result              |
| ------------ | ------------------- |
| EC2 Instance | Running             |
| CloudWatch   | CPU Metrics Visible |
| Alarm        | Triggered           |
| SNS          | Email Sent          |

---

## 💡 Key Learnings

* Monitor EC2 using CloudWatch
* Create real-time alerts
* Automate notifications with SNS

---

## 🔥 Future Improvements

* Add Slack notifications
* Monitor memory using custom metrics
* Use Auto Scaling based on alarms

---

## 📌 Author

Dhaval Talekar

---


# 🚀 AWS Serverless Image Processing (S3 + Lambda + DynamoDB)

## 📌 Project Overview

This project demonstrates a **serverless image processing pipeline** using AWS services.

When an image is uploaded to S3:

1. AWS Lambda is triggered
2. Image is resized
3. Resized image is stored in S3
4. Metadata is saved in DynamoDB

---

## 🏗️ Architecture

S3 (Upload Image)
↓
Lambda Function (Resize Image)
↓
S3 (Store Resized Image)
↓
DynamoDB (Store Metadata)

---

## 🛠️ AWS Services Used

* Amazon S3
* AWS Lambda
* Amazon DynamoDB
* IAM (Roles & Permissions)

---

## 📂 Project Structure

```
aws-serverless-image-processing/
│
├── lambda/
│   ├── resize_image.py
│   └── requirements.txt
│
├── images/
│   └── sample.jpg
│
└── README.md
```

---

## ⚙️ Step-by-Step Setup

### 1️⃣ Create S3 Bucket

* Go to AWS S3
* Create bucket: `image-processing-bucket-<your-name>`
* Disable block public access (optional)
* Enable event notifications

---

### 2️⃣ Create DynamoDB Table

* Table name: `ImageMetadata`
* Partition key: `image_name` (String)

---

### 3️⃣ Create IAM Role for Lambda

Attach policies:

* AmazonS3FullAccess
* AmazonDynamoDBFullAccess
* AWSLambdaBasicExecutionRole

---

### 4️⃣ Prepare Lambda Deployment Package

```bash
mkdir package
pip install -r requirements.txt -t package/
cd package
zip -r ../function.zip .
cd ..
zip -g function.zip resize_image.py
```

---

### 5️⃣ Create Lambda Function

* Runtime: Python 3.9+
* Upload `function.zip`
* Set handler:

```
resize_image.lambda_handler
```

---

### 6️⃣ Set Environment Variable

| Key        | Value         |
| ---------- | ------------- |
| TABLE_NAME | ImageMetadata |

---

### 7️⃣ Add S3 Trigger

* Go to Lambda → Add trigger
* Select S3
* Event type: PUT
* Prefix: (optional)

---

## 🧪 Testing

### Upload Image

```bash
aws s3 cp sample.jpg s3://your-bucket-name/
```

---

### Expected Output

* ✅ Resized image created:

```
resized-sample.jpg
```

* ✅ DynamoDB Entry:

```
{
  "image_name": "sample.jpg",
  "resized_image": "resized-sample.jpg"
}
```

---

## 🔍 Logs

Check logs in CloudWatch:

```
Processing file sample.jpg from bucket image-processing-bucket
```

---

## 🚀 Improvements

* Add multiple image sizes
* Use S3 separate output bucket
* Add API Gateway for upload
* Add Rekognition for image analysis
* Add SNS notifications

---

## 📌 Real-World Use Cases

* Image thumbnails for websites
* Profile picture resizing
* E-commerce product images
* Media processing pipelines

---

## 👨‍💻 Author

Dhaval Talekar

---

## ⭐ GitHub Tips

```bash
git init
git add .
git commit -m "AWS Serverless Image Processing Project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/aws-serverless-image-processing.git
git push -u origin main
```

---


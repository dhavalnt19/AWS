# 🚀 AWS Static Website Hosting (S3 + CloudFront)

## 📌 Overview

This project demonstrates how to host a static website using AWS services:

* Amazon S3 (storage + static hosting)
* Amazon CloudFront (CDN + HTTPS)
* (Optional) Route 53 (custom domain)

---

## 🧱 Architecture

S3 (Origin) → CloudFront (CDN) → End Users

---

## 📁 Project Structure

```
aws-static-website/
│
├── index.html
├── error.html
├── styles.css
├── images/
└── README.md
```

---

## 🛠️ AWS Services Used

* Amazon S3
* Amazon CloudFront
* AWS IAM
* Amazon Route 53 (optional)

---

# ⚙️ Step-by-Step Setup

## 1️⃣ Create Static Website Files

### index.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>AWS Static Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>🚀 Hosted on AWS S3 + CloudFront</h1>
    <p>Cybersecurity Project</p>
</body>
</html>
```

### styles.css

```css
body {
    font-family: Arial;
    text-align: center;
    margin-top: 100px;
    background-color: #0f172a;
    color: white;
}
```

---

## 2️⃣ Create S3 Bucket

1. Go to AWS Console → S3
2. Click **Create Bucket**
3. Enter bucket name:

   ```
   your-unique-bucket-name
   ```
4. Select region (recommended: nearest to you)
5. Uncheck:

   * ❌ Block all public access
6. Create bucket

---

## 3️⃣ Enable Static Website Hosting

1. Open your bucket
2. Go to **Properties**
3. Scroll to **Static Website Hosting**
4. Click **Enable**
5. Enter:

   * Index document: `index.html`
   * Error document: `error.html`
6. Save

---

## 4️⃣ Add Bucket Policy (Public Access)

Go to **Permissions → Bucket Policy** and add:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicRead",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-unique-bucket-name/*"
    }
  ]
}
```

---

## 5️⃣ Upload Website Files

Upload:

* index.html
* styles.css
* error.html

Make sure files are public.

---

## 6️⃣ Create CloudFront Distribution

1. Go to CloudFront
2. Click **Create Distribution**

### Origin Settings:

* Origin domain → Select your S3 bucket

### Default Cache Behavior:

* Viewer Protocol Policy → Redirect HTTP to HTTPS

### Settings:

* Default root object → `index.html`

3. Click **Create Distribution**
4. Wait 5–10 minutes for deployment

---

## 7️⃣ Access Your Website

After deployment, open:

```
https://your-distribution-id.cloudfront.net
```

---

## 8️⃣ (Optional) Setup Custom Domain

Using Route 53:

1. Register a domain
2. Create Hosted Zone
3. Request SSL certificate (ACM)
4. Add domain to CloudFront
5. Create A record pointing to CloudFront

---

# 🧪 Testing

| Test                | Expected Result    |
| ------------------- | ------------------ |
| Open CloudFront URL | Website loads      |
| HTTP access         | Redirects to HTTPS |
| Invalid URL         | Shows error.html   |

---

# 🔐 Security Best Practices

* Use **Origin Access Control (OAC)** instead of public bucket
* Enable **CloudFront logging**
* Add **AWS WAF** for protection
* Use **IAM least privilege access**

---

# 🚀 Future Improvements

* CI/CD with GitHub Actions
* Versioning in S3
* Monitoring with CloudWatch
* Add custom error pages

---

# 📸 Output

Your website will look like:

* Dark themed static page
* Hosted globally using CDN
* HTTPS enabled

---

# 💡 Interview Questions

* Why use CloudFront over direct S3?
* What is CDN?
* How to secure S3 bucket?
* What is edge location?

---

# 🧾 Author

Dhaval Talekar
Cybersecurity & Cloud Projects


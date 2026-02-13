# Serverless Web Application on AWS

## 📌 Project Level
Advanced / Industry-Level Internship Project

---

## 📖 Project Description
This project demonstrates the design and implementation of a fully serverless web application using Amazon Web Services (AWS).  
The application is built entirely using managed AWS services without provisioning or managing traditional servers.

The system allows users to submit data through a web interface, which is processed by AWS Lambda and stored securely in Amazon DynamoDB.

---

## 🎯 Objectives
- To understand serverless cloud architecture
- To build backend logic using AWS Lambda
- To expose backend services using Amazon API Gateway
- To store application data using Amazon DynamoDB
- To host a static frontend using Amazon S3
- To follow AWS Free Tier usage and cost optimization practices

---

## 🛠️ Technologies & Services Used
- AWS Lambda  
- Amazon API Gateway (HTTP API)  
- Amazon DynamoDB  
- Amazon S3 (Static Website Hosting)  
- AWS Identity and Access Management (IAM)  
- HTML & JavaScript  
- Git & GitHub  

---

## 🧩 System Architecture
User → Amazon S3 (Static Website) → API Gateway → AWS Lambda → DynamoDB

---

## 🚀 Implementation Steps (Serverless Web App: API Gateway + Lambda + DynamoDB + S3)

### ✅ Step 1: Create a DynamoDB Table

1. Login to **AWS Management Console**
2. Go to: **DynamoDB → Tables → Create table**
3. Enter:
   - **Table name**: `UserDataTable` (example)
   - **Partition key**: `id` (String)
4. Keep other settings as default
5. Click **Create table**

---

### ✅ Step 2: Create a Lambda Function (Python)

1. Go to: **AWS Lambda → Create function**
2. Select:
   - **Author from scratch**
3. Enter:
   - Function name: `StoreUserDataFunction`
   - Runtime: **Python 3.x**
4. Click **Create function**
5. Add code to:
   - Receive API request data
   - Process the request
   - Store the data into DynamoDB
For code refer to Above `Lambda` Folder in the Repository.

---

### ✅ Step 3: Configure API Gateway to Trigger Lambda

1. Go to: **API Gateway → Create API**
2. Select:
   - **HTTP API** (recommended for simple REST endpoints)
3. Add integration:
   - Choose **Lambda**
   - Select your Lambda function
4. Create a route:
   - Example: `POST /submit`
5. Deploy the API and copy the API endpoint URL

---

### ✅ Step 4: Enable CORS (Frontend ↔ Backend Communication)

1. Inside API Gateway, go to:
   - **CORS settings**
2. Enable CORS
3. Allow:
   - Methods: `POST`, `GET`, `OPTIONS`
   - Headers: `Content-Type`
   - Origins: `*` (for demo) OR your S3 website URL (recommended)

---

### ✅ Step 5: Host the Frontend Using Amazon S3 Static Website Hosting

1. Go to: **S3 → Create bucket**
2. Upload your frontend files:
   - `index.html`
   - `style.css`
   - `script.js`
3. Enable:
   - **Static website hosting**
4. Set:
   - Index document: `index.html` in setting Ststic Website Hosting property
5. Make the bucket public using a bucket policy (required for website access)

---

### ✅ Step 6: Connect Frontend with API Endpoint

1. Open frontend JavaScript file (example: `script.js`)
2. Paste the deployed API Gateway endpoint URL
3. Update the request method to call:
   - `POST /submit` route      

---

### ✅ Step 7: Verify Data Storage in DynamoDB

1. Open DynamoDB table
2. Go to:
   - **Explore table items**
3. Submit form data from the frontend
4. Confirm that records are successfully inserted into DynamoDB

---

### ✅ Step 8: Delete AWS Resources (To Avoid Charges)

If you created this project only for learning/demo purpose, it is recommended to delete resources after testing to avoid unnecessary charges.

Delete the following resources:
- Lambda function
- API Gateway
- DynamoDB table
- S3 bucket (including uploaded objects)

---

---

## 🔐 Security & Best Practices
- IAM roles used to grant minimum required permissions to Lambda.
- Root account was not used for project implementation.
- Principle of Least Privilege followed.
- AWS Free Tier services utilized.
- Resources cleaned up after completion.

---

## ✅ Conclusion
This project provided practical exposure to modern serverless cloud architecture.  
It demonstrates how scalable, secure, and cost-effective applications can be built without managing infrastructure.

The implementation reflects real-world cloud deployment practices used in industry.

---

## 🔮 Future Scope
- Implement authentication using Amazon Cognito
- Integrate Amazon CloudFront for HTTPS delivery
- Add multiple API endpoints
- Implement logging using CloudWatch
- Add monitoring and error tracking

---

## 👤 Author
Umesh Saini  
AWS Project
2026

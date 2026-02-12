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

## 🚀 Implementation Steps
1. Created a DynamoDB table for storing user-submitted data.
2. Developed a Lambda function (Python) to process API requests and store data in DynamoDB.
3. Configured API Gateway to trigger the Lambda function.
4. Enabled CORS to allow frontend-backend communication.
5. Hosted the frontend application using Amazon S3 static website hosting.
6. Connected the frontend to the deployed API endpoint.
7. Verified successful data storage inside DynamoDB.
8. Captured screenshots for internship documentation.
9. Deleted AWS resources after project completion to prevent unnecessary charges.

---

## 🔐 Security & Best Practices
- IAM roles used to grant minimum required permissions to Lambda.
- Root account was not used for project implementation.
- Principle of Least Privilege followed.
- AWS Free Tier services utilized.
- Resources cleaned up after completion.

---

## 💰 Cost Management
- Project executed within AWS Free Tier limits.
- No long-running compute services used.
- AWS resources were deleted after demonstration.
- Budget monitoring considered during implementation.

---

## 📸 Screenshots Included
- Lambda Function Configuration & Code
- API Gateway Route & Invoke URL
- DynamoDB Table with Stored Items
- S3 Static Website Hosting Output
- GitHub Repository Structure

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

# 🚀 AWS Elastic Beanstalk & RDS: Secure Multi-Tier VPC Deployment

---

## 👤 Author
**Pratiksha Lavand**  
Master of Computer Applications (MCA)  
Savitribai Phule Pune University  
Aspiring Cloud Architect | Cloud & DevOps Enthusiast  

---

## 📌 Project Overview

This project demonstrates the deployment of a **highly available and secure multi-tier web application on AWS**.  
It uses:

- AWS Elastic Beanstalk for managed application deployment  
- Amazon RDS for a persistent relational database  
- Custom VPC for network isolation and security  

### 🎯 Key Objectives

- Provision a managed web environment using Elastic Beanstalk  
- Integrate a private Amazon RDS database within the same VPC  
- Implement secure communication using Security Group referencing  
- Validate backend connectivity using an isolated EC2 management instance  

---

## 🏗️ Architecture Diagram

The application follows a standard **three-tier architecture**:

![Architecture Diagram](https://github.com/user-attachments/assets/7d14afda-b0a8-48c7-b1ba-f6fd1a51dc7f)

### Architecture Layers:

- **Public Tier:** Elastic Beanstalk EC2 instances (Web Server)  
- **Private Tier:** Amazon RDS (Database - No public access)  
- **Management Tier:** EC2 instance for administrative operations  

---

## ⚙️ Deployment & Configuration Steps

---

### 📍 Phase 1: Environment & Application Setup

- Created Elastic Beanstalk application using **Python 3.11 platform**
- Configured environment and deployment tier

#### Environment Selection
![Environment Tier](https://github.com/user-attachments/assets/582f07f4-1c53-4b79-a02c-93a833976d96)

#### Networking & VPC Configuration
![VPC Selection](https://github.com/user-attachments/assets/16f4159e-5bb2-442b-870b-010371c8d1d5)

#### Deployment Health Status
![EC2 Status](https://github.com/user-attachments/assets/3d9df3cc-ad80-459c-9927-bfe301b8ecf4)

---

### 📍 Phase 2: Compute & Storage Configuration

- Configured EC2 instances managed by Elastic Beanstalk  
- Optimized storage using **gp3 volume type**

#### Security Group & Storage Configuration
![Security Group](https://github.com/user-attachments/assets/43f7b039-73a1-4526-bcc3-1310c784aa54)

#### SSH Access Verification (Management Instance)
![SSH Access](https://github.com/user-attachments/assets/5aad6f96-d6e1-4152-a678-9bc60ec2d704)

---

### 📍 Phase 3: Secure Database Integration

- Provisioned **Amazon RDS (MySQL)** in private subnet  
- Disabled public access for security  
- Allowed access only via EC2 Security Group

#### RDS Connectivity Details
![RDS Details](https://github.com/user-attachments/assets/434bcb9c-cd5d-4593-9b17-88cbee7b4f5c)

#### Inbound Rule (Port 3306 MySQL)
![RDS Inbound Rules](https://github.com/user-attachments/assets/da0178eb-8a32-43a4-8e30-f3a4fd600cc5)

---

### 📍 Phase 4: Application Deployment

- Packaged Flask application  
- Deployed via Elastic Beanstalk console  

#### Source Code Upload
![Upload Code](https://github.com/user-attachments/assets/66f836be-d23e-4b62-b527-abf0fffe8608)

#### EC2 Security Configuration
![EC2 Security](https://github.com/user-attachments/assets/4c076ae0-b6d0-460c-8aec-9ae5639f4eca)

---

## 💻 Technical Implementation (Terminal Steps)

### 🖥️ Management EC2 Setup

```bash
# Set hostname
sudo hostnamectl set-hostname rds-client-ec2

# Update system and install database client
sudo dnf update -y
sudo dnf install mariadb105-server -y

🗄️ Database Setup (RDS MySQL)
-- Connect to RDS
mysql -h <YOUR_RDS_ENDPOINT> -u admin -p

-- Create database and table
CREATE DATABASE ebdb;
USE ebdb;

CREATE TABLE visits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    msg VARCHAR(255)
);

INSERT INTO visits (msg)
VALUES ('Hello from Elastic Beanstalk!');

SELECT * FROM visits;
EXIT;
```
<img width="1919" height="973" alt="14_db_connection_success" src="https://github.com/user-attachments/assets/389bda6e-de88-466c-9e38-0f4c308c9e9f" />

📊 Final Status & Results
EC2 Instances Status
<img width="1919" height="869" alt="INF_02_Final_EC2_Instances_Status_Running" src="https://github.com/user-attachments/assets/bd6975e6-205b-43b8-b220-e6ce41aa2f95" />

Deployment Health Logs
🎉 Final Application Output
<img width="1919" height="1016" alt="output" src="https://github.com/user-attachments/assets/092a80e0-83b1-4860-8705-7553b86d2d0c" />
🛠️ Skills Demonstrated
☁️ AWS Cloud Infrastructure (VPC, EC2, RDS)
⚙️ Elastic Beanstalk Automation
🔐 Security Groups & Network Isolation
🗄️ MySQL Database Management (RDS)
🐧 Linux System Administration
🚀 CI/CD Deployment Concepts

🏁 Conclusion

This project successfully demonstrates a secure, scalable, and production-ready AWS multi-tier architecture, combining compute, networking, and database services with strong security practices.
# Install Python dependencies
sudo yum install python3-pip -y
pip3 install mysql-connector-python pymysql

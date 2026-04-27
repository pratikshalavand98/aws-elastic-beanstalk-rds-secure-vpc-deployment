# 🚀 AWS Elastic Beanstalk & RDS: Secure Multi-Tier VPC Deployment

## 📌 Project Overview
This project demonstrates the deployment of a **highly available and secure multi-tier web application on AWS**. It utilizes managed services within a custom network to ensure data isolation, security, and scalability.

### 🎯 Key Objectives
- Provision a managed web environment using **AWS Elastic Beanstalk**
- Integrate a private **Amazon RDS (MySQL)** database inside a Custom VPC
- Enable secure communication using **Security Group referencing**
- Validate backend connectivity using a dedicated **EC2 management instance**

---

## 🏗️ Architecture Overview
The application follows a **three-tier architecture (Web Tier + App Tier + Database Tier)** ensuring separation of concerns and security.

![Architecture Diagram](https://github.com/user-attachments/assets/7d14afda-b0a8-48c7-b1ba-f6fd1a51dc7f)

---

## ⚙️ Deployment & Configuration Steps

### 📍 Phase 1: Elastic Beanstalk Environment Setup
- Created Elastic Beanstalk application using **Python 3.11 platform**
- Configured environment with proper networking inside Custom VPC

📷 Environment Tier Setup  
![Environment Tier](https://github.com/user-attachments/assets/582f07f4-1c53-4b79-a02c-93a833976d96)

📷 VPC Configuration  
![VPC Selection](https://github.com/user-attachments/assets/16f4159e-5bb2-442b-870b-010371c8d1d5)

---

### 📍 Phase 2: EC2 Management Instance Setup
To manage and test the private RDS database, a dedicated EC2 instance was launched.

#### 🖥️ Instance Details:
- AMI: Amazon Linux 2023
- Instance Type: t2.micro
- Network: Custom VPC (Public Subnet)

📷 AMI Selection  
![AMI Selection](https://github.com/user-attachments/assets/4833742a-47f9-42f1-b467-1f7f1b30813a)

📷 VPC Configuration for EC2  
![EC2 VPC Setup](https://github.com/user-attachments/assets/031e335b-b97c-401f-9584-9363424aa994)

---

## 💻 Technical Implementation (SSH & Commands)
### 🔐 SSH Connection
SSH is used to securely connect to the EC2 instance from the local machine.

```bash
ssh -i path/keyname.pem ec2-user@public_ip
```
### 🔧 1. System Setup & Dependencies

```bash
# Set hostname
sudo hostnamectl set-hostname rds-client-ec2

# Update system packages
sudo dnf update -y

# Install database client
sudo dnf install mariadb105-server -y
sudo dnf install nmap-ncat -y

# Install Python & dependencies
sudo yum install python3 -y
sudo yum install python3-pip -y

pip3 install mysql-connector-python pymysql
```

## 🗄️ 2. Database Configuration (RDS - MySQL)

```sql
-- Connect to RDS instance
mysql -h <YOUR_RDS_ENDPOINT> -u admin -p

-- Create database
CREATE DATABASE ebdb;
USE ebdb;

-- Create table
CREATE TABLE visits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    msg VARCHAR(255)
);

-- Insert test data
INSERT INTO visits (msg) VALUES ('Hello from Elastic Beanstalk!');

-- Verify data
SELECT * FROM visits;

EXIT;
```
<img width="1919" height="973" alt="14_db_connection_success" src="https://github.com/user-attachments/assets/48050c94-bb41-4488-92b9-99efa4adabcb" />



📍 Phase 3: Application Deployment
Packaged Flask application into .zip format
Uploaded and deployed using AWS Elastic Beanstalk Console
Verified successful deployment and health status


<img width="1919" height="872" alt="DEP_03_Uploading_Application_Source_Code" src="https://github.com/user-attachments/assets/e3bddcba-bcfa-4858-bb86-d4a6106002ab" />



📊 Final Results
✅ Infrastructure Status
Elastic Beanstalk Environment: Healthy

<img width="1919" height="868" alt="15_final_health_ok" src="https://github.com/user-attachments/assets/31637cb1-2125-4ca9-9c47-3f6cadd06030" />

EC2 Instance: Running

<img width="1919" height="869" alt="INF_02_Final_EC2_Instances_Status_Running" src="https://github.com/user-attachments/assets/41f1cdff-0654-47c0-9882-de97e8bf5fc0" />
RDS Database: Available & Connected

🎉 Final Output

<img width="1919" height="1016" alt="output" src="https://github.com/user-attachments/assets/391f64af-7135-4fdd-927d-c0c30114e086" />

Application successfully connected to backend database and displayed live data.

## 🛠️ Skills Demonstrated

- ☁️ AWS Cloud Infrastructure (VPC, EC2, RDS)
- ⚙️ Elastic Beanstalk Deployment Automation
- 🔐 Cloud Security (Security Groups & Private Subnets)
- 🐧 Linux Administration (SSH, package management)
- 🧠 Database Management (MySQL on RDS)
- 🧩 Multi-tier Architecture Design


## 👤 Author

**Pratiksha Lavand**  
Master of Computer Applications (MCA)  
Savitribai Phule Pune University
💡 Aspiring Cloud & DevOps Engineer


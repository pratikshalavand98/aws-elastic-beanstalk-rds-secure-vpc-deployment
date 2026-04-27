# 🚀 AWS Elastic Beanstalk & RDS: Secure Multi-Tier VPC Deployment

## 📌 Project Overview
This project demonstrates the deployment of a **highly available and secure multi-tier web application on AWS**. It utilizes managed services within a custom network to ensure data isolation, high performance, and scalability.

### 🎯 Key Objectives
- Provision a managed web environment using **AWS Elastic Beanstalk**.
- Integrate a private **Amazon RDS (MySQL)** database within the same VPC.
- Implement secure communication using **Security Group referencing**.
- Validate backend connectivity using an isolated **EC2 management instance**.

---

## 🏗️ Architecture Diagram
The application follows a standard **three-tier architecture**:

![Architecture Diagram](https://github.com/user-attachments/assets/7d14afda-b0a8-48c7-b1ba-f6fd1a51dc7f)

---

## ⚙️ Deployment & Configuration Steps

### 📍 Phase 1: Environment & Application Setup
- Created Elastic Beanstalk application using the **Python 3.11 platform**.
- **Environment Selection:** ![Environment Tier](https://github.com/user-attachments/assets/582f07f4-1c53-4b79-a02c-93a833976d96)
- **VPC Configuration:** ![VPC Selection](https://github.com/user-attachments/assets/16f4159e-5bb2-442b-870b-010371c8d1d5)

### 📍 Phase 2: Manual EC2 Management Client Setup
To manage the private RDS instance, I manually provisioned a standalone EC2 instance (`rds-client-ec2`) within the Custom VPC.

1. **Launch Instance:** Selected **Amazon Linux 2023 AMI** with **t3.micro**.
   ![AMI Selection](https://github.com/user-attachments/assets/4833742a-47f9-42f1-b467-1f7f1b30813a)
2. **Network Config:** Placed in the project VPC with a Public IP and SSH access.
   ![VPC Selection for EC2](https://github.com/user-attachments/assets/031e335b-b97c-401f-9584-9363424aa994)

---

## 💻 Technical Implementation (SSH & Terminal Steps)

Ek baar instance launch hone ke baad, maine SSH ke zariye connect kiya aur ye commands follow kiye:

### 🖥️ 1. System & Dependencies Setup
```bash
# Connecting to the instance and setting up the environment
sudo hostnamectl set-hostname rds-client-ec2

# Updating system and installing database client
sudo dnf update -y
sudo dnf install mariadb105-server -y
sudo dnf install nmap-ncat -y

# Installing Python and required connectors
sudo yum install python3-pip -y
sudo yum install python3 -y
pip3 install mysql-connector-python pymysql
```
🗄️ 2. Database Connectivity & Table Creation
I connected to the private RDS endpoint to initialize the schema:
-- Connect to RDS
mysql -h <YOUR_RDS_ENDPOINT> -u admin -p

-- Commands executed in RDS Terminal
CREATE DATABASE ebdb;
USE ebdb;

CREATE TABLE visits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    msg VARCHAR(255)
);

INSERT INTO visits (msg) VALUES ('Hello from Elastic Beanstalk!');
SELECT * FROM visits;
EXIT;
📍 Phase 3: Application Deployment
Packaged the Flask application into a .zip bundle.

Deployed via the Elastic Beanstalk console.
📊 Final Status & Results
Infrastructure Health Status
Verified EC2 Dashboard (All Instances Running)
🎉 Final Live Application Output
🛠️ Skills Demonstrated
☁️ AWS Cloud Infrastructure: VPC, EC2, RDS (Private/Public Networking).

⚙️ Elastic Beanstalk Automation: Managed deployment and health monitoring.

🔐 Security: Security Group Referencing & Network Isolation.

🐧 Linux Administration: SSH, Package Management, and Bash Scripting.

👤 Author
Pratiksha Lavand Master of Computer Applications (MCA) | Savitribai Phule Pune University

Aspiring Cloud Architect | Cloud & DevOps Enthusiast

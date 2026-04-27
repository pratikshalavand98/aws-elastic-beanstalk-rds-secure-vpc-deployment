AWS Elastic Beanstalk & RDS: Secure Multi-Tier VPC Deployment
📌 Project Overview
This project demonstrates the deployment of a highly available and secure multi-tier web application on AWS. It utilizes AWS Elastic Beanstalk for automated environment management and Amazon RDS for a persistent relational database backend, all residing within a Custom VPC to ensure network isolation and security.

Key Objectives:
Provision a managed web environment using Elastic Beanstalk.

Integrate a private Amazon RDS instance within the same VPC.

Implement strict security through Security Group Referencing.

Verify backend connectivity using an isolated EC2 management client.

🏗️ Architecture
The application follows a standard three-tier architecture:
<img width="1383" height="1137" alt="architecture_diagram" src="https://github.com/user-attachments/assets/7d14afda-b0a8-48c7-b1ba-f6fd1a51dc7f" />


Public Tier: Elastic Beanstalk managed EC2 instances (Web Server).

Private Tier: Amazon RDS (Database) hidden from the public internet.

Management Tier: A standalone EC2 instance for administrative database tasks.

⚙️ Deployment & Configuration Steps
Phase 1: Environment & Application Creation
Creating the Elastic Beanstalk Application and defining the platform (Python 3.11).

Creating the EB Environment > <img width="1919" height="865" alt="01_env_tier_selection" src="https://github.com/user-attachments/assets/582f07f4-1c53-4b79-a02c-93a833976d96" />


Networking & Traffic Configuration > <img width="1919" height="871" alt="05_vpc_selection" src="https://github.com/user-attachments/assets/16f4159e-5bb2-442b-870b-010371c8d1d5" />


Deployment Policies & Health > <img width="1919" height="869" alt="INF_02_Final_EC2_Instances_Status_Running" src="https://github.com/user-attachments/assets/3d9df3cc-ad80-459c-9927-bfe301b8ecf4" />


Phase 2: Compute & Storage Configuration
Configured the EC2 instances that power the Beanstalk environment.

Storage Optimization (gp3) > 
<img width="1919" height="844" alt="SG_01_RDS_Inbound_Rules" src="https://github.com/user-attachments/assets/43f7b039-73a1-4526-bcc3-1310c784aa54" />


SSH Access Verification (Managed Instance) > 
<img width="1919" height="913" alt="EB_INST_01_Provisioned_by_Beanstalk" src="https://github.com/user-attachments/assets/5aad6f96-d6e1-4152-a678-9bc60ec2d704" />


Phase 3: Secure Database Integration
A private RDS instance was provisioned with specific rules to block all public traffic.

RDS Connectivity Details > 
<img width="1919" height="872" alt="RDS_13_Database_Connectivity_and_Security_Details" src="https://github.com/user-attachments/assets/434bcb9c-cd5d-4593-9b17-88cbee7b4f5c" />


Security Group Identification > Yahan wo screenshot jisme aapne RDS ka Security Group select kiya hai.

Inbound Traffic Authorization (Port 3306) > 
<img width="1919" height="857" alt="SG_10_Authorizing_RDS_Inbound_Traffic" src="https://github.com/user-attachments/assets/da0178eb-8a32-43a4-8e30-f3a4fd600cc5" />


Phase 4: Application Deployment
The Flask-based application was bundled and deployed.

Source Code Upload >
<img width="1919" height="872" alt="DEP_03_Uploading_Application_Source_Code" src="https://github.com/user-attachments/assets/66f836be-d23e-4b62-b527-abf0fffe8608" />


Final Security Rules (HTTP/SSH) > <img width="1919" height="857" alt="SG_02_EC2_Security_Config" src="https://github.com/user-attachments/assets/4c076ae0-b6d0-460c-8aec-9ae5639f4eca" />


💻 Technical Implementation (Terminal Operations)
steps follow kiye:

1. Preparing the Management Client
Bash
# Hostname update for identification
sudo hostnamectl set-hostname rds-client-ec2

# Installing MariaDB Client to interact with RDS
sudo dnf update -y
sudo dnf install mariadb105-server -y

# Installing Python dependencies for Flask App testing
sudo yum install python3-pip -y
pip3 install mysql-connector-python pymysql
2. Database Schema Setup

SQL
-- Connecting to RDS
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
exit;
<img width="1919" height="973" alt="14_db_connection_success" src="https://github.com/user-attachments/assets/8a5bb044-e48b-4d36-a313-a14739af4e9a" />



📊 Final Status & Results
The infrastructure was successfully verified with all health checks passing.

EC2 Dashboard Status (Both Instances Running) > 
<img width="1919" height="869" alt="INF_02_Final_EC2_Instances_Status_Running" src="https://github.com/user-attachments/assets/89eaa905-5218-4b68-88ac-d594980b85e2" />


Deployment Event Logs > 
<img width="1919" height="868" alt="15_final_health_ok" src="https://github.com/user-attachments/assets/12d64d0c-233f-442c-bd4e-25bd283e4c25" />

final output
<img width="1919" height="1016" alt="output" src="https://github.com/user-attachments/assets/a8f3eb68-3903-43eb-b7a5-43088e1065db" />


🛠️ Skills Demonstrated
Cloud Infrastructure: VPC, Subnets, EC2, RDS.

Automation: Elastic Beanstalk Environment Management.

Security: Security Group Referencing, Least Privilege Access.

Database Management: SQL Operations, RDS Connectivity.

Linux Administration: SSH, Package Management, Shell Commands.

👤 Author
Pratiksha Lavand
Master of Computer Applications (MCA)
Aspiring Cloud Architect | Savitribai Phule Pune University

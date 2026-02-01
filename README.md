# 🚀 CI/CD Pipeline & Infrastructure Automation

## 📌 Project Overview
**Role Focus:** Release Management & DevOps  
**Goal:** Orchestrated the software delivery lifecycle for a Java application, ensuring zero-downtime deployments and consistent infrastructure.

This project automates the release process:
1.  **Code Commit:** Developer pushes code to GitHub.
2.  **Automated Build:** AWS CodeBuild compiles the Java source using Maven.
3.  **Infrastructure:** Python scripts provision the VPC network environment.
4.  **Deployment:** Successful artifacts are released to AWS Elastic Beanstalk.

## 🛠 Technology Stack
| Category | Tool | Usage |
| :--- | :--- | :--- |
| **Release Tools** | Git, GitHub | Version Control & Branch Management |
| **CI/CD** | AWS CodePipeline | Orchestration of the release flow |
| **Build Tool** | Maven | Packaging Java artifacts (.war) |
| **IaC** | Python (Boto3) | Automating VPC & Database setup |
| **Cloud** | AWS Elastic Beanstalk | Hosting environment |

## 📂 Project Structure
* `my-java-app/`: Source code for the Java web application.
* `infra_scripts/`: Python scripts for provisioning AWS resources (VPC/RDS).
* `buildspec.yml`: Configuration file defining the build phases for AWS CodeBuild.

## 🚀 How to Replicate
1.  **Clone the Repo:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/aws-release-automation.git](https://github.com/YOUR_USERNAME/aws-release-automation.git)
    ```
2.  **Run Infrastructure Automation:**
    ```bash
    python infra_scripts/setup_infra.py
    ```
3.  **Trigger Release:**
    Pushing to the `main` branch automatically triggers the AWS Pipeline.
## 📝 Project Overview

This project is a BDD-style test automation framework using Behave and Selenium. It supports Allure reporting and is designed for scalable, maintainable UI testing.


# 🧪 Behave Test Automation

Automated end-to-end testing framework using [Behave](https://behave.readthedocs.io/en/stable/) (BDD for Python), [Selenium](https://www.selenium.dev/), and [Allure](https://docs.qameta.io/allure/) for rich test reporting. Integrated with Jenkins for CI/CD workflows.

---

## 🚀 Features

- ✅ BDD-style test scenarios with Gherkin syntax
- ✅ Selenium WebDriver for browser automation
- ✅ Allure reporting for visual test insights
- ✅ Jenkins integration for automated test execution
- ✅ Modular page object design for maintainability

---

## 📁 Project Structure

<img width="634" height="428" alt="Screenshot 2025-08-06 at 8 48 28 PM" src="https://github.com/user-attachments/assets/cad73515-f024-4eed-aa52-9bcc84090963" />


## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ADMehta/behave-test-automation.git
cd behave-test-automation

### 2. Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate

### 3. Install Required Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt

### 4. Run Tests with Allure Formatter
```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-results

### 5. Generate and View Allure Report (Optional)
```bash
allure generate allure-results --clean -o allure-report
allure open allure-report

💡 If allure is not recognized, install it via:
brew install allure       # macOS
npm install -g allure-commandline  # cross-platform


⚙️ Jenkins Installation & Startup

On Linus/Uuntu/Mac
# 1. Install Java (Jenkins requires Java 17+)
sudo apt update
sudo apt install openjdk-17-jdk -y

# 2. Add Jenkins repository and key
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null

# 3. Install Jenkins
sudo apt update
sudo apt install jenkins -y

# 4. Start Jenkins
sudo systemctl start jenkins

# 5. Enable Jenkins to start on boot
sudo systemctl enable jenkins

# 6. Check Jenkins status
sudo systemctl status jenkins
Access Jenkins at: http://localhost:8080


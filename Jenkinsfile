pipeline {
  agent any

  environment {
    PYTHONPATH = "${WORKSPACE}"
  }

  stages {
    stage('Clean Workspace') {
      steps {
        echo 'Cleaning workspace...'
        deleteDir() // Wipes Jenkins workspace
      }
    }

    stage('Setup') {
      steps {
        echo 'Installing dependencies...'
        sh 'python3 -m venv venv'
        sh '. venv/bin/activate && pip install --upgrade pip'
        sh '. venv/bin/activate && pip install -r requirements.txt'
      }
    }

    stage('Run Sanity Tests') {
      steps {
        echo 'Cleaning previous Allure results...'
        sh 'rm -rf reports/allure-results'

        echo 'Running Behave tests with Allure formatter...'
        sh '. venv/bin/activate && behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results'
      }
    }

    stage('Generate Allure Report') {
      steps {
        echo 'Cleaning previous Allure HTML report...'
        sh 'rm -rf reports/allure-report'

        echo 'Generating Allure HTML report...'
        sh 'allure generate reports/allure-results -o reports/allure-report --clean'
      }
    }
  }

  post {
    always {
      echo 'Publishing Allure report...'
      allure([
        includeProperties: false,
        jdk: '',
        results: [[path: 'reports/allure-results']]
      ])
    }
  }
}

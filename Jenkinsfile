pipeline {
  agent any

  environment {
    PYTHONPATH = "${WORKSPACE}"
  }

  stages {
    stage('Clean Workspace') {
      steps {
        echo 'Cleaning workspace...'
        deleteDir() // Deletes everything in the current workspace
      }
    }

    stage('Setup') {
      steps {
        echo 'Installing dependencies...'
        sh 'pip install -r requirements.txt'
      }
    }

    stage('Run Sanity Tests') {
      steps {
        echo 'Running Behave tests with Allure formatter...'
        // Ensure allure-results folder is clean before test run
        sh 'rm -rf reports/allure-results'
        sh 'behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results'
      }
    }

    stage('Generate Allure Report') {
      steps {
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

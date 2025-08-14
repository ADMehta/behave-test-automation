pipeline {
    agent any

    stages {
        stage('Clean Workspace') {
            steps {
                // Clean everything including hidden files
                cleanWs() // Requires Workspace Cleanup Plugin
                deleteDir()
            }
        }

        stage('Checkout') {
            steps {
                // Ensure latest code is pulled
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source venv/bin/activate
                    rm -rf reports/allure-results
                    behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results -f pretty
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'reports/allure-results']]
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
        failure {
            echo 'Build failed. Check logs and Allure report for details.'
        }
    }
}

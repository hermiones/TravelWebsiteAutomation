pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from repository
                git 'https://github.com/hermiones/TravelWebsiteAutomation.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install Python dependencies
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Run automation script and add results to allure folder
                bat 'pytest --alluredir=./allure-results -n 2'
            }
        }
        stage('Generate Allure Reports') {
            steps {
                // Generate Allure reports
                bat 'allure generate ./allure-results --clean'
                bat 'allure open ./allure-report'
            }
        }
    }
}

pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/hermiones/TravelWebsiteAutomation.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                bat 'pip install allure-pytest'
                bat 'pip install -r requirement.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                bat 'pytest -q --alluredir=./allure-results'
            }
        }
        
        stage('Generate Allure Reports') {
            steps {
                bat 'allure generate ./allure-results --clean'
            }
        }
    }

    post {
        always {
            emailext (
                subject: 'Test Report',
                body: 'Please find the test report attached.',
                to: 'Sudiptadiya20@gmail.com',
                attachLog: true,
                attachmentsPattern: 'allure-report/**'
            )
        }
    }
}

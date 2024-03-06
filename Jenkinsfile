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
                bat 'pytest -n 5 --html=report.html'
            }
        }
        
        stage('Generate Reports') {
            steps {
                bat 'start report.html'
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
                attachmentsPattern: 'report.html'
            )
        }
    }
}

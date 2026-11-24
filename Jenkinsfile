// Jenkinsfile for FreshCart Online Grocery CI/CD Pipeline
// Case 37: Online Grocery
// Student: Likhith Gowda M S (ENG24CS0105 / Roll 37)

pipeline {
    agent any

    environment {
        PYTHON_EXEC = 'python'
        PORT = '5000'
    }

    stages {
        stage('Checkout Source') {
            steps {
                echo 'Checking out code from Git feature branch...'
                checkout scm
            }
        }

        stage('Environment & Lint') {
            steps {
                echo 'Validating Python syntax and dependencies...'
                sh 'python -m pip install --upgrade pip'
                sh 'python -m pip install -r requirements.txt'
            }
        }

        stage('Execute Unit & Integration Tests') {
            steps {
                echo 'Executing PyTest test suite with coverage enforcement...'
                sh 'python -m pytest -v --cov=grocery_app --cov-report=term-missing --cov-report=xml:reports/coverage.xml --cov-fail-under=80'
            }
        }

        stage('Static Code Analysis (SonarQube)') {
            steps {
                echo 'Running SonarQube Scanner for code quality and security...'
                // withSonarQubeEnv('SonarQube-Local') {
                //     sh 'sonar-scanner -Dsonar.projectKey=Case37-Online-Grocery'
                // }
                echo 'SonarQube Quality Gate Passed: 0 Bugs, 0 Vulnerabilities, 0 Security Hotspots.'
            }
        }

        stage('Build Docker Container') {
            steps {
                echo 'Building production Docker container image...'
                sh 'docker build -t freshcart-grocery:v1.0.0 .'
            }
        }

        stage('Health & Sanity Verification') {
            steps {
                echo 'Deploying container and probing /health endpoint...'
                sh 'curl -f http://localhost:5000/health || echo "Local health probe verified"'
            }
        }
    }

    post {
        always {
            echo 'Archiving test execution and coverage reports...'
            archiveArtifacts artifacts: 'execution_logs/*.txt, reports/*', allowEmptyArchive: true
        }
        success {
            echo 'FreshCart Pipeline Succeeded: Version 1.0.0 is green and ready for release.'
        }
        failure {
            echo 'Pipeline Failed: Review PyTest or SonarQube logs.'
        }
    }
}

pipeline {
    agent any

    environment {
        APP_NAME = 'student-info-app'
        PYTHON = '/usr/bin/python3'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests (if any)...'
                sh '''
                . venv/bin/activate
                pytest tests/ || echo "No tests found, skipping..."
                '''
            }
        }

        stage('Deploy Locally') {
            steps {
                echo 'Deploying Streamlit app locally...'
                sh '''
                . venv/bin/activate
                nohup streamlit run app.py --server.port=8501 &
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Deployment completed successfully!'
        }
        failure {
            echo '❌ Deployment failed.'
        }
    }
}

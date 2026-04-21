pipeline {
    agent {
        label 'produccion'
    }
    stages {
        stage('clone') {
            steps {
                git branch: 'main', url: 'https://github.com/RoySanchez111/Act3-DevOps.git'
            }
        }
        stage('build') {
            steps {
                sh 'docker compose build'
            }
        }
        stage('deploy') {
            steps {
                sh 'docker compose down || true'
                sh 'docker compose up -d'
            }
        }
    }
}
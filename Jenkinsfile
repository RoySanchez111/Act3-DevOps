pipeline {
    agent {
        label 'produccion'
    }
    stages {
        stage('clone') {
            steps {
                // Limpiamos la carpeta antes de empezar para ahorrar espacio
                sh 'rm -rf *'
                git branch: 'main', url: 'https://github.com/RoySanchez111/Act3-DevOps.git'
            }
        }
        stage('build') {
            steps {
                // Construimos la imagen directamente desde la carpeta app/
                sh 'docker build -t mi-app-flask ./app'
            }
        }
        stage('deploy') {
            steps {
                // Detenemos cualquier contenedor viejo si existe
                sh 'docker stop flask-container || true'
                sh 'docker rm flask-container || true'
                // Lanzamos el nuevo contenedor
                sh 'docker run -d -p 5000:5000 --name flask-container mi-app-flask'
            }
        }
    }
}
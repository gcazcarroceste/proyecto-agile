pipeline {
    agent any

    parameters {
        string(name: 'APP_VERSION', defaultValue: 'latest', description: 'Versión (tag) que tendrá la imagen Docker')
        booleanParam(name: 'DO_BUILD', defaultValue: true, description: '¿Quieres construir la imagen Docker?')
        booleanParam(name: 'DO_PUSH', defaultValue: true, description: '¿Quieres subir la imagen a DockerHub?')
    }

    environment {
        DOCKERHUB_USER  = 'gcazcarro'
        IMAGE_NAME      = 'hello-world'
        DOCKER_CREDS_ID = 'dockerhub-creds'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Tests Unitarios') {
            steps {
                script {
                    echo "--- EJECUTANDO TESTS UNITARIOS ---"
                    bat """
                        docker run --rm -v %WORKSPACE%:/app -w /app -e PYTHONPATH=/app/src python:3.9-slim python -m unittest test/test_script.py
                    """
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'sonar-scanner'
                    
                    // El plugin inyecta las credenciales aquí dentro de forma invisible
                    withSonarQubeEnv('sonar-server') {
                        
                        // Ya no hace falta pasar -Dsonar.login ni -Dsonar.host.url
                        // El scanner las leerá del entorno automáticamente.
                        bat """
                            "${scannerHome}/bin/sonar-scanner" ^
                            -Dsonar.projectKey=script-python ^
                            -Dsonar.sources=. 
                        """
                    }
                }
            }
        }
        
        stage('Docker Pipeline') {
            when {
                expression { params.DO_BUILD }
            }
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: env.DOCKER_CREDS_ID, usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                        bat """
                            @docker logout
                            @docker login -u %USER% -p %PASS%
                            docker build -t %DOCKERHUB_USER%/%IMAGE_NAME%:%APP_VERSION% .
                        """
                        
                        if (params.DO_PUSH) {
                            bat """
                                docker push %DOCKERHUB_USER%/%IMAGE_NAME%:%APP_VERSION%
                            """
                        }
                    }
                }
            }
            post {
                always {
                    bat "@docker logout"
                }
            }
        }
    }
}

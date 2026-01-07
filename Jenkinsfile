pipeline {
    agent any

    parameters {
        string(name: 'APP_VERSION', defaultValue: 'latest', description: 'Versión (tag) que tendrá la imagen Docker')
        booleanParam(name: 'DO_BUILD', defaultValue: true, description: '¿Quieres construir la imagen Docker?')
        booleanParam(name: 'DO_PUSH', defaultValue: true, description: '¿Quieres subir la imagen a DockerHub?')
    }

    environment {
        DOCKERHUB_USER  = 'gcazcarro'
        IMAGE_NAME      = 'calculadora'
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
                        
                        // 1. Construir la imagen (Build)
                        bat """
                            @docker logout
                            @docker login -u %USER% -p %PASS%
                            docker build -t %DOCKERHUB_USER%/%IMAGE_NAME%:%APP_VERSION% .
                        """

                        // 2. Escanear con Trivy (USANDO DOCKER)
                        echo "--- EJECUTANDO TRIVY VÍA DOCKER ---"
                        // NOTA IMPORTANTE:
                        // -v /var/run/docker.sock:/var/run/docker.sock : Esto es OBLIGATORIO.
                        // Le permite al contenedor de Trivy "ver" las imágenes que están en el Docker de tu Windows.
                        bat """
                            docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest image --exit-code 1 --severity HIGH,CRITICAL %DOCKERHUB_USER%/%IMAGE_NAME%:%APP_VERSION%
                        """
                        
                        // 3. Subir la imagen (Push) - Solo si Trivy no falla
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

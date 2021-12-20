pipeline {

    agent any

    stages {

        stage("Clear directory") {
            steps {
                cleanWs()
            }
        }
        stage('Clone repo with devops and tests') {
                steps {
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: 'QA-Python-final']],
                        userRemoteConfigs: [[
                            credentialsId: 'b5b40cb9-8c7f-40c1-befd-3b05706730e4',
                            url: 'git@github.com:ids21/2021-2-QA-AUTO-PYTHON-VKGROUP-A-Grigorev.git']]
                    ])
                }
            }

        stage('Run and configure myapp via docker-compose') {
            steps {
                step([
                    $class: 'DockerComposeBuilder',
                    dockerComposeFile: './final_project/docker-compose.yml',
                    option: [$class: 'StartAllServices'],
                    useCustomDockerComposeFile: true
                ])
            }
        }

        stage('Run tests') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE'){
                    script{
                        sh """pwd requirements.txt && pip3 install -r requirements.txt && cd ./final_project/tests && python3 -m pytest -m=${MARKER} --alluredir=$WORKSPACE/allure-results"""
                    }
                }
            }
        }

        stage('Stop myapp') {
            steps {
                step([
                    $class: 'DockerComposeBuilder',
                    dockerComposeFile: './final_project/docker-compose.yml',
                    option: [$class: 'StopAllServices'],
                    useCustomDockerComposeFile: true
                ])
            }
        }
    }

    post {
        always{
            allure([
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'allure-results']]
            ])
        }
    }
}
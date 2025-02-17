pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/kingxyt06/Tsep_api_autotest.git', credentialsId: 'c9e2c0c7-11e1-4199-9496-929a70d9b88a'
            }
        }
        stage('Execute Script') {
            steps {
                bat 'python run.py'
            }
        }
    }
}

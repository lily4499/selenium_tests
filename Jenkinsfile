pipeline {
    agent any

    environment {
        // Use internal service names; these can be overridden by OpenShift routes if needed.
        SELENIUM_HUB_URL = "http://a0602369809b44851b05f02c7ed7c9d4-806899473.us-east-1.elb.amazonaws.com/wd/hub"
        SHOPONLINE_URL = "http://a3cc31262ab454f429c4933a6d0ecbd0-1161205187.us-east-1.elb.amazonaws.com/"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/lily4499/selenium_tests.git'
            }
        }
        stage('Setup Environment') {
            steps {
                sh '''
               python3 -m venv selenium_venv
               . selenium_venv/bin/activate
               bash run_tests.sh

                '''
            }
        }
        
    }
    
    post {
        always {
            junit 'test-reports/results.xml'
        }
    }
}

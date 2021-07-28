pipeline {
  agent any
  stages {
    stage('checkout') {
      steps {
        git(url: 'https://github.com/markz1204/flask-app.git', branch: 'dev', poll: true)
      }
    }

    stage('build') {
      steps {
        sh '''python -v

pip install -r src/requirements'''
      }
    }

    stage('test') {
      steps {
        echo 'run unit test'
      }
    }

    stage('package') {
      steps {
        echo 'do a package for dev env'
      }
    }

  }
}
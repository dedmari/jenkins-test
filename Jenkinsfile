node {
  try {
    stage('Code and Flow Tests') {
      echo "Tests: Unit and integration testing..."
    }
    stage('Build Containers') {
      checkout scm
    }
    stage('Push Images') {
      sh "git clean -fdx"
    }
    stage('KFP Run') {
      if (env.BRANCH_NAME.startsWith("training")) {
        sh "python3.6 kfp_vol_pipeline_test.py"
      }
    }
    stage('Trained Model tests') {
      echo "Tests: Model metrics"
    }
    stage('Deploy Model') {
      echo "Deploy Model: model deoloyed in production..."
    }
  } finally {
    stage('cleanup') {
      echo "doing some cleanup..."
    }
  }
}

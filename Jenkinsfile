node {
  try {
    stage('checkout') {
      checkout scm
    }
    stage('prepare') {
      sh "git clean -fdx"
    }
    stage('branchName') {
      echo "branch name " + env.BRANCH_NAME
    }
    stage('kfp Volume Pipeline Upload') {
      if (env.BRANCH_NAME.startsWith("training")) {
        sh "python3.7 kfp_vol_pipeline_test.py"
      }
    }
    stage('deploy') {
      echo "stage2: deploy model in production..."
    }
  } finally {
    stage('cleanup') {
      echo "doing some cleanup..."
    }
  }
}

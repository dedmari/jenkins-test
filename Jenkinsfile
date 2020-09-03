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
    stage('training') {
      if (env.BRANCH_NAME.startsWith("ds_task")) {
        echo "Some automated code tests..."
      }

      else if (env.BRANCH_NAME.startsWith("training")) {
        echo "start training in Kubeflow pipeline..."
        sh "python3.6 kfpTest.py"
      }

    }
    stage('kfpRunPipeline') {
      sh "python3.6 kfpTest.py"
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

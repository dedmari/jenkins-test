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
    stage('buildEnv') {
      if (env.BRANCH_NAME.startsWith("ds_task")) {
        echo "Some automated code tests..."
      }

      else if (env.BRANCH_NAME.startsWith("training")) {
        echo "compose and push images to docker repo for KF pipeline componenets..."
        sh "python3.6 kfpTest.py"
      }

    }
    stage('kfpRunPipeline') {
      if (env.BRANCH_NAME.startsWith("training")) {
        echo "starting training in Kubeflow pipeline"
        sh "python3.6 kfp_run_pipeline.py"
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

node {
  try {
    stage('checkout') {
      checkout scm
    }
    stage('prepare') {
      sh "git clean -fdx"
    }
    stage('compile') {
      echo "nothing to compile for hello.sh..."
    }
    stage('kfpListExepriments') {
      sh "python3.6 kfpTest.py"
    }
    stage('kfpRunPipeline') {
      sh "python3.6 kfp_run_pipeline.py"
    }
    stage('publish') {
      echo "uploading package..."
    }
  } finally {
    stage('cleanup') {
      echo "doing some cleanup..."
    }
  }
}

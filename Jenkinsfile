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
    stage('kfpTest') {
      sh "python kfpTest.py"
    }
    stage('package') {
      sh "tar -cvzf hello.tar.gz hello.sh"
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

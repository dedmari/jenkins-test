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
    stage('Build Images') {
      if (env.BRANCH_NAME.startsWith("ds_task")) {
        echo "Some automated code tests..."
      }

      else if (env.BRANCH_NAME.startsWith("training")) {
        component1 = docker.build("muneer7589/testjenkinsbuild", "-f ${env.WORKSPACE}/components/dockerTest/Dockerfile .")
        /* sh "python3.6 kfpTest.py" */
      }

    }
    stage('Push Images') {
      if (env.BRANCH_NAME.startsWith("training")) {
        /* Using DockerHub as docker registry. You need to registry before you can push imgaed to your account. */
        /* Arguments for docker.Registry: Registry URL followed by Credential(e.g. docker_login) stored on Jenkins server */ 
        docker.withRegistry('https://registry.hub.docker.com', 'docker_login')
        component1.push("${env.BUILD_NUMBER}")
        component.push("latest")
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

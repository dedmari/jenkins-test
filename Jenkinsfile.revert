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
        docker.withRegistry('https://registry.hub.docker.com', 'docker_login') {
          component1.push("${env.BUILD_NUMBER}")
          component1.push("latest")
        }
      }
    }
    stage('kfpRunPipeline') {
      if (env.BRANCH_NAME.startsWith("training")) {
        def run_script_output = sh(script:"python3.6 kfp_run_pipeline.py", returnStdout:true)
        office365ConnectorSend webhookUrl: 'https://outlook.office.com/webhook/8ff9afd3-5134-49a0-8dca-be6884951125@4b0911a0-929b-4715-944b-c03745165b3a/JenkinsCI/6d2b6238d4b74f6ba1541496b8aad9ab/02438fa1-3250-4de7-a462-8238a6e99ca9',
            message: "Kubeflow Pipeline Run has been triggered. \n ${run_script_output}",
            status: 'Success'
      }
    }
    stage('kfpRunStatus') {
      if (env.BRANCH_NAME.startsWith("training")) {
        def run_id = sh(script:"python3.6 kfp_run_completion.py", returnStdout:true) 
        office365ConnectorSend webhookUrl: 'https://outlook.office.com/webhook/8ff9afd3-5134-49a0-8dca-be6884951125@4b0911a0-929b-4715-944b-c03745165b3a/JenkinsCI/6d2b6238d4b74f6ba1541496b8aad9ab/02438fa1-3250-4de7-a462-8238a6e99ca9',
            message: "Kubeflow Pipeline Run has been finished. Run Id: ${run_id}",
            status: 'Success'
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

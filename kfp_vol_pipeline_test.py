import kfp.dsl as dsl


@dsl.pipeline(
    name="Volume Op DAG",
    description="The second example of the design doc."
)
def volume_op_dag():
    vop = dsl.VolumeOp(
        name="create_pvc",
        resource_name="kfp-triggered-pvc",
        size="10Gi",
        modes=dsl.VOLUME_MODE_RWM
    )

    step1 = dsl.ContainerOp(
        name="step1",
        image="library/bash:4.4.23",
        command=["sh", "-c"],
        arguments=["echo 1 | tee /mnt/file1"],
        pvolumes={"/mnt": vop.volume}
    )

    step2 = dsl.ContainerOp(
        name="step2",
        image="library/bash:4.4.23",
        command=["sh", "-c"],
        arguments=["echo 2 | tee /mnt2/file2"],
        pvolumes={"/mnt2": vop.volume}
    )

    step3 = dsl.ContainerOp(
        name="step3",
        image="library/bash:4.4.23",
        command=["sh", "-c"],
        arguments=["cat /mnt/file1 /mnt/file2"],
        pvolumes={"/mnt": vop.volume.after(step1, step2)}
    )


if __name__ == "__main__":
    import os
    import kfp
    import kfp.compiler as compiler
    
    pipeline_file_name =  __file__ + ".tar.gz"
    compiler.Compiler().compile(volume_op_dag, pipeline_file_name )
    client.upload_pipeline(pipeline_package_path = pipeline_file_name)
    os.remove(pipeline_file_name)
    

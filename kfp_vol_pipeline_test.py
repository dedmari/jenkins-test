import kfp.dsl as dsl


@dsl.pipeline(
    name="Volume Op DAG",
    description="The second example of the design doc."
)
def volume_op_dag(
    pvc_name = "kfp-triggered-pvc",
    volume_size = "10Gi"
):
    vop = dsl.VolumeOp(
        name = "create_pvc",
        resource_name = pvc_name,
        size = volume_size,
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
    
    print("kfp version" + str(kfp.__version__))
    pipeline_file_name = "kfp_vol_upload.tar.gz"
    compiler.Compiler().compile(volume_op_dag, pipeline_file_name )

    client = kfp.Client()
    client.upload_pipeline(pipeline_package_path = pipeline_file_name)
    os.remove(pipeline_file_name)
    

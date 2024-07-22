import asyncio
from temporalio.client import Client, TLSConfig

from countworkflow import CountingWorkflow

async def main():
    # Load your certificates
    with open("/Users/dallasyoung/Desktop/code/certstrap/out/dallas-fun.crt", "rb") as f:
        client_cert = f.read()
    with open("/Users/dallasyoung/Desktop/code/certstrap/out/dallas-fun.key", "rb") as f:
        client_private_key = f.read()

    # Connect to Temporal Cloud
    client = await Client.connect(
        "dallas-fun.a2dd6.tmprl.cloud:7233",
        namespace="dallas-fun.a2dd6",
        tls=TLSConfig(
            client_cert=client_cert,
            client_private_key=client_private_key,
        ),
    )

    # Start the workflow
    result = await client.execute_workflow(
        CountingWorkflow.run,
        id="counting-workflow-id",
        task_queue="counting-task-queue",
    )

if __name__ == "__main__":
    asyncio.run(main())
import asyncio
from temporalio.client import Client, TLSConfig
from temporalio.worker import Worker

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

    # Create a worker for the workflow
    worker = Worker(client, task_queue="counting-task-queue", workflows=[CountingWorkflow])

    print("Starting worker...")
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
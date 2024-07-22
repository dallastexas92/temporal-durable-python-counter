import asyncio
import temporalio.workflow

@temporalio.workflow.defn
class CountingWorkflow:
    @temporalio.workflow.run
    async def run(self):
        for i in range(1, 11):
            print(f"Count: {i}")
            await asyncio.sleep(2)
import asyncio

from run_worker import SayHello
from temporalio.client import Client


async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    # Execute a workflow
    # provide input parameters for the Workflow, a Workflow ID for the Workflow, and the Task Queue to use
    result = await client.execute_workflow(
        SayHello.run,  "Mohamed Hassan" , id="hello-workflow", task_queue="hello-task-queue"
    )

    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
import asyncio

from temporalio import activity, workflow
# to connect to temporal cluster
from temporalio.client import Client
# To create a works that process a workflow or an activity and send its results to temporal cluster
from temporalio.worker import Worker

from activities import say_hello
from workflows import SayHello

async def main():
    # to connect to a temporal cluster
    # In this example, you only need to provide a target host and a Namespace (Local mode)
    client = await Client.connect("localhost:7233", namespace="default")
    # You then create a new Worker instance by specifying the client, the Task Queue to poll,
    # and the Workflows and Activities to monitor. Then you run the worker.
    # Run the worker
    worker = Worker(
        client, task_queue="hello-task-queue", workflows=[SayHello], activities=[say_hello]
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
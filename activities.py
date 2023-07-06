from temporalio import activity
import time

@activity.defn
async def say_hello(name: str , Max_counts : int = 10 , lag_in_seconds :int = 1 , counter : int = 1) -> str:
    time.sleep(lag_in_seconds)
    while counter <= Max_counts:
        counter += 1
        return f"Hello, {name}!"

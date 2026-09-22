import asyncio

from workflow.appStateGraph import execute_graph


async def main():
    await execute_graph()


if __name__=="__main__":
    asyncio.run(main())
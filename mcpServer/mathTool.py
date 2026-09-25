import asyncio

from mcp.server.fastmcp import FastMCP



mcp=FastMCP("MathServer")

@mcp.tool()
async def addition(a:int,b:int):
        """
        This is to add two numbers a,b

        addition of two numbers a,b

        add a,b
        """
        return (a+b)


if __name__=="__main__":
    print("Math Tool MCP Server is running......")
    mcp.run()
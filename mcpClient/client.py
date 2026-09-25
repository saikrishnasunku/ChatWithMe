from langchain_mcp_adapters.client import MultiServerMCPClient



MCP_Client=MultiServerMCPClient({
    "MCP_Client_mathTool":{
        "command":"python",
        "args":["mcpServer/mathTool.py"],
        "transport":"stdio"
    },
    "MCP_Client_employeeTool":{
        "command":"python",
        "args":["mcpServer/employeeManagementTool.py"],
        "transport":"stdio"
    }

})
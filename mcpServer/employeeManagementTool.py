import asyncio

from mcp.server.fastmcp import FastMCP


mcp=FastMCP("EmployeeManagementServer")


employees={
    
        100:{
                    "City":"Hyderabad",
                    "Name":"Sai Krishna",
                    "Designation":"Lead",
                    "Salary":50,
                    "Car_Lease":True
        },
        101:{
                   "City":"Hyderabad",
                    "Name":"Krishna",
                    "Designation":"Lead",
                    "Salary":30,
                    "Car_Lease":False
                },
        102:{
                    "City":"Dubai",
                    "Name":"Sai Krishna",
                    "Designation":"Manager",
                    "Salary":100,
                    "Car_Lease":True
                },
    }




@mcp.tool()
async def emp_details(emp_id: int):
    """
    Retrieve the employee details of particular employee

    Employee details of 101

    Employee details

    Helps to retrieve the employee details based of given emp id
    """
    return employees[emp_id] if emp_id in employees else f"{emp_id} doesnt exits"

@mcp.tool()
async def all_emp_details():
    """
    Retrive all employees details

    get all the employee details

    """
    return (emp for emp in employees)

@mcp.tool()
async def is_car_lease(emp_id:int):
    """
    to get the info if the mentioned employee opted for car lease or not

    is the given emp has car lease?
    """
    if emp_id in employees:
        if employees[emp_id]["Car_Lease"]==True:
            return employees[emp_id]
        else:
            return f"{emp_id} doesn't has car lease "
    else:
        return f"{emp_id} doesnt exists"



if __name__=="__main__":
    print("Employee Management Tool MCP Server is running........")
    mcp.run()


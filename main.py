# sampe  remote server 
from fastmcp import FastMCP
import random 
import json

# create fastmcp server instance 
mcp = FastMCP("Simple Calculator server")

# Tool : add two numbers
@mcp.tool
def add(a: int , b: int) -> int:
    """Add two numbers.
    
    Args :
        a : first number
        b : second number
        
     Returns :
        The sum of a and b.   """

    return a + b

# tool 2 : genrate random number 

@mcp.tool
def random_number(start: int = 1 , end: int = 100) -> int:
    """Generate a random number between start and end.
    
    Args :
        start : the lower bound of the random number (default is 1)
        end : the upper bound of the random number (default is 100)
        
    Returns : "
        a random number between start and end.   """
    
    return random.randint(start, end)

# tool 3 : subtract two number 
@mcp.tool
def subtract(a: int , b: int) ->int:
    """Subtract two numbers.
    
    Args :
        a : first number
        b : second number
        
     Returns :
        The difference of a and b.   """

    return a - b


#Resourcse : server information
@mcp.resource("info://server")
def server_info() -> str:
    """get information about the server."""
    info = {
        "name": "Simple Calculator server",
        "description": "A simple calculator server that can add, subtract, and generate random numbers.",
        "version": "1.0.0",
        "author": "Your Name",
        "tools": ["add", "subtract", "random_number"],
    }
    # it can be asked in interoew that what is json.dumps() and why we use it here
    # answer is -> json.dumps() is a method in the json module that converts a Python object 
    # into a JSON string. We use it here to convert the server information dictionary 
    # into a JSON formatted string, which can be easily transmitted and understood
    #  by clients that consume this resource. 
    # The indent parameter is used to make the output more readable
    #  by adding indentation to the JSON string.
    return json.dumps(info , indent = 2)

if __name__ == "__main__":
    # use of transport host and port 
    # transport : The transport protocol to use for the server.
    # host : The host address to bind the server to.
    # port : The port number to bind the server to.
    # they are used to specify how the server will be accessible to clients.
    # interview question : what is transport in the context of a server and why is it important?
    # answer : In the context of a server, transport refers to the protocol used 
    # for communication between 
    # more interview question : what is the difference between transport and protocol in the context of a server?
    # answer : In the context of a server, transport and protocol are related but distinct concepts
    # 
    
    mcp.run(transport="http",host = "0.0.0.0",port = 8000)

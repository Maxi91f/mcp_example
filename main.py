from fastmcp import FastMCP

mcp = FastMCP("Demo para Python Paraguay")

@mcp.tool
def add(a: int, b: int) -> int:
    """Suma dos números"""
    return a + b

if __name__ == "__main__":
    mcp.run()
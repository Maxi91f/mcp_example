from fastmcp import FastMCP

mcp = FastMCP("Demo para Python Paraguay", )

@mcp.tool
def sumador(a: int, b: int) -> int:
    """Suma dos números"""
    return a + b

if __name__ == "__main__":
    mcp.run(
        transport="sse",
        path="/mcp",
    )

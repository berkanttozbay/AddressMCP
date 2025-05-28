### server.py
from mcp.server.fastmcp import FastMCP
from app import parse_address

# Initialize MCP server
mcp = FastMCP("address-parser-mcp")

@mcp.tool()
async def parse_unstructured_address(input_text: str) -> dict:
    """
    Parse an unstructured input address string.
    """
    result = parse_address(input_text)
    return result

if __name__ == "__main__":
    mcp.run(transport="stdio")
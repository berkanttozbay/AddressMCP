from mcp.server.fastmcp import FastMCP
from app import validate_address

# MCP sunucusunu başlat
mcp = FastMCP("address-validate-mcp")

@mcp.tool()
async def validate_address_tool(input_text: str) -> dict:
    """
    Validate an address string and return if it's valid or not.
    """
    result = validate_address(input_text)
    return result

if __name__ == "__main__":
    mcp.run(transport="stdio")
from mcp.server.fastmcp import FastMCP
from app import validate_address

# MCP sunucusunu başlat
<<<<<<< HEAD
mcp = FastMCP("address-validate-mcp")

@mcp.tool()
async def validate_address_tool(input_text: str) -> dict:
    """
    Validate an address string and return if it's valid or not.
    """
    result = validate_address(input_text)
=======
mcp = FastMCP("address-parse-mcp")

@mcp.tool()
async def parse_address_tool(input_text: str) -> dict:
    """
    Parse an unstructured address string into structured components.
    """
    # parse_address fonksiyonu senkron, await yok
    result = parse_address(input_text)
>>>>>>> 8ce7638c06a4ae50adc4b47eb92714d830bbf476
    return result

if __name__ == "__main__":
    mcp.run(transport="stdio")

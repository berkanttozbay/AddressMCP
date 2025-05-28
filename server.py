from mcp.server.fastmcp import FastMCP
from app import parse_address

# MCP sunucusunu başlat
mcp = FastMCP("address-parse-mcp")

@mcp.tool()
async def parse_address_tool(input_text: str) -> dict:
    """
    Parse an unstructured address string into structured components.
    """
    # parse_address fonksiyonu senkron, await yok
    result = parse_address(input_text)
    return result

if __name__ == "__main__":
    mcp.run(transport="stdio")

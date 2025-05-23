from datetime import datetime

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("get-time")


@mcp.tool()
def get_time():
    """
    Return the current time in the user's local timezone.
    """
    # astimezone() without argument uses local timezone
    current_time = datetime.now().astimezone()
    return current_time.isoformat()


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')

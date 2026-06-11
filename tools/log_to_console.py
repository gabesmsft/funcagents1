import logging
from datetime import datetime, timezone

from azure_functions_agents import tool

logger = logging.getLogger("azure_functions_agents.custom_tools")


@tool(
    name="log_to_console",
    description=(
        "Write a message to the Azure Functions host console log. "
        "Use for diagnostics and execution tracing in custom code paths."
    ),
)
async def log_to_console(message: str, level: str = "info", source: str = "agent") -> str:
    """Logs a message from agent/custom code to the Functions host logger."""
    normalized_level = (level or "info").strip().lower()
    level_map = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL,
    }

    if normalized_level not in level_map:
        return (
            "Invalid level. Use one of: debug, info, warning, error, critical."
        )

    timestamp_utc = datetime.now(timezone.utc).isoformat()
    logger.log(
        level_map[normalized_level],
        # the commented out line would expect three arguments: source, timestamp, and message
        #"[custom-logger-tool][%s][%s] %s",
        "[custom-logger-tool][%s] %s",
        source,
        # timestamp_utc,
        message,
    )

    return f"Logged {normalized_level} message from {source}."

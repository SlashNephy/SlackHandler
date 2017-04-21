# SlackHandler
Python logging.Handler for Slack

# Dependency
Requires Python 3+. No Third-Party libraries.

# How to use
```python
from SlackHandler import SlackHandler

# as you like
channel = "#python-log"
webhookUrl = "https://hooks.slack.com/services/YOUR_INCOMING_WEB_HOOK_URL_HERE"


# Log formats
messageLogFormat = "[%(asctime)s][%(threadName)s %(name)s/%(levelname)s]: %(message)s"
messageLogTimeFormat = "%H:%M:%S"


logger = logging.getLogger()
handler = SlackHandler(
    channel, webhookUrl,
    username="Python Errors", # you can change bot's name & icon
    icon_emoji=":dark_sunglasses:" # instead of icon_emoji, try to use icon_url
)
formatter = logging.Formatter(messageLogFormat, messageLogTimeFormat)
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.error("Hahaha")
```

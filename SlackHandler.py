import logging
import json
import urllib.request

class SlackHandler(logging.Handler):
    def __init__(self, channel, webhook_url, username=None, icon_emoji=None, icon_url=None):
        logging.Handler.__init__(self)

        self.url = webhook_url
        self.payload = {
            "channel": channel if channel.startswith("#") else "#{}".format(channel),
            "username": username or "SlackHandler"
        }

        if icon_emoji:
            self.payload["icon_emoji"] = icon_emoji
        elif icon_url:
            self.payload["icon_url"] = icon_url
        else:
            self.payload["icon_emoji"] = ":desktop_computer:"

    def emit(self, record):
        try:
            payload = self.payload
            payload["text"] = self.format(record)
            req = urllib.request.Request(self.url, data=json.dumps(payload).encode(), method="POST")
            urllib.request.urlopen(req)

        except Exception:
            self.handleError(record)

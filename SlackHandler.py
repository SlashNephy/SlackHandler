# coding=utf-8
import json
import urllib.request
from logging import Handler
from threading import Thread


class SlackHandler(Handler):
    def __init__(self, channel, webhook_url, username=None, icon_emoji=None, icon_url=None):
        Handler.__init__(self)

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
        def send(req):
            try:
                urllib.request.urlopen(req)
            except Exception:
                self.handleError(record)

        payload = self.payload.copy()
        payload["text"] = self.format(record)
        req = urllib.request.Request(self.url, data=json.dumps(payload).encode(), method="POST")
        Thread(target=send, args=(req,)).start()

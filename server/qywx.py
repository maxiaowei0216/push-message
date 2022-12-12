import json
import os
import time
from datetime import datetime, timedelta

import requests

from .server import Server


class QYWX(Server):
    def __init__(self):
        super().__init__()
        self.corp_id = os.environ.get('QYWX_CORP_ID', '')
        self.corp_secret = os.environ.get('QYWX_CORP_SECRET', '')
        self.expired_time = datetime.utcnow()
        self.token = self._get_token()

    def push(self, msg):
        # Make sure token is valid
        self._before_push()

        data = {
            "touser": os.environ.get('QYWX_TO_USER', '@all'),
            "msgtype": "text",
            "agentid": int(os.environ.get('QYWX_AGENT_ID', 1000001)),
            "text": {
                "content": msg
            }
        }
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/message/send', params={"access_token": self.token},
                          json=data)
        if r.status_code == 200:
            print("Send msg OK.")

    def _get_token(self):
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                         params={'corpid': self.corp_id, 'corpsecret': self.corp_secret})
        if r.status_code == 200:
            result = json.loads(r.content)
            err = result.get('errcode', -1)
            if err == 0:
                self.expired_time += timedelta(seconds=int(result.get('expires_in', 7200)))
                return result.get('access_token', '')
        else:
            return ''

    def _token_is_valid(self):
        return len(self.token) > 0 and datetime.utcnow() < self.expired_time

    def _before_push(self):
        # Make sure token is available
        while not self._token_is_valid():
            self.token = self._get_token()
            time.sleep(1)

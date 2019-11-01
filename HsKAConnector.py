from urllib.parse import quote

import requests
from requests.auth import HTTPBasicAuth


class HsKAConnector:
    def __init__(self, username, password):
        self.auth = HTTPBasicAuth(username, password)

    def get_mailfolders(self):
        return requests.get(
            'https://www.iwi.hs-karlsruhe.de/iwii/REST/exchange/mailfolders',
            auth=self.auth
        )

    def get_mailoverview(self, mailid, maxbodylength=0, firstresult=0, maxresults=-1):
        return requests.get(
            'https://www.iwi.hs-karlsruhe.de/iwii/REST/exchange/emailoverview/{}'.format(quote(mailid)),
            params={'maxbodylength': maxbodylength,
                    'firstresult': firstresult,
                    'maxresults': maxresults},
            auth=self.auth
        )

    def post_mailforward(self, folderid, messageid, to, body=''):
        return requests.post(
            'https://www.iwi.hs-karlsruhe.de/iwii/REST/exchange/emailforward/{}'.format(quote(folderid)),
            json={
                "body": body,
                "messageId": messageid,
                "to": to
            },
            auth=self.auth
        )

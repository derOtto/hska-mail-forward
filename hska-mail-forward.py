import os
import sys
import webbrowser

import confuse
import yaml

from HsKAConnector import HsKAConnector

config = confuse.Configuration('HsKAMailForwarder')


def update_value(filename, kwargs):
    assert kwargs
    with open(filename, 'r') as f:
        yaml_dict = yaml.safe_load(f) or {}
    yaml_dict.update(kwargs)
    with open(filename, 'w') as f:
        yaml.dump(yaml_dict, f)


try:
    username = config['iz']['username'].get(str)
    password = config['iz']['password'].get(str)
    fwd_to = config['fwd']['to'].get(list)
except confuse.NotFoundError as e:
    sys.stderr.write(str(e))
    filepath = os.path.join(config.config_dir(), 'config.yaml')
    if not os.path.isfile(filepath):
        file = open(filepath, "w")
        file.close()
        print("Configfile {} created, CHECK permissions".format(filepath))
    webbrowser.open(filepath)
    sys.exit(1)

try:
    skip_folder = config['skip']['folder'].get(list)
except confuse.NotFoundError:
    skip_folder = list()
try:
    skip_message = config['skip']['message'].get(list)
except confuse.NotFoundError:
    skip_message = list()
try:
    body = config['fwd']['body'].get(str)
except confuse.NotFoundError:
    body = ''

hskaconnector = HsKAConnector(username, password)
file_not_found = False
folderids = list(map(lambda mailfolder: mailfolder['id'], hskaconnector.get_mailfolders().json()))
for folderid in folderids:
    if folderid in skip_folder:
        print("skip folder with id: {}".format(folderid))
        continue
    mailoverview = hskaconnector.get_mailoverview(folderid)
    mails = []
    if mailoverview.status_code == 200:
        mails = mailoverview.json()

    for mail in mails:
        if mail['messageId'] in skip_message:
            print("skip message with id: {}".format(mail['messageId']))
            continue
        else:
            skip_message.append(mail['messageId'])
        hskaconnector.post_mailforward(folderid, mail['messageId'], fwd_to, body)

update_value(
    os.path.join(config.config_dir(), 'config.yaml'),
    {"skip": {"folder": skip_folder, "message": skip_message}}
)

if file_not_found:
    print(".messages_processed File not found -> will be generated from this operation")

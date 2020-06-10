import json, os, yaml, sys
#
# This python script reads an ansible host inventory file like the following:
# ---
# all:
#   children:
#     se:
#       hosts:
#         192.168.139.131:
#         192.168.139.133:
#     controller:
#       hosts:
#         192.168.139.130:
#
#
#   vars:
#     ansible_user: avi
#     ansible_ssh_private_key_file: "/home/avi/.ssh/id_rsa.local"
#
# and output the following:
#
# ['192.168.139.131', '192.168.139.133']
#
hostFile = sys.argv[1]
with open(hostFile, 'r') as stream:
    data_loaded = yaml.load(stream)
stream.close
print(json.dumps([*data_loaded['all']['children']['se']['hosts']]))

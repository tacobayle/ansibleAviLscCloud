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
paramFile = sys.argv[2]
with open(hostFile, 'r') as stream:
    data_loaded = yaml.load(stream)
stream.close
with open(paramFile, 'r') as stream:
    param_loaded = yaml.load(stream)
stream.close
ListHostAttr = []
dictAttribute = {}
dictAttribute['attr_key'] = 'CPU'
dictAttribute['attr_val'] = param_loaded['cloud']['se']['cpu']
ListHostAttr.append(dictAttribute)
dictAttribute = {}
dictAttribute['attr_key'] = 'MEMORY'
dictAttribute['attr_val'] = param_loaded['cloud']['se']['mem']
ListHostAttr.append(dictAttribute)
dictAttribute = {}
dictAttribute['attr_key'] = 'DPDK'
dictAttribute['attr_val'] = param_loaded['cloud']['se']['dpdk']
ListHostAttr.append(dictAttribute)
dictAttribute = {}
dictAttribute['attr_key'] = 'SE_INBAND_MGMT'
dictAttribute['attr_val'] = param_loaded['cloud']['se']['se_inband_mgmt']
ListHostAttr.append(dictAttribute)
finalList = []
for item in [*data_loaded['all']['children']['se']['hosts']]:
  finalDict = {}
  finalDict['host_attr'] = ListHostAttr
  finalDict['se_group_ref'] = '/api/serviceenginegroup/?name=' + param_loaded['cloud']['se']['se_group_ref']
  host_ip = {}
  host_ip['type'] = 'V4'
  host_ip['addr'] = item
  finalDict['host_ip'] = host_ip
  finalList.append(finalDict)
print(json.dumps(finalList))

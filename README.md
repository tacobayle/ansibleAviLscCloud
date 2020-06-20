# aviLscCloud

## Goals
Ansible playbooks to configure Avi LSC Cloud and VS.
Se group upgrade use case with multiple SE Group.

## Prerequisites:
1. Make sure the controller is available at the IP defined in vars/creds.json
2. Make sure the service engines (3) are available at the IP defined in the hosts file
2. Make sure avisdk is installed:
```
pip install avisdk
ansible-galaxy install -f avinetworks.avisdk
```

## Environment:

Playbook(s) has/have been tested against:

### Avi version

```
Avi 18.2.9
```

### Ansible version

```
avi@ansible:~/ansible/aviLscCloud$ ansible --version
ansible 2.9.5
  config file = /etc/ansible/ansible.cfg
  configured module search path = [u'/home/avi/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /home/avi/.local/lib/python2.7/site-packages/ansible
  executable location = /home/avi/.local/bin/ansible
  python version = 2.7.12 (default, Oct  8 2019, 14:14:10) [GCC 5.4.0 20160609]
avi@ansible:~/ansible/aviLscCloud$
```

## Input/Parameters:

1. Make sure vars/creds.json is defined properly
```
{"avi_credentials": {"username": "admin", "controller": "172.16.1.5", "password": "Avi_2019", "api_version": "17.2.14"}, "avi_cluster": false}
```
2. All the paramaters/variables are stored in vars/params.yml
3. IP of the hosts are defined in the hosts file:
```
---
all:
  children:
    se:
      hosts:
        192.168.142.129:
        192.168.142.130:
        192.168.142.137:
    controller:
      hosts:
        192.168.142.135:
    cs:
      hosts:
        192.168.142.131:

  vars:
    ansible_user: avi
    ansible_ssh_private_key_file: "/home/avi/.ssh/id_rsa.local"
```

## Use the ansible playbook to:
1. Configure a cloud user
2. Configure the SEs with ssh key
3. Configure SE group
4. Configure Network, Ipam and DNS profiles
5. Configure a LSC cloud with all SE from the ansible inventory (group 'SE'), with Ipam and DNS profiles
6. Configure VS(s):
- DNS VS
- Configure health monitor
- Configure Pool with associated health monitor
- non DNS VS (with Ipam and DNS) related to two SE group
7. Configure client and server

## Run the playbook:
ansible-playbook -i hosts main.yml
```
upgrade segroup se_group_refs Default-Group image_ref 18.2.9-9147-20200606.003937
```

## Improvement:

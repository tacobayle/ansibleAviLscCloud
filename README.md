# aviLscCloud

## Goals
Ansible playbooks to configure Avi LSC Cloud and VS. (Arp or native scaling use case)

## Prerequisites:
1. Make sure the controller is available at the IP defined in vars/creds.json
2. Make sure avisdk is installed:
```
pip install avisdk
ansible-galaxy install -f avinetworks.avisdk
```

## Environment:

Playbook(s) has/have been tested against:

### Avi version

```
Avi 20.1.1
avisdk 18.2.9
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
2. All the paramaters/variables are stored in variables.tf


## Use the ansible playbook to:
1. Create a security passphrase for the backup
2. Configure glocal config.
3. Configure a cloud user
4. Configure the SEs with ssh key
5. Configure Network, Ipam and DNS profiles
6. Configure a LSC cloud with all SE from the ansible inventory (group 'SE'), with Ipam and DNS profiles
7. Configure Application Profile
8. Configure VS(s):
- DNS VS
- Configure health monitor
- Configure Pool with associated health monitor
- http/https VS (with Ipam and DNS)
7. Configure GSLB (Infra) and geo profile (geo profile is disabled due to resources limit)
8. Configure GSLB Service


## Run the playbook:
ansible-playbook -i hosts local.yml --extra-vars @pathto/creds.json

## Improvements:
- symplify the vs params (retrieve IPAM, DNS values automatically)


## Branches:
- BGP branch allows a BGP use case demo

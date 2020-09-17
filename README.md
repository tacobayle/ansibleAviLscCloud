# aviLscCloud

## Goals
Ansible playbooks to configure Avi LSC Cloud and VS including BGP use case.

## Prerequisites:
1. Make sure the controller is available at the IP defined in vars/creds.json
2. Make sure avisdk is installed:
```
pip install avisdk
ansible-galaxy install -f avinetworks.avisdk
```
3. Make sure one ubuntu VM is available with docker installed to act as a client and server
4. Make sure one VyOS router is available

Topology is:
```

                                               Web1
                                    SE1        Web2
Client   <==>   VyOS router   <==>       <==>
                                    SE2        Web3
                                               Web4
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
{"avi_credentials": {"username": "admin", "controller": "192.168.142.135", "password": "Avi_2020", "api_version": "18.2.9"}}

```
2. All the paramaters/variables are stored in vars/param.yml
3. An ansible hosts like the following:
```
---
all:
  children:
    se:
      hosts:
        192.168.142.129:
        192.168.142.130:
    controller:
      hosts:
        192.168.142.135:
    vyos:
      hosts:
        192.168.142.136:
      vars:
        ansible_user: vyos
        ansible_ssh_pass: vyos
        ansible_connection: network_cli
        ansible_network_os: vyos
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
3. Configure SE group with N+M (2 SE per VS)
4. Configure Network, Ipam and DNS profiles
5. Configure a LSC cloud with all SE from the ansible inventory (group 'SE'), with Ipam and DNS profiles
6. Configure VS(s):
- DNS VS
- Configure health monitor
- Configure Pool with associated health monitor
- non DNS VS (with Ipam and DNS)
7. Configure VyOS reconfiguration
8. Configure client and server

## Run the playbook:
ansible-playbook -i hosts local.yml --extra-vars @pathto/creds.json
try from the client:
```
while true ; do curl 5.5.5.52 ; sleep 0.5 ; done
while true ; do curl --interface 10.1.4.2 5.5.5.51 ; sleep 0.5 ; done
while true ; do curl --interface 10.1.4.3 5.5.5.51 ; sleep 0.5 ; done
while true ; do curl --interface 10.1.4.4 5.5.5.51 ; sleep 0.5 ; done
```
check the BGP routes:
```



show ip route
```
stop the docker to make sure BGP will update (RHI feature):
```
sudo docker stop web4
sudo docker stop web3
```

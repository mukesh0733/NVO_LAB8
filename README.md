##  NVO_LAB8
Objectives: Virtualized Network Automation
1)	Automate the creation of multiple virtual networks (VNs) within the hypervisor and their connection to the public network.
2)	Automate the creation of multiple VMs within the hypervisor-
  - Both single tenant (same VN) and multi-tenant (different VNs).
  - All VMs should be accessible from the host server and be able to access the Internet.
3)	Automate the security groups and port security configuration to make intra-VN and inter-VN communication possible.
4)	Automate spinning up and configuring a Quagga/FRR BGP router as a Docker container.
a)	Automate its BGP configuration to peer with the SDN controller in the next objective.
5)	Automate spinning up and configuring an SDN controller as another Docker container.
  - Automate its BGP speaker configuration to peer with Quagga/FRR.

-----
# Main.py:

The main python file will import all the modules simulatenouly. We can modify the main file to run as more interactively(user imput for specific modules if required).
The scope of this lab was sequential. The input of the main module is given as NSOT like this, which can be again modified or gievn at the run time if needed. Before running
this script, user need to do folloing stuff in the devstack directory in the stack user of the openstack or user can import the .sh file downloaded form the openstack webpage.
- source openrc
- export | grep _os

-------

network_data(manually provided to the main.py):

                {'SDN-LAB8-net1': {'ip': '15.0.0.0/24', 'subnets': '', 'subnets_id': '','floating' : ''}, 
                'SDN-LAB8-net2': {'ip': '16.0.0.0/24', 'subnets': '', 'subnets_id': '','floating' : ''}, 
                'SDN-LAB8-net3': {'ip': '17.0.0.0/24', 'subnets': '', 'subnets_id': '','floating' : ''}}

Network_data at start:
![image](https://user-images.githubusercontent.com/71536049/112732424-7e32df80-8eff-11eb-9c17-2161645007ab.png)

Updated Network_data:
![image](https://user-images.githubusercontent.com/71536049/112732645-c30b4600-8f00-11eb-914a-89e162bf4f61.png)


-------
# Objective: Create_vn:

- The main module will call the create_vn module with already defined network_data. and will create all the given subnet and then update the original network_data details. 
![image](https://user-images.githubusercontent.com/71536049/112732502-eed9fc00-8eff-11eb-867d-e35c26980737.png)

- Created a Public router and then attached all those created interfaces in it.
![image](https://user-images.githubusercontent.com/71536049/112732507-fa2d2780-8eff-11eb-9f41-dacd4d5c253e.png)

- Error handing if interfaces are already created or some other issues arises.
- returned the updated network_data to the main module.

----


# Objective: Create_vm:
- The main module will now calls the create_vm module with the updated network_data details. 

- Now it will create individual 1-VM for all indiviual virtual networks and one vm which will have all the virtual networks. 
![image](https://user-images.githubusercontent.com/71536049/112732528-1f219a80-8f00-11eb-9205-346d49c30c83.png)

- Creating the floating ip, attaching them to individual vms and then updated this floating ip information to the global network_data.
![image](https://user-images.githubusercontent.com/71536049/112732542-33fe2e00-8f00-11eb-89e8-ca4f91f39dee.png)

- Here only the virtual networks are getting changed while creating a new vm. All other variables are hard-coded to the dafault values such as flavour,image-name, key-name and etc. It can be modified depending upon the requirments. 
- Error handing at various steps.

-----

# Objective: Create_sec_group:
- The main module will now calls the create_sec_group module with the updated network_data details. 
- It will create a new sec_gorup with the default rules.
![image](https://user-images.githubusercontent.com/71536049/112732564-5b54fb00-8f00-11eb-8326-6b904762f2bf.png)

- Now the tool will add the ICMP allow rules for given virtual networks.
![image](https://user-images.githubusercontent.com/71536049/112732579-6c9e0780-8f00-11eb-841b-27b9d047c963.png)

- Now the tool will apply this sec_group to the already created virtual machines in the objective2.
![image](https://user-images.githubusercontent.com/71536049/112732588-7de71400-8f00-11eb-9959-d37bac8c5d5a.png)

- Error handling at various steps.

-----

# Objective: Create_frr_bgp:
- Already created a base image first for this. In the base imagem the bgpd module enabled. if we do not want to make a base image then,
we just need to do a start/stop of the container to make into effect this change then.
- The main module will now calls the create_frr_bgp module. 
- The tool will create a frr.conf file with the desired bgp config details. We can read already created files too. Need to to little modification for that.
- Now the tool will take this already created 'frr.conf' file and map to the new running container.
- At the end showing varius bgp commands for the neighborship and the network details. 
-  Error handling at various steps.
![image](https://user-images.githubusercontent.com/71536049/112732753-6e1bff80-8f01-11eb-8516-bd6b5dbd303b.png)

![image](https://user-images.githubusercontent.com/71536049/112732762-7f650c00-8f01-11eb-893e-8b458bab7210.png)

-------

# Objective: Create_ryu_bgp:
- In this objective, there was a paramiko issue, The container was not ables to install paramiko files. So commented the ssh part in the application.py and created a new base image for this objective. 
- The main module will now call the create_ryu_bgp module.
- Her we need a conf file to run the container. So I already created a ryu_bgp.py with the configurations. We can create a file on the go too, future enhnacements if requires.
- The tool will take this ryu_bgp.py file and will create a new conatiner. 
- Now the tool will start the ryu_bgp application with the already provided config file. 
- Error handling at various steps.
![image](https://user-images.githubusercontent.com/71536049/112732776-9572cc80-8f01-11eb-9362-f03e3f536272.png)

------

# Verifications:
- Virtual networks:
![image](https://user-images.githubusercontent.com/71536049/112732821-eaaede00-8f01-11eb-8e43-0a548a43e33a.png)
--

- Virtual public router and the subent details:
![image](https://user-images.githubusercontent.com/71536049/112732837-ff8b7180-8f01-11eb-8470-e0b96bc75778.png)
![image](https://user-images.githubusercontent.com/71536049/112732844-0c0fca00-8f02-11eb-8e52-d6c2f1e8c8f0.png)
--

- Individual Virtual machines
![image](https://user-images.githubusercontent.com/71536049/112732858-1f229a00-8f02-11eb-9487-111f87135671.png)
--

- Floatinp ip list:
![image](https://user-images.githubusercontent.com/71536049/112732864-31043d00-8f02-11eb-9e13-f6cbf94a0d93.png)

- Security gorup:
![image](https://user-images.githubusercontent.com/71536049/112732882-47aa9400-8f02-11eb-9ea5-ab4d622ba357.png)

- New updated security group rules:
![image](https://user-images.githubusercontent.com/71536049/112732888-55f8b000-8f02-11eb-82e7-11f7b58aa923.png)

- Instance snapshot:
![image](https://user-images.githubusercontent.com/71536049/112732924-79bbf600-8f02-11eb-81fc-ae4095e7fb9d.png)

- Topology created via tool:
![image](https://user-images.githubusercontent.com/71536049/112732971-d15a6180-8f02-11eb-89e4-8b584fcb559d.png)
![image](https://user-images.githubusercontent.com/71536049/112732994-f18a2080-8f02-11eb-821e-55772df51766.png)

- Connectivity check:
![image](https://user-images.githubusercontent.com/71536049/112733237-4da17480-8f04-11eb-93e8-db4be412925e.png)

- Docker ps:
![image](https://user-images.githubusercontent.com/71536049/112733009-0797e100-8f03-11eb-835c-5d3b3f1046ba.png)






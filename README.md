# NVO_LAB8
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
The main python file will import all the modules simulatenouly. We can modify the main file to run as more interactively(user imput for specific modules if required).
The scope of this lab was sequential. The input of the main module is given as NSOT like this, which can be again modified or gievn at the run time if needed. Before running
this script, user need to do folloing stuff in the devstack directory in the stack user of the openstack or user can import the .sh file downloaded form the openstack webpage.
- source openrc
- export | grep _os

network_data = 
                
                {'SDN-LAB8-net1': {'ip': '15.0.0.0/24', 'subnets': '', 'subnets_id': '','floating' : ''}, 
                
                'SDN-LAB8-net2': {'ip': '16.0.0.0/24', 'subnets': '', 'subnets_id': '','floating' : ''}, 
                
                'SDN-LAB8-net3': {'ip': '17.0.0.0/24', 'subnets': '', 'subnets_id': '','floating' : ''}}
-------
Objective:1:Create_vn:
- The main module will call the create_vn module with already defined network_data. and will create all the given subnet and then update the original network_data details. 
- Created a Public router and then attached all those created interfaces in it.
- Error handing if interfaces are already created or some other issues arises.
- returned the updated network_data to the main module.

Objective:2:Create_vm:
- The main module will now calls the create_vm module with the updated network_data details. 
- Now it will create individual 1-VM for all indiviual virtual networks and one vm which will have all the virtual networks. 
- Cretateing the loating ip, attaching them to individual ips and then updated this floating ip information to the global network_data.
- Here only the network details are getting changed while creating a new vm. All other variables are hard-coded to the dafault values such as flavour,image-name, key-name. 
it can be later modified depending upon the requirments. 
- Error handing at various steps.

Objective:3:Create_sec_group:
- The main module will now calls the create_sec_group module with the updated network_data details. 
- It will create a new sec_gorup and add the ICMP allow rules for given virtual networks.
- Now it will apply this sec_group to the already created virtual machines in the objective2.
- Error handling at various steps.

Objective:4:Create_frr_bgp:
- Already created a base image first for this. In the base image the bgpd module enabled. if we do not want to make a base image then we can add this step in this objective,
we just need to do a start/stop of the container to make into effect this change then.
- The main module will now calls the create_frr_bgp module. 
- The tool will create a frr.conf file with the desired bgp config details. We can read already created files too. Need to to little modification for that.
- Now the tool will take this already created 'frr.conf' file and map to the new running container.
- At the end showing varius bgp commands for the neighborship and the network details. 
-  Error handling at various steps.

Objective:5:Create_ryu_bgp:
- In this objective, there was a paramiko issue, The container was not ables to install paramiko files. So commented the ssh part in the application.py and created a new base image for this objective. 
- The main module will now call the create_ryu_bgp module.
- Her we need a conf file to run the container. So I already created a ryu_bgp.py with the configurations. We can create a file on the go too, future enhnacements if requires.
- The tool will take this ryu_bgp.py file and will create a new conatiner. 
- Now the tool will start the ryu_bgp application with the already provided config file. 
- Error handling at various steps.



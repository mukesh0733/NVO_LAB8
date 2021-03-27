try:
    import os
except Exception as e:
    print(e)

def create_sec_group(network_data):
    # network_data = {'SDN-LAB8-net1':{'ip':'15.0.0.0/24','subnets':'','subnets_id':''}, 'SDN-LAB8-net2':{'ip':'16.0.0.0/24','subnets':'','subnets_id':''}, 'SDN-LAB8-net3':{'ip':'17.0.0.0/24', 'subnets':'','subnets_id':''}}
    try:
        group = os.popen('openstack security group list').read()
        sec_group_name = 'SDN_LAB8'
        if 'SDN_LAB8' not in group:
            os.popen('openstack security group create '+ sec_group_name + ' --description "ICMP traffic allow"').read()
            print('Sec group:{} created and default rules for the sec group:'.format(sec_group_name))
            os.system('openstack security group rule list ' + sec_group_name)
        else:
            print("{} sec gorup already created.".format(sec_group_name))

        for i,j in network_data.items():
            os.popen('openstack security group rule create ' + sec_group_name  + ' --protocol icmp --remote-ip ' + network_data[i]['ip']).read()
        
        os.popen('openstack security group rule create ' + sec_group_name  + ' --protocol icmp --remote-ip 172.24.4.0/24').read()

        print('\nNew Updated rules for the sec gorup: {}'.format(sec_group_name))
        os.system('openstack security group rule list \n' + sec_group_name)
        
        for m in range(1,4):
            os.popen('openstack server add security group SDN_LAB8_VM_' + str(m) + ' ' + sec_group_name ).read()
            print('New sec gorup: {} appied on VM: SDN_LAB8_VM_{}'.format(sec_group_name,str(m)))
        os.popen('openstack server add security group SDN_LAB8_VM_COMMON ' + sec_group_name).read()
        print('New sec gorup: {} appied on VM: SDN_LAB8_VM_COMMON'.format(sec_group_name))
    except Exception as e:
        print(e)
# create_sec_group()

try:
    import os
except Exception as e:
    print(e)

def create_network(network_data):
    try:
        networks = os.popen('openstack network list').read()
        # network_data = {'SDN-LAB8-net1':{'ip':'15.0.0.0/24','subnets':'','subnets_id':''}, 'SDN-LAB8-net2':{'ip':'16.0.0.0/24','subnets':'','subnets_id':''}, 'SDN-LAB8-net3':{'ip':'17.0.0.0/24', 'subnets':'','subnets_id':''}}
        for i,j in network_data.items():
            if i not in networks:
                os.popen('openstack network create ' + i).read()
                os.popen('openstack subnet create subnet1 --network ' + i + ' --subnet-range ' + network_data[i]['ip']).read()
                op = os.popen('openstack network show '+ i).read()
                network_data[i]['subnets'] = op.split('|\n|')[24].split('|')[-1].strip()
                network_data[i]['subnets_id'] = op.split('|\n|')[6].split('|')[-1].strip()
                print('Created network:{} ip:{}'.format(i,network_data[i]['ip']))
            else:
                print('Network: {} ip:{} already created..'.format(i,network_data[i]['ip']))
                op = os.popen('openstack network show '+ i).read()
                network_data[i]['subnets'] = op.split('|\n|')[24].split('|')[-1].strip()
                network_data[i]['subnets_id'] = op.split('|\n|')[6].split('|')[-1].strip()
    
        # public router created and the subnet addition
        routers = os.popen('openstack router list').read()
        router_name = 'SDN_LAB8'
        if router_name not in routers:
            os.popen('openstack router create ' + router_name).read()
            os.popen('openstack router set SDN_LAB8 --external-gateway public').read()
            print('\nPublic router:{} created'.format(router_name))
            for i,j in network_data.items():
                os.popen('openstack router add subnet ' + router_name + ' ' + network_data[i]['subnets']).read()
                print('Subnet:{} added into the router:{}'.format(network_data[i]['ip'],router_name))
        else:
            print('Router {} already in the system'.format(router_name))
            try:
                os.system('openstack router set SDN_LAB8 --external-gateway public')
                for i,j in network_data.items():
                    print(network_data[i]['subnets'])
                    os.system('openstack router add subnet ' + router_name + ' ' + network_data[i]['subnets'])
            except:
                pass
        return network_data
    except Exception as e:
        print(e)

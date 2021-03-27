try:
    import os
except Exception as e:
    print(e)

def create_virtual_machine(network_data):
    # network_data = {'SDN-LAB8-net1': {'ip': '15.0.0.0/24', 'subnets': 'ee755e36-3e02-48c6-a21b-800a676a0ff1', 'subnets_id': '21efb43f-5b62-41b1-b570-489475a6c0e7','floating' : ''}, 'SDN-LAB8-net2': {'ip': '16.0.0.0/24', 'subnets': 'ec021d0d-9076-4360-b972-fa3a706ef119', 'subnets_id': '1542e623-7010-4d27-bbd2-999e5ec15e15','floating' : ''}, 'SDN-LAB8-net3': {'ip': '17.0.0.0/24', 'subnets': 'e33a644c-ac7f-44d1-9131-f9157ace6e54', 'subnets_id': 'bc7545d7-e51d-4477-8c72-c9b22eabf426','floating' : ''}}
    count = 1
    try:
        floating_ip = []
        for i,j in network_data.items():
            os.popen('openstack server create --flavor m1.tiny --image cirros-0.5.1-x86_64-disk --nic net-id=' + network_data[i]['subnets_id'] + ' --security-group default --key-name mykey ' + 'SDN_LAB8_VM_' + str(count)).read()
            print('Server created: {} with vn: {}'.format('SDN_LAB8_VM_'+str(count),network_data[i]['ip']))
            count += 1
        os.popen('openstack server create --flavor m1.tiny --image cirros-0.5.1-x86_64-disk --nic net-id=' + network_data['SDN-LAB8-net1']['subnets_id'] +' --nic net-id=' + network_data['SDN-LAB8-net2']['subnets_id'] + ' --nic net-id=' + network_data['SDN-LAB8-net3']['subnets_id'] +' --security-group default --key-name mykey ' + 'SDN_LAB8_VM_COMMON').read()
        print('Server created: {} with all interfaces {}\n'.format('SDN_LAB8_VM_COMMON','15.0.0.0/24,16.0.0.0/24,17.0.0.0/24'))
        try:
            for m in range(1,5):
                os.popen('openstack floating ip create public --description SDN_LAB8_VM_' + str(m)).read()
                float_ip_list = os.popen('openstack floating ip list').read()
                try:
                    for i in range(8,len(float_ip_list.split('|')),7):
                        p = float_ip_list.split('|')[i+1].strip()
                        if p not in floating_ip:
                            floating_ip.append(p)
                            if m <= 3:
                                os.system('openstack server add floating ip SDN_LAB8_VM_' + str(m)+ ' ' + p)
                                print('Floating ip:{} added for server SDN_LAB8_VM_{}'.format(p,str(m)))
                                key = 'SDN-LAB8-net'+str(m)
                                network_data[key]['floating'] = p
                            if m > 3:
                                os.system('openstack server add floating ip SDN_LAB8_VM_COMMON ' + p)
                                print('Floating ip:{} added for server SDN_LAB8_VM_COMMON'.format(p))
                except:
                    pass
        except Exception as e:
            print(e)
        return network_data
    except Exception as e:
        print(e)
# create_vm()

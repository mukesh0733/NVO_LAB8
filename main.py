try:
    import create_vn
    import create_vm
    import create_sec_group
    import create_frr_bgp
    import create_ryu_bgp
except Exception as e:
    print(e)

def main():
    try:
        network_data = {'SDN-LAB8-net1': {'ip': '15.0.0.0/24', 'subnets': '', 'subnets_id': '','floating' : ''}, 
                        'SDN-LAB8-net2': {'ip': '16.0.0.0/24', 'subnets': '', 'subnets_id': '','floating' : ''}, 
                        'SDN-LAB8-net3': {'ip': '17.0.0.0/24', 'subnets': '', 'subnets_id': '','floating' : ''}}
        print('\n ----------- Default Network data input to all the modules ----------- \n')
        print(network_data)
        
        print('\n ----------- Create network module started ----------- \n')
        create_vn.create_network(network_data)
        
        print('\n ----------- Create virtual machine module started ----------- \n')
        create_vm.create_virtual_machine(network_data)
        
        print('\n ----------- Create sec gorup module started ----------- \n')
        create_sec_group.create_sec_group(network_data)

        print('\n ----------- Updated Network data ----------- ')
        print(network_data)
        
        print('\n ----------- Create ryu bgp module started ----------- \n')
        create_ryu_bgp.create_ryu_bgp()

        print('\n ----------- Create frr bgp module started ----------- \n')
        create_frr_bgp.create_frr_bgp()
    except Exception as e: 
        print(e)
main()

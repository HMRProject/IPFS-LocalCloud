import os
import base64

key = base64.b64encode(os.urandom(32)).decode()
with open("swarm.key", "w") as f:
    f.write("/key/swarm/psk/1.0.0/\n")
    f.write("/base16/\n")
    f.write(key)
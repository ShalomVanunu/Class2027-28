
file="ListIPs.txt"

def Checkfile(file="ListIPs.txt"):
    internal = []
    external = []
    with open(file,"r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("192.168."):
                internal.append(line)
            elif line.startswith("10."):
                external.append(line)
    return internal, external

external_IPs, internal_IPs = Checkfile(file)
#print(internal_IPs)
#print(external_IPs)

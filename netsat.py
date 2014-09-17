import re
 
def GetInterfaces():
    ret = {}
    f = open("/proc/net/dev", "r");
    data = f.read()
    f.close()
 
    r = re.compile("[:\s]+")
 
    lines = re.split("[\r\n]+", data)
    for line in lines[2:]:
        columns = r.split(line)
        if len(columns) < 18:
            continue
        info                  = {}
        info["rx_bytes"]      = columns[2]
        info["rx_packets"]    = columns[3]
        info["rx_errors"]     = columns[4]
        info["rx_dropped"]    = columns[5]
        info["rx_fifo"]       = columns[6]
        info["rx_frame"]      = columns[7]
        info["rx_compressed"] = columns[8]
        info["rx_multicast"]  = columns[9]
 
        info["tx_bytes"]      = columns[10]
        info["tx_packets"]    = columns[11]
        info["tx_errors"]     = columns[12]
        info["tx_dropped"]    = columns[13]
        info["tx_fifo"]       = columns[14]
        info["tx_frame"]      = columns[15]
        info["tx_compressed"] = columns[16]
        info["tx_multicast"]  = columns[17]
 
        iface                 = columns[1]
        ret[iface] = info
    return ret
 
interfaces = GetInterfaces()
for(iface, info) in interfaces.items():
 
    print "Interface: %s" % (iface)
    for (metric, value) in info.items():
        print "% 10s% 20s = %s" % (" " * 10, metric, value)
    print

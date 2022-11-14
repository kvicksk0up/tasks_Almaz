import re

def find_log():
    l = []
    with open('str_log.txt') as str_log:
        for i in str_log:
            ip = re.match('\w+.\w+.\w+.\w+', i)
            ip = ip.group(0)
            l.append(ip)
    d = {x: l.count(x) for x in l}
    print(max(d.values()))
find_log()
import re

x = 'Email from pyzhai@umcih.edu ; time: 12:30:33 '
y = re.findall('\S+@\S+', x)
print(y)
z = re.findall('^Email from (\S+@\S+)', x)
print(z)
at = z[0].find('@')
blank = z[0].find(' ', at)
host_server = z[0][at + 1:blank]
print(host_server)
host_server2 = re.findall('@([^ ]*)', x)
print(host_server2)

# netifaces

- A portable third-party library in Python to enumerate network interfaces on local machine.
- Historically it has been difficult to straightforwardly get the network address(es) of the machine on which your Python scripts are running without compromising the portability of your script.
- `netifaces` takes care of enumerating interfaces, network addresses and also preserves the portability(works on all *nix systems atleast).

## Installation

netifaces needs python extension modules. In case you haven’t already, you should install python-dev package.

```
$ sudo apt-get install python-dev
```

You can install netifaces using PIP.

```
$ pip install netifaces
```

## Basic operations

You can take a look at all the modules that are part of netifaces

```
>>> import netifaces
>>> 
>>> dir(netifaces)
[ ... snipped ...
'address_families', 'gateways', 'ifaddresses', 'interfaces', 'version']
>>> 
```

Getting a list of all the network interface identifiers on the machine.

```
>>> netifaces.interfaces()
['lo', 'eth0', 'wlan0', 'eth3', 'vboxnet0']
```

You can ask for the addresses of a particular interface

```
>>> import netifaces
>>> from pprint import pprint
>>>
>>> pprint(netifaces.ifaddresses('eth3'))
{2: [{'addr': '192.168.1.100',
      'broadcast': '192.168.1.255',
      'netmask': '255.255.255.0'}],
 10: [{'addr': 'fe80::364b:50ff:feb7:ef1d%eth3',
       'netmask': 'ffff:ffff:ffff:ffff::/64'}],
 17: [{'addr': '34:4b:50:b7:ef:1d', 'broadcast': 'ff:ff:ff:ff:ff:ff'}]}
```

## pprint

- pprint contains a “pretty printer” for producing aesthetically pleasing representations of your data structures
- The formatter produces representations of data structures that can be parsed correctly by the interpreter, and are also easy for a human to read

You can also get list of all the gateways

```
>>> netifaces.gateways()
{'default': {2: ('192.168.1.1', 'eth3')}, 2: [('192.168.1.1', 'eth3', True)]}
```

Getting list of IPv4 addresses excluding loopback and virtualbox adapters

```
>>> for iface in netifaces.interfaces():
...     if iface == 'lo' or iface.startswith('vbox'):
...         continue
...     iface_details = netifaces.ifaddresses(iface)
...     if iface_details.has_key(netifaces.AF_INET):
...         print iface_details[netifaces.AF_INET]
... 
[{'broadcast': '192.168.1.255', 'netmask': '255.255.255.0', 'addr': '192.168.1.100'}]
[{'broadcast': '192.168.1.255', 'netmask': '255.255.255.0', 'addr': '192.168.1.101'}]
```

## Examples of netifaces usage in open source projects

For more examples of netifaces usage in open source projects: [http://www.programcreek.com/python/example/81895/netifaces.interfaces](http://www.programcreek.com/python/example/81895/netifaces.interfaces)


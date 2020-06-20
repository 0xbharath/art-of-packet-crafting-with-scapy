# netaddr

A Python library for representing and manipulating network addresses.

## Features

### Layer 3 addresses

- IPv4 and IPv6 addresses, subnets, masks, prefixes
- Iterating, slicing, sorting, summarizing and classifying IP networks
- Dealing with various ranges formats (CIDR, arbitrary ranges and globs, nmap)
- Set based operations (unions, intersections etc) over IP addresses and subnets
- Parsing a large variety of different formats and notations
- Looking up IANA IP block information
- Generating DNS reverse lookups
- Supernetting and subnetting

### Layer 2 addresses

- Representation and manipulation MAC addresses and EUI-64 identifiers
- Looking up IEEE organisational information (OUI, IAB)
- Generating derived IPv6 addresses

## Installation

Install the latest netaddr from PIP

```
pip install netaddr
```

Importing netaddr

```
from netaddr import *
```

> **Importing modules**
> 
> Importing this way is not optimal and leads to name clashes.
> 
> In your own code, you should be explicit about the classes, functions and constants you import to avoid name clashes.


## Layer 3 addressing(IP)

### IPAddress

IPAddress object represents a single IP address.

```
>>> from netaddr import IPAddress
>>>
>>> ip = IPAddress('192.21.8.11')
>>> ip.version
4
>>> dir(ip)
[ ... Snipped... 'bin', 'bits', 'format', 'info', 'ipv4', 'ipv6', 
'is_hostmask', 'is_ipv4_compat', 'is_ipv4_mapped', 'is_link_local',
'is_loopback', 'is_multicast', 'is_netmask', 'is_private', 'is_reserved',
'is_unicast', 'key', 'netmask_bits', 'packed', 'reverse_dns', 'sort_key',
'value', 'version', 'words']
>>> 
```

There are methods to handle coverting an IP adress into binary or bits, split an IP, pack an

```
>>> ip.bin
'0b11000000000101010000100000001011'
>>> 
>>> ip.bits()
'11000000.00010101.00001000.00001011'
>>> 
>>> ip.words
(192, 21, 8, 11)
>>> ip.packed
'\xc0\x15\x08\x0b'
```

There are methods to check if the type of IP address(class, scope, type)

```
>>> ip.version
6
>>> ip.is_unicast()
True
>>> 
>>> ip.is_link_local()
True
```

### IPNetwork

IPNetwork objects are used to represent subnets, networks or VLANs that accept CIDR prefixes and netmasks.

```
>>> from netaddr import IPNetwork
>>> 
>>> ip_range = IPNetwork('192.241.21.6/24')
>>> 
>>> dir(ip_range)
[ ... snipped ...  'broadcast', 'cidr', 'first', 'hostmask', 'info',
'ip', 'ipv4', 'ipv6', 'is_ipv4_compat', 'is_ipv4_mapped', 'is_link_local',
'is_loopback', 'is_multicast', 'is_private', 'is_reserved', 'is_unicast',
'iter_hosts', 'key', 'last', 'netmask', 'network', 'next', 'prefixlen',
'previous', 'size', 'sort_key', 'subnet', 'supernet', 'value', 'version']
>>>
```

There are a bunch of methods associated with IPNetwork to understand the network defined.

```
>>> ip_range.network
IPAddress('192.241.21.0')
>>>
>>> ip_range.hostmask
IPAddress('0.0.0.255')
>>> 
>>> ip_range.netmask
IPAddress('255.255.255.0')
>>>
>>> ip_range.broadcast
IPAddress('192.241.21.255')
>>>
>>> ip_range.size
256
```

You can use a simple for loop to iterate over the list of IP addresses in the network range defined.

```
>>> for i in ip_range:
...     print i
... 
192.241.21.0
192.241.21.1
... snipped ...
192.241.21.255
```

#### List operations on IPNetwork object

If you treat an IPNetwork object as if it were a standard Python list object it will give you access to a list of individual IP address objects also various standard python list methods.

```
>>> ip_range = IPNetwork('192.0.2.16/29')
>>> 
>>> ip_range_list = list(ip_range)
>>> 
>>> len(ip_range_list)
8
>>> ip_range_list
[IPAddress('192.0.2.16'), IPAddress('192.0.2.17'), ...snipped... IPAddress('192.0.2.23')]
>>>
>>> ip_range_list[6]        # indexing
IPAddress('192.0.2.22')
>>>
>>> ip_range_list[2:5

]      # slicing
[IPAddress('192.0.2.18'), IPAddress('192.0.2.19'), IPAddress('192.0.2.20')]
```

### IPRange

You can represent an arbitrary IP address range using a lower and upper bound address in the form of an IPRange object.

```
>>> ip_range = IPRange('192.168.1.0', '192.168.1.20')
>>> 
>>> for i in ip_range:
...     print i
... 
192.168.1.0
... snipped ...
192.168.1.19
192.168.1.20
```

### IP sets

You can specify either IP addresses and networks as strings. Alternatively, you can use IPAddress, IPNetwork, IPRange or other IPSet objects.

```
>>> IPSet(['192.0.2.0'])
IPSet(['192.0.2.0/32'])
>>>
>>> IPSet([IPAddress('192.0.2.0')])
IPSet(['192.0.2.0/32'])
>>>
>>> IPSet([IPNetwork('192.0.2.0/24')])
IPSet(['192.0.2.0/24'])
>>>
>>> IPSet(IPRange("10.0.0.0", "10.0.1.31"))
IPSet(['10.0.0.0/24', '10.0.1.0/27'])
```

You can interate over all the IP addresses that are members of the IP set.

```
>>> for ip in IPSet(['192.0.2.0/28']):
...     print ip
192.0.2.0
192.0.2.1
... snipped ...
192.168.2.15
```

Adding and removing set elements

```
>>> from netaddr import IPSet
>>> 
>>> s1 = IPSet()
>>> 
>>> s1.add('192.168.1.0/30')
>>> s1.size
4
>>> 
>>> '192.168.1.3' in s1
True
>>> 
>>> s1.remove('192.168.1.3')
>>> s1.size
3
```

You can do all sorts of set operations on IPSets

```
>>> scan1 = IPSet(['192.168.1.0/30'])
>>> 
>>> scan1
IPSet(['192.168.1.0/30'])
>>> 
>>> scan1.size
4
>>> 
>>> scan2 = IPSet(['192.168.1.0/31'])
>>> 
>>> scan2.size
2
>>> 
>>> scan1 | scan2
IPSet(['192.168.1.0/30'])
>>> 
>>> scan1 & scan2
IPSet(['192.168.1.0/31'])
>>>
>>> scan1 ^ scan2
IPSet(['192.168.1.2/31'])
```

### Layer 2 addressing(MAC)

Instances of the EUI class are used to represent MAC addresses.

```
>>> mac = EUI('ec:f4:bb:87:2d:0c')
```

There are methods to print out common properties of an address

```
>>> dir(mac)
 ... snipped ... 'bin', 'bits', 'dialect', 'ei', 'eui64', 'iab',
'info', 'ipv6', 'ipv6_link_local', 'is_iab', 'modified_eui64', 'oui',
'packed', 'value', 'version', 'words']
>>>
>>> str(mac), str(mac.ei), str(mac.oui), str(mac.version)
('EC-F4-BB-87-2D-0C', '87-2D-0C', 'EC-F4-BB', '48')
```

There are methods to provide info on OUI and other organizational info.

```
>>> mac.info
{'OUI': {'address': ['one dell way',
             'MS:RR5-45',
             'Round rock Texas 78682',
             'UNITED STATES'],
 'idx': 15529147,
 'offset': 3429092,
 'org': 'Dell Inc',
 'oui': 'EC-F4-BB',
 'size': 141}}
>>> 
```

```
>>> oui = mac.oui
>>> 
>>> dir(oui)
[ ... snipped ... 'records', 'reg_count', 'registration']
>>> 
>>> oui.registration().org
'Dell Inc'
>>>
>>> oui.registration().address
['one dell way', 'MS:RR5-45', 'Round rock Texas 78682', 'UNITED STATES']
```

## Examples of netaddr usage in open source projects

For more examples of various netaddr modules usage in open source projects: [http://www.programcreek.com/python/index/2955/netaddr](http://www.programcreek.com/python/index/2955/netaddr)


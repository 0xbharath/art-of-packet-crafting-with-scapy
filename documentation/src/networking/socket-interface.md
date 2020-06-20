# Socket Interface

![socket-interface](../imgs/socket_interface.png)

## Raw sockets

Kernel offers two ways to forge packets:

### Layer 3 - PF_INET, SOCK_RAW

- Classic raw sockets
- Lot of heavy lifting is done by the kernel which means there is a limitation on what you can do

### Layer 2 - PF_PACKET, PF_RAW

- No hand holding by kernel
- There is no limit on what you craft and send
- You are responsible for choosing interfaces, linktypes, ARP stuff, calculate checksum etc
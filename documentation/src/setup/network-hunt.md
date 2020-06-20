# Network Hunt


## Setup



Directory tree for the lab on your *attacker machine*

```
/
│
└───home
    │
    └───network_hunt_challenge
        │    
        └── network_hunt.py
```


- Run the `network_hunt.py` script as root


```
sudo python network_hunt.py 
```

- If the script executed without errors, the challenge is setup!
- The lab will start and `tap0` interface will be created.
- Terminating the script will deallocate this interface and release all state.


Refer to "exercises" section –> "network hunt" page in this notes for instruction on cracking the challenge.

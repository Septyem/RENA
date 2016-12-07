# RENA - Redundancy-Eliminating Network (traffic) Analyzer

RENA is supposed to be a framework to deal with PCAP file for on-site CTFs, features including payloads extraction, deduplication, crash test, database management and display.

The name seems to be weird but its abbreviation looks good:)

__WARNING:__ Not well-tested now. Should be updated after we play several on-site CTFs.

# Usage

```python
import rena

context = {
"chals": [
    {"id":"bin1","binary": "./overflow", "port": 666}], 
"ip": "1.1.1.1",
"name": "comp"}

a=rena.PCAP(context=context)
a.run('test-defcon.cap')
a.display()
```

# Installation

Only tested on Ubuntu 14.04 now. But should work on other Linux distros. You can install it with following commands:

```sh
apt-get update
apt-get install python2.7 python-pip tshark sqlite3
pip install --upgrade rena
```

# TODO List
* More flexible deduplicate policy
* More friendly config
* Add logging support
* Better display. Maybe Web UI
* UDP support?

Since I'm unlikely to fulfill it recently due to lack of time, any bug report or pull request would be appreciated.

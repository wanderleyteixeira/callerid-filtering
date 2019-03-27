## Description ##
Python script to blacklist a Caller ID to [VoIP.ms](https://voip.ms). This script uses the [voipms](https://pypi.org/project/voipms/) to wrap around the VoIP.ms RESTful API. Has an easily-usable command line to send a Caller ID to VoIP.ms.

This is a script that adds a Caller ID filter to a VoIP.ms account. When I receive a telemarketer or unwanted call to one of my phone lines, I want to make sure that never happens again. This script allows me to quickly add a number that next time the caller tried to reach me, it will be hung up automatically. Also, you could set different actions such as busy tone, no service message, or even a message that the number is disconnected.

## Requirements

* Python (tested with 3.7)
* VoIP.ms account with API enabled

## Installation

To install voipms with pip, run: `pip install voipms`

## Basic Usage

Enable API support in your [VoIP.ms account](https://voip.ms/m/api.php). Click on `Enable API`, enter a password, and restrict to a static IP or open to all (_0.0.0.0_). 

You will need this password and the user account (e.g. email address registered) to allow the script to make RESTful API calls and blacklist the Caller ID.

Using a separate configuration file called `settings.py` containing:

```bash
user='<voip.ms username>'
key='<voip.ms key generated>'
```

The credentials are imported from the main file using:

```python
import settings
```

Run the script from the command line as follows:

```bash
python3.7 callerFilter.py NPANXXXXXXX "all" "hangup" "Spam (API)"
```

## TO DO

Automate using AppleScript + Mail to trigger the script.



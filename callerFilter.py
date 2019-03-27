#!/usr/bin/python
from voipms import VoipMs
import settings

def initAccount(user, password):
    voip = VoipMs(user, password)
    return voip

def addFilter(voip, callerid, did, action, note):
    callerid = checkISBN(callerid)
    if action == "hangup":
        routing = u"sys:hangup"
    elif action == "busy":
        routing = u"sys:busy"
    elif action == "noservice":
        routing = u"sys:noservice"
    elif action == "disconnected":
        routing = u"sys:disconnected"
    elif action == "ivr":
        routing = u"ivr:" + action
    print(voip.dids.set.caller_id_filtering(callerid, did, routing, note=note))

def getAllFilters(voip):
    raw_filters = voip.dids.get.caller_id_filtering(filtering=None)
    return raw_filters[u'filtering']

def checkISBN(callerid):
    if len(callerid) == 10 and callerid.isdigit():
        print("Incoming number for filtering", callerid)
        return callerid[-10:]
    else:
        raise SystemExit("Error: Invalid Caller ID %s" % callerid)

if __name__ == "__main__":
    import sys
    callerid = sys.argv[1]
    did = sys.argv[2]
    action = sys.argv[3] # either 'hangup' or 'ivr'
    note = ""
    #print(sys.argv, len(sys.argv)) #debug
    if len(sys.argv) == 5:
        note = sys.argv[4]

    client = initAccount(settings.user, settings.key)
    addFilter(client, callerid, did, action, note)


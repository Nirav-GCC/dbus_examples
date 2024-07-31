#!/usr/bin/env python3
from pyclbr import Function
import random
import re
import time
import dbus 
from gi.repository import GLib
import sys
import dbus.service

bus = dbus.SessionBus()
BUS = "org.example.demo.test"
server_object = bus.get_object(BUS,"/org/example/demo/test")
loop = GLib.MainLoop()
INTERVAL = 2
bus = dbus.SessionBus()
def make_method_call():

    reply = server_object.return_me()
    print(reply)
    return True

if __name__ == "__main__":
    print("starting client demo 9...")
    make_method_call()
    GLib.timeout_add_seconds(interval=INTERVAL,
                            function=make_method_call)

    loop.run()
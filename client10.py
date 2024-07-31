#!/usr/bin/env python3
from dataclasses import replace
from pyclbr import Function
import random
import re
import time
from traceback import print_tb
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

def make_method_call10():
    
    reply = server_object.give_data()
    print(reply)
    return True

if __name__ == "__main__":
    print("client demo 10 is started")
    make_method_call10()
    GLib.timeout_add_seconds(interval=INTERVAL,
                            function=make_method_call10)
    
    loop.run()
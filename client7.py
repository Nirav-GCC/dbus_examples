from http import server
from pyclbr import Function
import random
import re
import time
import dbus  # from pydbus import SystemBus
from gi.repository import GLib
import sys
import dbus.service
count = 1

bus = dbus.SessionBus()
BUS = "org.example.demo.test"
server_object = bus.get_object(BUS,"/org/example/demo/test")
loop = GLib.MainLoop()
INTERVAL = 2

def make_method_call7():
    name_list = ["Bob", "Pete", "Fred", "Sue", "Wendy"]
    name = name_list[random.randint(0, len(name_list)-1)]
    reply = server_object.greetings(name)
    return True

def msg_snd():
    global count
    print(count,"message sended")
    count+=1
    return True
    

if __name__ == "__main__":
    print("starting client demo 7...")
    GLib.timeout_add_seconds(interval=INTERVAL,
                            function=make_method_call7)
    GLib.timeout_add_seconds(interval=INTERVAL,
                            function=msg_snd)
    

    loop.run()
    
from pyclbr import Function
import random
import re
import time
import dbus  # from pydbus import SystemBus
from gi.repository import GLib
import sys
import dbus.service

# from deBus.client7 import make_method_call7
count = 1

bus = dbus.SessionBus()
BUS = "org.example.demo.test"
server_object = bus.get_object(BUS,"/org/example/demo/test")
loop = GLib.MainLoop()
INTERVAL = 2

# def str_data():
#     data = input("input data :")
#     print(data)

def make_method_call():
    # name_list = ["Bob", "Pete", "Fred", "Sue", "Wendy"]
    # name = name_list[random.randint(0, len(name_list)-1)]
    # reply = server_object.greetings(name)
    # str_data()

    reply = server_object.get_data()
    print(reply)
    print("data is :{}".format(reply))
    return True
    
    msg_snd()


def msg_snd():
    global count
    print(count,"message sended")
    count+=1
    return True

if __name__ == "__main__":
    print("starting client demo 8...")
    make_method_call()
    GLib.timeout_add_seconds(interval=INTERVAL,
                            function=make_method_call)
    # GLib.timeout_add_seconds(interval=INTERVAL,
    #                         function=msg_snd)
    

    loop.run()
    
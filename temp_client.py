from client11 import *
import time
import dbus  # from pydbus import SystemBus
from gi.repository import GLib
import sys
import dbus.service

# Instantiation, Constants , Variables...
bus = dbus.SessionBus()
BUS = "org.example.demo.test"
server_object = bus.get_object(BUS,"/org/example/demo/test")
loop = GLib.MainLoop()
INTERVAL = 2

def make_method_call_client_1():
    myData = input("Enter Data :")
    reply = server_object.server_no_args()
    print(reply)
    return True

if __name__=="__main__":
    print("Starting Client Demo 1...")
    # Call function to make a method call.
    GLib.timeout_add_seconds(interval=INTERVAL, 
                             function=make_method_call_client_1)
    loop.run()

from dataclasses import replace
import dbus
from gi.repository import GLib
import sys
import dbus.service

bus =dbus.SessionBus()
BUS="org.nirav.demo.test"
server_object = bus.get_object(BUS,"/org/nirav/demo/test")
loop =GLib.MainLoop()

def call_me_method():
    print("sending to the server ")
    reply = server_object.myFunction()
    return 

if __name__=="__main__":
    print("Client is succesfully started..")
    call_me_method()
    loop.run()
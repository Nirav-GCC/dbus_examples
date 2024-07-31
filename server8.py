#!/usr/bin/env python3
import time
from traceback import print_tb
import dbus
from gi.repository import GLib
import dbus.service
import dbus.mainloop.glib

class DBusService_XML(dbus.service.Object):
    @dbus.service.method("org.example.demo.test",
                        in_signature='',out_signature='s')
    def get_data(self):
        data = input("Enter data:")
        print(type(data))
        print(data)
        return data

if __name__ == "__main__":
    print("starting the server demo 8...")
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()
    loop = GLib.MainLoop()
    name = dbus.service.BusName("org.example.demo.test",bus)
    object= DBusService_XML(bus,"/org/example/demo/test")
    
    loop.run()


#!/usr/bin/env python3
'''Objective: 
   Test that a server program can receive a method call using dbus.
   The method call receives data from the client.
   Uses the session bus '''
import time
import dbus
from gi.repository import GLib
import dbus.service
import dbus.mainloop.glib

class DBusService_XML(dbus.service.Object):
    @dbus.service.method("org.example.demo.test",
                        in_signature='',out_signature='')
    def greetings(self,name):
        print("Hello{}".format(name))
        return

if __name__ == "__main__":
    print("starting the server demo 7...")
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()
    loop = GLib.MainLoop()
    name = dbus.service.BusName("org.example.demo.test",bus)
    object= DBusService_XML(bus,"/org/example/demo/test")

    loop.run()
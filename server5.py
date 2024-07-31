#!/usr/bin/env python3
'''
Test that a server program can receive a method call using pydbus.
#   The method call then sends a time stamp back to the client.
#   Uses the session bus
'''
import time
import dbus
from gi.repository import GLib
import dbus.service
import dbus.mainloop.glib

class DBusService_XML(dbus.service.Object):
    @dbus.service.method("org.example.demo.test",
                        in_signature='',out_signature='s')
    def get_time_stamp(self):
        return str(time.time())

if __name__=="__main__":
    print("Starting the server demo 5..")
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()
    loop = GLib.MainLoop()
    name=dbus.service.BusName("org.example.demo.test",bus)
    object = DBusService_XML(bus,"/org/example/demo/test")

    loop.run()
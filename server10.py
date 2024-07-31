#!/usr/bin/env python3
import random
import dbus
from gi.repository import GLib
import dbus.service
import dbus.mainloop.glib


class DBusService_XML(dbus.service.Object):
    @dbus.service.method("org.example.demo.test",
                         in_signature='', out_signature='s')
    def give_data(self):
        myData = input("Enter the data to send :")
        return myData


if __name__ == "__main__":
    print("server demo 10 is started")
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()
    loop = GLib.MainLoop()
    name = dbus.service.BusName("org.example.demo.test", bus)
    object = DBusService_XML(bus, "/org/example/demo/test")

    loop.run()

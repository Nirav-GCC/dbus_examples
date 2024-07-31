#!/usr/bin/env python3
import signal
from ast import arguments
from inspect import signature
import dbus
from gi.repository import GLib
import sys
import dbus.service
import dbus.mainloop.glib

INTERVAL = 2


class DBusService_XML(dbus.service.Object):

    @dbus.service.method("org.example.demo.test",
                         in_signature='ss')
    def greetings(self, name, msg):
        print("name :{} & msg : {}".format(name, msg))
        object.mySignal(name, msg)

    @dbus.service.signal("org.example.demo.test", signature="ss")
    def mySignal(self, names, msg):
        pass


if __name__ == "__main__":
    print("server demo 11 is started")
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()
    loop = GLib.MainLoop()
    name = dbus.service.BusName("org.example.demo.test", bus)
    object = DBusService_XML(bus, "/org/example/demo/test")

    loop.run()

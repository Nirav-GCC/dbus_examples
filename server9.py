#!/usr/bin/env python3
from telnetlib import SE
import time
from traceback import print_tb
import dbus
from gi.repository import GLib
import dbus.service
import dbus.mainloop.glib
from requests import Session

class DBusService_XML(dbus.service.Object):
    @dbus.service.method("org.example.demo.test",
                        in_signature='',out_signature='s')
    def return_me(self):
        return "Return call"

if __name__=="__main__":
    print("server 9 demo start :")
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()
    loop = GLib.MainLoop()
    name = dbus.service.BusName("org.example.demo.test",bus)
    object= DBusService_XML(bus,"/org/example/demo/test")
    loop.run()


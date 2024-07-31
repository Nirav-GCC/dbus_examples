#!/usr/bin/env python3
import dbus
from gi.repository import GLib
import dbus.service
import dbus.mainloop.glib


class myCustom(dbus.service.Object):
    @dbus.service.method("org.nirav.demo.test",
                        in_signature='',out_signature='')
    def myFunction(self):
        print("Hello From Server..!")
        return

if __name__=="__main__":
    print("Server is started sucessfully")
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus=dbus.SessionBus()
    loop=GLib.MainLoop()
    name=dbus.service.BusName("org.nirav.demo.test",bus)
    object=myCustom(bus,"/org/nirav/demo/test")
    loop.run()
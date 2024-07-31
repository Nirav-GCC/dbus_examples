#!/usr/bin/env python3

import dbus
from gi.repository import GLib
import dbus.service
import dbus.mainloop.glib
# Variables / Constants / Instantiation...

message_count = 0
#dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)


class DBusService_XML(dbus.service.Object):
    @dbus.service.method("org.example.demo.test",
                        in_signature='',out_signature='')
    def server_no_args(self):
        "No arguments over the dbus. Server produces a message on the console."
        global message_count
        print("This is message {}".format(message_count))
        message_count +=1
        return 

if __name__ == "__main__":
    print("Starting Server Demo 1...")
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()  # essionBus
    #BUS = "org.example.demo.test"
    loop = GLib.MainLoop()
    name = dbus.service.BusName("org.example.demo.test",bus)
    object = DBusService_XML(bus,"/org/example/demo/test")
    #dbus.publish(BUS, DBusService_XML())

    loop.run()
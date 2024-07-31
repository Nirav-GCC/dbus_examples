#!/usr/bin/env python3
from hashlib import new
from operator import index
from re import T
from textwrap import indent
import dbus
from gi.repository import GLib
import sys
from threading import Thread
import dbus.service
import dbus.mainloop.glib
import sys


dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.SessionBus()
BUS = "org.example.demo.test"
server_object = bus.get_object(BUS, "/org/example/demo/test")
loop = GLib.MainLoop()
INTERVAL = 2
bus = dbus.SessionBus()


def user_return_signal(msg):

    my_index = msg.index(":")
    temp = (msg[:my_index])
    if(name != temp):

        print(msg)

    return True


def user_input_method():
    while True:
        mydata = input(f"{name}:")
        reply = server_object.greetings(f"{name}:{mydata}")


if __name__ == '__main__':
    name = sys.argv[1]
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()

    object = bus.get_object("org.example.demo.test", "/org/example/demo/test")

    object.connect_to_signal(
        "mySignal", user_return_signal, dbus_interface="org.example.demo.test")

    in_th = Thread(target=user_input_method)
    in_th.start()
    loop.run()

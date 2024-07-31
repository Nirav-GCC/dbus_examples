#!/usr/bin/env python3
from errno import ESTALE
from socket import send_fds
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


def get_msg(name, msg):
    if(name != input_name):
        print(name, msg)


def send_msg():
    value = True
    global input_name
    input_name = input("enter name :")

    while (value):
        msg = input("")
        reply = server_object.greetings(input_name, msg)
    return True


if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()

    object = bus.get_object("org.example.demo.test", "/org/example/demo/test")

    object.connect_to_signal(
        "mySignal", get_msg, dbus_interface="org.example.demo.test")

    in_th = Thread(target=send_msg)
    in_th.start()
    loop.run()

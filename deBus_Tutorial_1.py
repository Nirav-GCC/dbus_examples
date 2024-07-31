# import dbus
# def get_song_info(player):
#     if player == "mpd":
#         from mpd import MPDClient
#         client = MPDClient()
#         client.connect("localhost", 6600)
#         song_info = client.currentsong()
#         return song_info["artist"], song_info["title"]
#     else:
#         bus = dbus.SessionBus()
#         try:
#             proxy = bus.get_object("org.mpris.MediaPlayer2.%s" % player,
#                                    "/org/mpris/MediaPlayer2")
#         except dbus.exceptions.DBusException:
#             print("[ERROR] Player \"%s\" doesn't exist or isn't playing" \
#                   % player)
#             return

#         interface = dbus.Interface(
#             proxy, dbus_interface="org.freedesktop.DBus.Properties"
#         )
#         properties = interface.GetAll("org.mpris.MediaPlayer2.Player")
#         metadata = properties["Metadata"]
#         artist = str(metadata["xesam:artist"][0])
#         title = str(metadata["xesam:title"])
#         return artist, title 

# import dbus

# bus = dbus.SystemBus()
# hal_manager_object = bus.get_object('org.freedesktop.Hal', '/org/freedesktop/Hal/Manager')
# hal_manager_interface = dbus.Interface(hal_manager_object, 'org.freedesktop.Hal.Manager')

# # calling method upon interface
# print(hal_manager_interface.GetAllDevices())

# # accessing a method through 'get_dbus_method' through proxy object by specifying interface
# method = hal_manager_object.get_dbus_method('GetAllDevices', 'org.freedesktop.Hal.Manager')
# print(method())

# # calling method upon proxy object by specifying the interface to use
# print( hal_manager_object.GetAllDevices(dbus_interface='org.freedesktop.Hal.Manager'))

# myservice.py
# simple python-dbus service that exposes 1 method called hello()

import gtk
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop

class MyDBUSService(dbus.service.Object):
    def __init__(self):
        bus_name = dbus.service.BusName('org.frankhale.helloservice', bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/org/frankhale/helloservice')

    @dbus.service.method('org.frankhale.helloservice')
    def hello(self):
        return "Hello,World!"

DBusGMainLoop(set_as_default=True)
myservice = MyDBUSService()
gtk.main()

#######################

# consumeservice.py
# consumes a method in a service on the dbus

import dbus

bus = dbus.SessionBus()
helloservice = bus.get_object('org.frankhale.helloservice', '/org/frankhale/helloservice')
hello = helloservice.get_dbus_method('hello', 'org.frankhale.helloservice')
print(hello())
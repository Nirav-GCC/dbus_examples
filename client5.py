import time
import dbus
from gi.repository import GLib
import sys
import dbus.service

bus = dbus.SessionBus()
BUS = "org.example.demo.test"
server_object = bus.get_object(BUS,"/org/example/demo/test")

# Proxy = bus.get_object('BUS', '/org/fedoraproject/FirewallD1')
# Proxy.Get('org.fedoraproject.FirewallD1', 'state', dbus_interface='org.freedesktop.DBus.Properties')
loop = GLib.MainLoop()
INTERVAL = 2

def make_method_call_client():
    print("Sending Method Call: get_time_stamp")
    reply = server_object.get_time_stamp()
    print("Returned data is of type: {}".format(type(reply)))
    print("Time stamp received from server: {}".format(reply))
    #print(time.localtime( time.time() ))
    return True

if __name__=="__main__":
    print("Starting Client Demo 5...")
    GLib.timeout_add_seconds(interval=INTERVAL,
                             function=make_method_call_client)
    loop.run()


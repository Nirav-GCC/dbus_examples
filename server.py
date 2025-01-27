import sys
if int(sys.version[0]) < 3: sys.exit("Please use python 3. Exiting...")

# Importing...
from pydbus import SessionBus  # SystemBus
from gi.repository import GLib

# Variables / Constants / Instantiation...
bus = SessionBus()  # SystemBus
BUS = "org.example.demo.test"
loop = GLib.MainLoop()
message_count = 0


class DBusService_XML():
    """
    DBus Service XML definition. 
    type="i" for integer, "s" string, "d" double, "as" list of string data.
    """
    dbus = """
    <node>
        <interface name="{}">
            <method name="server_no_args">
            </method>
        </interface>
    </node>
    """.format(BUS)

    def server_no_args(self):
        "No arguments over the dbus. Server produces a message on the console."
        global message_count
        print("This is message {}".format(message_count))
        message_count +=1
        return

if __name__ == "__main__":
    print("Starting Server Demo 1...")
    bus.publish(BUS, DBusService_XML())
    loop.run()
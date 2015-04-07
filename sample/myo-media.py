import sys
import dbus
sys.path.append('../lib/')

from myo import Myo
from device_listener import DeviceListener
from pose_type import PoseType

bus = dbus.SessionBus()
obj = bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
interface = dbus.Interface(obj, "org.mpris.MediaPlayer2.Player")

class ActionHandler(DeviceListener):
    def on_pose(self, pose):
            if pose == PoseType.DOUBLE_TAP:
                    print("Play/Pause")
                    reply = interface.PlayPause()
            elif pose == PoseType.FINGERS_SPREAD:
                    print("Next")
                    reply = interface.Next()
            elif pose == PoseType.FIST:
                    print("Prev")
                    reply = interface.Previous()

def main():
    print('Start Myo for Linux')

    listener = ActionHandler()
    myo = Myo()

    try:
        myo.connect()
        myo.add_listener(listener)

        while True:
            myo.run()

    except KeyboardInterrupt:
        pass
    except ValueError as ex:
        print(ex)
    finally:
        myo.safely_disconnect()
        print('Finished.')

if __name__ == '__main__':
    main()
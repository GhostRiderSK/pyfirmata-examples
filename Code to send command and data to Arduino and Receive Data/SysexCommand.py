from pyfirmata import pyfirmata,ArduinoNano,util
import time
# check line number 490 in StandardFirmata_edited.ino file , for the code we have edited
board=ArduinoNano('COM3')
iter = util.Iterator(board)
iter.start()
time.sleep(1)
def receive(*args, **kwargs):
    print(args)
    print(kwargs)
board.add_cmd_handler(0x02,receive)
board.send_sysex(0x01,[0x06,0x05,0x11,0x02,0x06])
while 1:
    pass

	#print util.two_byte_iter_to_str(args)


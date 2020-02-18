from pyfirmata import pyfirmata,ArduinoNano,util
import time
board=ArduinoNano('COM3')
iter = util.Iterator(board)
iter.start()
def receive(*args, **kwargs):
    print(args)

board.add_cmd_handler(0x03,receive)
while True:
    time.sleep(1)
    board.send_sysex(0x03, [0x02, 0x03,0xFF])  # Values can be send upto 0 - 255 , it is then received as two bytes

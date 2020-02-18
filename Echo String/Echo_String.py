import time

import pyfirmata
from pyfirmata import Arduino, util


def main():
    board = Arduino('COM3')
    board.add_cmd_handler(pyfirmata.pyfirmata.STRING_DATA, on_string_received)

    iter = util.Iterator(board)
    iter.start()


    write_loop(board)




def write_loop(board):


    i = 0

    while True:

        message = util.str_to_two_byte_iter("Hi This is GhostRider")  # Converting String two midi format, 1 character of this string is as two bytes
        #message = "Hello yo"
        board.send_sysex(pyfirmata.pyfirmata.STRING_DATA, message)   # first argument is command and the secon is the data
        time.sleep(0.5)
        i=i+1
        print(i)


def on_string_received(*args, **kwargs):
    print(util.two_byte_iter_to_str(args))  # converts the incoming 2 byte data to character and then forms String
    #print(kwargs)

    # print util.two_byte_iter_to_str(args)



if __name__ == "__main__":
    main()
#!/usr/bin/env python

import asyncio
import websockets
from websockets.server import serve
import rtmidi
import time
import rtmidi

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

if available_ports:
    midiout.open_port(0)




async def handler(websocket):
    number = 0
    while True:
        if(number>127):
            number = 0
        try:
            message = await websocket.recv()
            note_on = [0x90, number, 112] # channel 1, middle C, velocity 112
            note_off = [0x80, number, 0]
            midiout.send_message(note_on)
            #time.sleep(0.5)
            midiout.send_message(note_off)
            #time.sleep(0.1)
            number = number +1
            available_ports = midiout.get_ports()
            #print(available_ports)
        except websockets.ConnectionClosedOK:
            break
        print(message)

async def main():
    async with serve(handler, "localhost", 8767):
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    # test1.py executed as script
    # do something
    asyncio.run(main())


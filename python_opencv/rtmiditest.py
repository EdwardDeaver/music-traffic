import time
import rtmidi

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

if available_ports:
    midiout.open_port(0)
else:
    midiout.open_virtual_port("My virtual output")

with midiout:
    for i in range(1000):
        for z in range(100):
            note_on = [0x90, z, 112] # channel 1, middle C, velocity 112
            note_off = [0x80, z, 0]
            midiout.send_message(note_on)
            midiout.send_message(note_off)


del midiout
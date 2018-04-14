from math import sin, cos, log, pi
from random import random
from time import time
import sys
from os import system
from struct import pack
from copy import deepcopy
# from pieces import clapping_1 as piece
# from pieces import clapping_2 as piece
from pieces import minimal_1 as piece
# from pieces import self_made_3 as piece
# from pieces import self_made_2 as piece
# from pieces import self_made_1 as piece
# from pieces import Scarborough_Fair as piece
# from pieces import King_of_Thule as piece

make_str = lambda arr : [str(a) for a in arr]

#possible console args:
    # "print", "printh",
    # "print_text", "print_texth",
    # "print_arr", "print_arrh",
    # "play", "playh",
    # "save", "saveh",
    # "note_by_note", "note_by_noteh",
    # "random_title"
#-"h" attached means that the action should be applied to the harmonified piece
args = sys.argv[1:]
print("modes: ("+", ".join(args)+")")

rate = 32000
print("rate: "+str(rate))

zero_freq = 256
print("base_freq: "+str(zero_freq))

#determines the influence of each voice (if several are present) in the summing of frequencies
weight = [2, 2, 2, 1]
# weight = [0, 1, 1, 10, 0]
print("weights for different voices: "+"¦".join(make_str(weight))+"None"*int(len(weight) == 0))

beats_per_bar = piece[0][1]
print("beats per bar: "+str(beats_per_bar))

#shortening for tests: from start_play to stop_play only will be played; measurement in beats
start_play = beats_per_bar*0 #0 bars
# stop_play = beats_per_bar*4
stop_play = len(piece)-1

length_of_a_note = 0.2
bits = 8 #can't currently play other than one-byte files
print("bits: "+str(bits))

# wave = 'sin'
# wave = 'sq'
# wave = 'saw'
wave = 'tri'
print("wave form: "+wave)

if(not 'random_title' in args):
    title = (
        piece[0][0]
        +"-r["+str(rate)+"]"
        +"-w["+"¦".join(make_str(weight))+"]"
        +"-p["+str(start_play)+"-"+str(stop_play)+"]"
        +"-l["+str(length_of_a_note)+"]"
        +"-f["+str(zero_freq)+"]"
        +"-b["+str(bits)+"]"
        +"-W["+wave+"]"
        +"-h"*("playh" in args or "saveh" in args)
    )
else:
    title = str(random())[:10]+"-r["+str(rate)+"]"
print("title: "+str(title))
piece = piece[1:]

print("summed beats: "+str(len(piece)))
print("summed bars: "+str(int(len(piece)/beats_per_bar+0.9999999))) #ceil
print("length of a note: "+str(length_of_a_note)+" s")

# exit(0)

def ext(f, t, wave=wave): #extension of the speaker diaphram
    if(wave == 'saw'):
        return (f*t*1)%1
    elif(wave == 'tri'):
        return abs(1-(f*t*2)%2)
    elif(wave == 'sq'):
        return int((f*t)%1 >= 0.5)
    elif(wave == 'sin'):
        return -cos(f*t*2*pi)*0.5+0.5
    else:
        # return -cos(f*t*6.28)*0.5+0.5
        return 0
# print('\n'.join(['.'*int(ext(220, t*0.0001)*20) for t in range(0, 100)]))
# exit()

# convering from a tone
# (like [0, 6, 12] = [base_note, base_note+tritone, base_note+octave])
# to frequencies ([base_freq, base_freq * sqrt(2), base_freq * 2])
f = lambda T : zero_freq * 2**(T/12)
l2 = log(2)
Tfactors = [ #taylor by Wolfram alpha
    zero_freq,
    zero_freq/4/    3 * l2,
    zero_freq/8/   36 * l2**2,
    zero_freq/8/ 1296 * l2**3,
    zero_freq/8/62208 * l2**4
]
Tf = lambda T : (Tfactors[0] + sum([(pow(T, k) * Tfactors[k]) for k in range(1, 5)]))

#test the quality of Tf against f (wich is probably slowe than Tf)
# from matplotlib import pyplot as plt
# plt.plot([(f(T/10)) for T in range(-120, 240)])
# plt.plot([(Tf(T/10)) for T in range(-120, 240)])
# plt.show()
# input()
freq = Tf #choosing which function will be used in the latter program
# exit(0)

def isint(n):
    try:    return int(n)==n
    except: return False

#function for flattening a 2D-list
flatten = lambda l: [item for sublist in l for item in sublist] #https://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python

def print_piece(piece=piece, connected=True):
    from matplotlib import pyplot as plt
    t = 0
    presult = []
    result = "\n"
    harmonified = harmonify(piece)
    if("print_text" in args or "print_texth" in args):
        if("print_texth" in args): printed = harmonified
        else:                      printed = piece
        filtered = list(filter(lambda x : isint(x), flatten(printed)))
        minimum = min(filtered)
        maximum = max(filtered)
        for chord in printed:
            row = " "*(maximum - minimum+1)
            for note in chord:
                char = '#'
                char = '0123456789X€'[note%12]
                row = row[:note-minimum]+char+row[note-minimum+1:]
            presult += [row]
            t += 1
        for col in range(maximum - minimum, -1, -1):
            for row in range(min(len(presult), 180)):
                result += presult[row][col]
                if(row%beats_per_bar == beats_per_bar-1):
                    result += "|"
            result += "#"*int(printed.count(col)/len(piece)*100)+"\n"
        print(result) #does not return the strings that show the music in text format (using '#' in a specific column to indicate a note)
    if("print" in args or "printh" in args):
        if("printh" in args): plotted = harmonified
        else:                 plotted = piece
        filtered = list(filter(lambda x : isint(x), flatten(plotted)))
        minimum = min(filtered)
        maximum = max(filtered)
        for n in range(max([len(chord) for chord in plotted])):
            pieces = []
            for c in range(len(plotted)):
                try:
                    pieces += [plotted[c][n]-(0.2)*(n%6)]*5
                except:
                    pieces += [None]*5
            if(connected):
                plt.plot(pieces, 'brcgmy'[n%6]+'')
            plt.plot(pieces, 'brcgmy'[n%6]+'o')
        plt.axis([0, len(plotted)*5, minimum-2, maximum+2])
        plt.ion()
        plt.show()

printing_interval = 1
BYTES = bytearray()
def play_piece(
    piece=piece,
    dt = 1/rate, #resolution of time
    l = length_of_a_note, #length of one note
    # variation = [-1, 5, 0, -1, 0, 0]
    variation = [0]
):
    # global STRING
    global BYTES
    max = l/len(variation)
    t = 0 #time = dt * ct
    ct = 0 #counter of notes played / of timesteps
    time0 = time()

    for c in range(start_play, stop_play):
        try:
            chord = piece[c]
        except:
            break
        for add in variation:
            while t < max:
                E = []
                # if(chord == [None]):
                #     E = [0]
                for n in range(len(chord[:])): #chord[:-1] if variation is used, but then add the "E += [ext(t, freq(chord[-1]+add))]*2" after the loop (where it is commented out)
                    try:
                        for k in range(weight[n]):
                            E += [ext(freq(chord[n]), t)]
                    except IndexError:
                        E += [ext(freq(chord[n]), t)]
                # E += [ext(freq(chord[-1]+add), t)]*2
                e = sum(E)/(len(E)+1)*2**bits
                # STRING += chr(int(e))
                BYTES += pack("I", int(e))[:int(bits/8)] #resolving multi-byte-numbers (anything greater than 8 bits = 256)
                ct += 1
                t = ct * dt
            max += l/len(variation)
        percent_done = (c - start_play) / len(piece) * 100 + printing_interval
        prev_percent_done = (c-1) / len(piece) * 100
        pd = percent_done
        ppd = prev_percent_done
        pi = printing_interval
        if(int(ppd/pi) < int(pd/pi)):
            system(
                "echo \"\r\033[A\033[K" #moving in the above line and clearing it (see sources below)
                +"["+"#"*int(pd/pi)+"-"*int(100/pi - int(pd/pi))+"] " #printing a bar that fills
                +str(int(pd/pi)*pi)+'% of chords processed' #printing the percentage
            +"\"")
            #sources:  https://en.wikipedia.org/wiki/ANSI_escape_code and https://stackoverflow.com/questions/2388090/how-to-delete-and-replace-last-line-in-the-terminal-using-bash
    print('processed in '+str(round(time()-time0, 3))+'s')

def modify_for_terminal(name, maske="[\"]\\|", filter=""):
    result = ""
    for c in name:
        if(c in filter):
            continue
        if(c in maske):
            result += "\\"
        result += c
    return result

def save_to_file(file_name, piece=piece):
    play_piece(piece)
    file_name = file_name+'.sound.string'
    try:
        file = open(file_name, 'bx')
    except FileExistsError:
        file = open(file_name, 'bw')
    # BYTES = bytearray(STRING, 'ascii')
    file.write(BYTES)
    file.close()
    print("Saved to file "+file_name)
    return file_name

def brute_sort(arr):
    result = []
    while arr:
        result += [min(arr)]*arr.count(min(arr))
        arr = list(filter(lambda x : x!=result[-1], arr))
    return result

def harmonify(piece, K=[0, 1]):
    result = []
    for chord in piece:
        new_chord = []
        for note in chord:
            if(not note%12 in new_chord):
                new_chord += [note%12+12*k for k in K]
        result += [brute_sort(new_chord)]
    return result

if("print_arr" in args):
    print(piece)
if("print_arrh" in args):
    print(harmonify(piece, K=[0]))
if("print" in args or "print_text" in args or "printh" in args or "print_texth" in args):
    print_piece()
    input("[ENTER] to  proceed")
if(("save" in args or "play" in args or "saveh" in args or "playh" in args) and not ("note_by_note" in args or "note_by_noteh" in args)):
    if("playh" in args):
        piece = harmonify(piece)
    file_name = save_to_file(file_name=title)
if("note_by_note" in args or "note_by_noteh" in args):
    if("note_by_noteh" in args):
        piece = harmonify(piece)
    for i in range(len(piece)):
        BYTES = bytearray()
        # file_name = "!"+" "*(4-len(bin(i)[2:]))+"".join([" #"[int(b, 2)] for b in bin(i)[2:]])+"!"
        file_name = title+"_"+str(i)+"of"+str(len(piece))
        file_name = save_to_file(file_name=file_name, piece=[piece[i]])
        if("play" in args or "playh" in args):
            system("aplay \""+modify_for_terminal(file_name)+"\" -r "+str(rate))
        #an example for how to output a long row of .sound.string files: terminal
        #for i in {0..15}; do aplay "clapping_2-r[128000]-w[]-p[0-16]-l[0.05]-f[256]-b[8]-W[tri]_"$i"of16.sound.string" -r128; done
if(("play" in args or "playh" in args) and not ("note_by_note" in args or "note_by_noteh" in args)):
    from os import system
    system("aplay "+modify_for_terminal(file_name)+" -r "+str(rate))

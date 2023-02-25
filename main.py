# Bruteforce password unlocker (4-digit)
import random as rand
import sys
import time
import pynput as inp

# Get the virtual kb
kb = inp.keyboard.Controller()

# Key Atlas
ENTER = inp.keyboard.Key(inp.keyboard.Key.enter)

# Declare const
TTS = 3     # Time before bruteforce starts
dig: int


def max_pass(pwr: int):
    total = 0
    pwr -= 1
    while pwr >= 0:
        total += 9*(10 ** pwr)
        pwr -= 1
    return total


def pin_format(num: int):
    frm = str(num)
    while len(frm) < dig:
        frm = '0' + frm
    return frm


def try_pin(pin: str):
    pin_inputs = [c for c in pin]    # Unpack and separate all digits
    for digit in pin_inputs:
        kb.tap(digit)
    # kb.tap(key=ENTER)  # WARNING: Disable to test or android phones


def start_seq():
    i = TTS   # Time to start
    while i != 0:
        sys.stdout.write("\rStarting in " + str(i))
        time.sleep(1)
        i -= 1


print("██████╗░██████╗░██╗░░░██╗████████╗███████╗███████╗░█████╗░██████╗░░█████╗░███████╗\n"
      "██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝\n"
      "██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░█████╗░░██║░░██║██████╔╝██║░░╚═╝█████╗░░\n"
      "██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░██╔══╝░░██║░░██║██╔══██╗██║░░██╗██╔══╝░░\n"
      "██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗██║░░░░░╚█████╔╝██║░░██║╚█████╔╝███████╗\n"
      "╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░╚════╝░╚══════╝")
currN = 0
print("Welcome to bruteforce. Insert number of digits to crack")
dig = int(input())

# Random Number generator tester
max_n = max_pass(dig)
print("Max Code N: " + str(max_n))
n = rand.randint(0, max_n)
print("Password: " + str(n))
# Random Number generator tester

start_seq()     # Wait TTS secs to start, remove if needed

while currN != n:   # Change cond to sensor correct input recieved
    sys.stdout.write("\rTrying " + str(currN) + "...")
    try_pin(pin_format(currN))   # Input pin
    currN += 1
    time.sleep(0.0001)  # WARNING: Only for testing. Remove later
print("\n\nSucessfully Cracked: " + str(currN))

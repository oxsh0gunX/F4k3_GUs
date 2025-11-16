import random
import os
import sys
import time

def dramatic(text, delay=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def simulate_delete():
    files = os.listdir(".")
    dramatic("\n⚠️ SYSTEM FAILURE DETECTED!")
    dramatic("Initiating file purge in current directory...\n", delay=0.05)

    for f in files:
        dramatic(f"Deleting: {f}", delay=0.02)
        time.sleep(0.1)

    dramatic("\n💀 BOOTLOADER ERASED! (simulation)")

def game():
    number = random.randint(1, 10)
    dramatic("Welcome to the Dangerous Guess Game! ")
    dramatic("Cr3at3d b7 oxsh0gunX")
    dramatic("Guess the number (1–10) or watch your system burn .")

    try:
        guess = int(input("\nYour guess: "))
    except ValueError:
        dramatic("Not a number! SYSTEM EXPLODING…")
        simulate_delete()
        return

    if guess == number:
        dramatic("\n Correct guess! System safe.")
    else:
        dramatic("\n Wrong guess!")
        simulate_delete()

if __name__ == "__main__":
    game()

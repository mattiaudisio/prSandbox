import time
from playsound import playsound


def countdown(timer):
    print("*** ALLENATI ***")
    while timer:
        time.sleep(1)
        timer -= 1
    playsound("src/audio/Start.mp3")


def pausa(timer):
    print("*** PAUSA ***")
    while timer:
        time.sleep(1)
        timer -= 1
    playsound("src/audio/Pause.mp3")


print("=== ALLENAMENTO ===\n1) Skip alto\n2) Squat Jump\n3) Affondi con salto\n4)Jumping Jacks\n5) "
      "Climbers\n6)Burpees\n")
inizio = str(input("Inizio (S,N):"))
if inizio == 'S':
    i = 0
    pausa(10)
    while i < 24:
        countdown(20)
        pausa(10)
        i = i + 1

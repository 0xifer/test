import pyautogui
import pydirectinput as pg
from time import sleep

#presets
timer = 10
seq_num = 0
chat_button = input('\n\nWELCOME TO A LIL CHEAT I MADE\n\n[Highlife = "t"]\nButton to open chat / type in chat: ').lower()
chat_text = input('\n[Highlife = "/mask"]\nCommand/Text to use: ').lower()
loop_amount = int(input('\n[Highlife = "2"]\nDo this how many times for each sequence?: '))
command_delay = int(input('\n[Highlife = "1"]\nEnter the delay for how long to wait between typing "' + chat_button + '" and "' + chat_text + '"\nSeconds: '))
wait_time = int(input('\n[Highlife = "300"]\nEnter the time to wait between each sequence\nEx. Entering "60" will wait 60 seconds before doing "' + chat_text + '" ' + str(loop_amount) + ' time(s)\nSeconds: '))

print('\n\nLoad into GTA now and wait')
while timer > 0:
    print('\n\nStarting in ' + str(timer) + ' second(s)')
    sleep(1)
    timer = timer - 1

print('Loading now...')
pg.PAUSE = command_delay

def typer():
    LoopsLeft = loop_amount
    while LoopsLeft > 0:
        pg.typewrite(chat_button)
        pg.typewrite(chat_text)
        pg.press('enter')
        LoopsLeft = LoopsLeft - 1

while 1 == 1:
    seq_num = seq_num + 1
    print('\n==========================\nSequence #' + str(seq_num) + '\n==========================')
    typer()
    timer = wait_time
    print('Sequence #' + str(seq_num) + ' complete')
    while timer > 0:
        print('Waiting ' + str(timer) + ' more second(s)')
        sleep(1)
        timer = timer - 1

# Created by Xpirement#7005

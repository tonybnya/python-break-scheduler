#!/usr/bin/env python3
# break_scheduler.py - Break Scheduler inspired by the Pomodoro Technic.

'''
Here's how Pomodoro Technic works.
Note: 25-minutes work period (5 minutes short break) is called a "Pomodoro".

1. Work intensely for 25 minutes (set a timer) - no phones, social media...
2. Take a short break (5 minutes).
3. Work intensely for 25 minutes (set a timer) - no phones, social media...
4. Take a short break (5 minutes).
5. Work intensely for 25 minutes (set a timer) - no phones, social media...
6. Take a short break (5 minutes).
7. Work intensely for 25 minutes (set a timer) - no phones, social media...
8. Take a long break (15 to 45 minutes).
'''

import time
import os
import webbrowser


filename1 = f'file:{os.getcwd()}/short_break.html'
filename2 = f'file:{os.getcwd()}/long_break.html'

BREAKS = ['SHORT BREAK', 'LONG BREAK']
LINE = '+' + '-'*47 + '+'
SPACES = '\t'*2 + '+' + ' '


def countdown(time_, type_):
    '''A countdown function.'''

    duration = int(time_ * 60 / 3600)
    print(LINE)
    print(SPACES + type_ + ' +')
    print(LINE)
    print(f'Countdown of {duration} minute(s).')
    print('\a')
    while time_:
        minutes, seconds = divmod(time_, 60)
        timer = f'{minutes}:{seconds}'
        print(timer, end='\r')
        time.sleep(1)
        time_ -= 1
    print(f'End of {duration} minute(s)!')
    print('\a')
    print(LINE)


def pomodoro():
    '''
    Schedule 25-minutes work period.
    & 5 minutes for a short break.
    '''

    countdown(1500, BREAKS[1])          # 25 minutes = 1500 seconds.
    webbrowser.open(filename1)
    countdown(300, BREAKS[0])           # 5 minutes = 300 seconds.


def main():
    '''Main program.'''

    print('Press ENTER to start Pomodoro Timer.')
    print('Press CTRL-C to stop the program!')

    try:
        for i in range(4):
            input('POMODORO TIMER!!!')
            pomodoro()
            i += 1

        time_ = 15
        print('TIME FOR A LONG BREAK!')
        print(f'{time_} minutes countdown...')
        duration = time_ * 60 / 3600
        webbrowser.open(filename2)
        countdown(duration, BREAKS[1])

    except KeyboardInterrupt:
        print('Pomodoro timer interrupted!')


if __name__ == '__main__':
    main()

import pyautogui as pg
from pynput.keyboard import Key, Listener
import json

from pokemon import Pokemon

HUNTING = ''

DIR = 'sprite/' + HUNTING + '.png'

KEY_SHINY = 'a'
KEY_NORMAL = 'd'
KEY_CENTER = 's'
KEY_SAVE = 'w'
KEY_LOAD = 'q'
KEY_PRINT = 'e'

while not HUNTING:
    HUNTING = input('Insert sprite name (without extension): ')

huntedPkmn = Pokemon(HUNTING)


def getCurrentRGB():
    x, y = pg.position()
    screen = pg.screenshot()
    rgb = screen.getpixel((x, y))
    return rgb


def on_press(key):
    try:
        # Set shiny sprite color
        if key.char == KEY_SHINY:
            rgb = getCurrentRGB()
            huntedPkmn.setSpriteColor(rgb, True)
            print('[BOT - sprite] *shiny* color set to ' + str(rgb))
        # Set normal sprite color
        if key.char == KEY_NORMAL:
            rgb = getCurrentRGB()
            huntedPkmn.setSpriteColor(rgb, False)
            print('[BOT - sprite] normal color set to ' + str(rgb))
        # Center mouse on the sprite
        if key.char == KEY_CENTER:
            try:
                img = pg.locateOnScreen(DIR, confidence=0.9)
                if img:
                    pg.moveTo(pg.center(img))
                    print('[BOT - sprite] mouse set on ' + str(img))
                    print('[BOT - sprite] color detected: '
                          + str(getCurrentRGB()))
                else:
                    print('[BOT - sprite] sprite not found . . .')
            except OSError:
                print(
                    "[BOT - sprite] invalid sprite directory - can't find ./sprite/" + HUNTING + ".png")
                print('[BOT - option] shutting down . . .')
                return False
        # Save object
        if key.char == KEY_SAVE:
            dirJson = 'huntings/' + huntedPkmn.getName() + '.txt'
            with open(dirJson, 'w') as outfile:
                print('[BOT - options] saving . . .')
                json.dump(huntedPkmn.__dict__, outfile)
                print('[BOT - options] saved in ' + dirJson)
        # Load object
        if key.char == KEY_LOAD:
            try:
                print('[BOT - options] loading . . .')
                dirJson = 'huntings/' + huntedPkmn.getName() + '.txt'
                file = open(dirJson)
                data = json.load(file)
                huntedPkmn.setName(data["name"])
                huntedPkmn.setSpriteColors(data["spriteColors"])
                print('[BOT - options] loaded')
            except FileNotFoundError:
                print(
                    "[BOT - option] invalid file directory - can't find ./huntings/" + HUNTING + ".txt")
                print('[BOT - option] shutting down . . .')
                return False
        # Print object
        if key.char == KEY_PRINT:
            print('[BOT - options] printing . . .')
            print(huntedPkmn.__dict__)
    except AttributeError:
        pass


def on_release(key):
    # Shut down
    if key == Key.esc:
        print('[BOT - option] shutting down . . .')
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

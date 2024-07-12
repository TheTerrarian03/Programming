import pygame
import PygameFunctions as PF
import Variables as v
import start

start.main()
PF.create_screen()


def show_help():
    print("Commands:\n"
          "help - shows this diologue\n"
          "clear - clears board\n"
          "clear(startX,startY,endX,endY) - clears a certain area, defined by user.\n"
          "fill - fills entire board\n"
          "fill(startX,startY,endX,endY) - fill a certain area, defined by user.\n"
          "")


show_help()

while v.GlobalRunning:
    user_command = input("Enter command: ")

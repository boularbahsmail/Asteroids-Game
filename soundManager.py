
import pygame
import sys
import os
import random
from pygame.locals import *

sounds = {}  # create empty dictionary of sounds


def initSoundManager():
    pygame.mixer.init()
    sounds["fire"] = pygame.mixer.Sound("../res/FIRE.WAV")
    sounds["explode1"] = pygame.mixer.Sound("../res/EXPLODE1.WAV")
    sounds["explode2"] = pygame.mixer.Sound("../res/EXPLODE2.WAV")
    sounds["explode3"] = pygame.mixer.Sound("../res/EXPLODE3.WAV")
    sounds["lsaucer"] = pygame.mixer.Sound("../res/LSAUCER.WAV")
    sounds["ssaucer"] = pygame.mixer.Sound("../res/SSAUCER.WAV")
    sounds["thrust"] = pygame.mixer.Sound("../res/THRUST.WAV")
    sounds["sfire"] = pygame.mixer.Sound("../res/SFIRE.WAV")
    sounds["extralife"] = pygame.mixer.Sound("../res/LIFE.WAV")


def playSound(soundName):
    channel = sounds[soundName].play()


def playSoundContinuous(soundName):
    channel = sounds[soundName].play(-1)


def stopSound(soundName):
    channel = sounds[soundName].stop()

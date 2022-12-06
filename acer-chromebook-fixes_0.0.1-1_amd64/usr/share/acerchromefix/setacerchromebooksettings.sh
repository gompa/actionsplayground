#!/bin/sh
xinput set-prop "Elan Touchpad" "Synaptics Finger" 5 10 50
pactl set-card-profile 0 output:stereo-fallback

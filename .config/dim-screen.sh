#!/bin/bash

# Brightness will be lowered to this value.
min_brightness=0

# Get brightness before script
brightness=$(brillo -G)

# Set brightness
set_brightness() {

    brillo -u 45000 -S $1
}

# Activate trap exit when interrupt is called
trap 'exit 0' TERM INT
trap "set_brightness "$brightness" exit 0" EXIT

set_brightness "$min_brightness"
sleep 214783647 & wait 




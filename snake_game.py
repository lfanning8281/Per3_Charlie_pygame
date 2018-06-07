from gpiozero import Button
button_right = Button(2)
button_left = Button(18)
button_down = Button(25)
button_up = Button(8)


while True:
    if button_right.is_pressed:
        print('turn right')
    elif button_left.is_pressed:
        print('turn left')
    elif button_down.is_pressed:
        print('turn down')
    elif button_up.is_pressed:
        print('turn up')
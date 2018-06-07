from gpiozero import Button
button_right = Button(2)
button_left = Button(18)
button_down = Button(25)
button_up = Button(8)



        
def is_right_button_pressed():
    if button_right.is_pressed:
        return "right"
def is_left_button_pressed():
    if button_left.is_pressed:
        return "left"
def is_down_button_pressed():
    if button_down.is_pressed:
        return "down"
def is_up_button_pressed():
    if button_up.is_pressed:
        return "up"
if __name__ == '__main__':
    while True:
        is_right_button_pressed()
        is_left_button_pressed()
        is_down_button_pressed()
is_up_button_pressed()

import mouse
import keyboard
from time import sleep

mouse_movement_displacement = 2
d_time = 0.01
mouse_movement_speed_up = 5
while True:
    if keyboard.is_pressed('d+f'):
        while not keyboard.is_pressed('a+s'):
            # RIGHT
            # FAST
            if keyboard.is_pressed('shift+h'):
                mouse.move(-mouse_movement_displacement*mouse_movement_speed_up, 0, absolute=False)
            # SLOW
            elif keyboard.is_pressed('h'):
                mouse.move(-mouse_movement_displacement, 0, absolute=False)

            # LEFT
            # FAST
            if keyboard.is_pressed('shift+l'):
                mouse.move(mouse_movement_displacement*mouse_movement_speed_up, 0, absolute=False)
            # SLOW
            elif keyboard.is_pressed('l'):
                mouse.move(mouse_movement_displacement, 0, absolute=False)

            # DOWN
            # FAST
            if keyboard.is_pressed('shift+j'):
                mouse.move(0, mouse_movement_displacement*mouse_movement_speed_up, absolute=False)
            # SLOW
            elif keyboard.is_pressed('j'):
                mouse.move(0, mouse_movement_displacement, absolute=False)

            # UP
            # FAST
            if keyboard.is_pressed('shift+k'):
                mouse.move(0, -mouse_movement_displacement*mouse_movement_speed_up, absolute=False)
            # SLOW
            elif keyboard.is_pressed('k'):
                mouse.move(0, -mouse_movement_displacement, absolute=False)

            # CLICK LEFT
            if keyboard.is_pressed('p'):
                mouse.click()

            scroll_speed_up = 1
            scroll_displacement = 1
            # SCROLL DOWN
            if keyboard.is_pressed('n'):
                mouse.wheel(-scroll_displacement)

            # SCROLL UP
            if keyboard.is_pressed('m'):
                mouse.wheel(scroll_displacement)

            # return control to other applications for a while
            sleep(d_time)

    sleep(0.1)

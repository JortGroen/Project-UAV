#!/usr/bin/env python

# Copyright (c) 2011 Bastian Venthur
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.



"""Demo app for the AR.Drone.
dawsdw
This simple application allows to control the drone and see the drone's video
stream.
"""


import pygame
import libardrone
gem = 0
i = 0

def main():
    pygame.init()
    W, H = 320, 240
    screen = pygame.display.set_mode((W, H))
    drone = libardrone.ARDrone()
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                drone.hover()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    drone.reset()
                    running = False
                # takeoff / land
                elif event.key == pygame.K_RETURN:
                    drone.takeoff()
                elif event.key == pygame.K_SPACE:
                    drone.land()
                # emergency
                elif event.key == pygame.K_BACKSPACE:
                    drone.reset()
                # forward / backward
                elif event.key == pygame.K_w: # TODO while maken die gaat lopen als de toets ingedrukt is. Tijd toevoegen, staat in timer.py in dezelfde map
                    drone.move_forward()
                    vx = drone.navdata.get(0, dict()).get('vx', 1)
                    global gem, i
                    gem += vx
                    print gem
                    i += 1
                elif event.key == pygame.K_s:
                    drone.move_backward()
                # left / right
                elif event.key == pygame.K_a:
                    drone.move_left()
                elif event.key == pygame.K_d:
                    drone.move_right()
                # up / down
                elif event.key == pygame.K_UP:
                    drone.move_up()
                elif event.key == pygame.K_DOWN:
                    drone.move_down()
                # turn left / turn right
                elif event.key == pygame.K_LEFT:
                    drone.turn_left()
                elif event.key == pygame.K_RIGHT:
                    drone.turn_right()
                # speed
                elif event.key == pygame.K_1:
                    drone.speed = 0.1
                elif event.key == pygame.K_2:
                    drone.speed = 0.2
                elif event.key == pygame.K_3:
                    drone.speed = 0.3
                elif event.key == pygame.K_4:
                    drone.speed = 0.4
                elif event.key == pygame.K_5:
                    drone.speed = 0.5
                elif event.key == pygame.K_6:
                    drone.speed = 0.6
                elif event.key == pygame.K_7:
                    drone.speed = 0.7
                elif event.key == pygame.K_8:
                    drone.speed = 0.8
                elif event.key == pygame.K_9:
                    drone.speed = 0.9
                elif event.key == pygame.K_0:
                    drone.speed = 1.0

        try:
            #surface = pygame.image.fromstring(drone.image, (W, H), 'RGB')
            # battery status
            hud_color = (255, 0, 0) if drone.navdata.get('drone_state', dict()).get('emergency_mask', 1) else (10, 255, 10)
            bat = drone.navdata.get(0, dict()).get('battery', 0)
            vx = drone.navdata.get(0, dict()).get('vx', 1)
            vy = drone.navdata.get(0, dict()).get('vy', 1)
            altitude = drone.navdata.get(0, dict()).get('altitude', 1)
            theta = drone.navdata.get(0, dict()).get('theta', 1)
            phi = drone.navdata.get(0, dict()).get('phi', 1)
            psi = drone.navdata.get(0, dict()).get('psi', 1)
            f = pygame.font.Font(None, 20)
            battery_screen = f.render('Battery: %i%%' % bat, True, hud_color)
            vx_screen = f.render('Vx: %i' % vx, True, hud_color)
            vy_screen = f.render('Vy: %i' % vy, True, hud_color)
            theta_screen = f.render('Pitch: %i' % theta, True, hud_color)
            phi_screen = f.render('Roll: %i' % phi, True, hud_color)
            psi_screen = f.render('Yaw: %i' % psi, True, hud_color)
            altitude_screen = f.render('Altitude: %f mm' % altitude, True, hud_color)
            #screen.blit(surface, (0, 0))
            screen.fill((0,0,0))
            screen.blit(battery_screen, (10, 10))
            screen.blit(vx_screen, (10, 25))
            screen.blit(vy_screen, (10, 40))
            screen.blit(theta_screen, (10, 55)) #hoeken werken, altitude nog niet
            screen.blit(phi_screen, (10, 70))
            screen.blit(psi_screen, (10, 85))
            screen.blit(altitude_screen, (10, 100))

        except:
            pass

        pygame.display.flip()
        clock.tick(50)
        pygame.display.set_caption("FPS: %.2f" % clock.get_fps())


    print "Shutting down...",
    average_speed_x = gem/i
    print "Average speed x", average_speed_x
    drone.halt()
    print "Ok."

if __name__ == '__main__':
    main()


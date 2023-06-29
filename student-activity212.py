import glob
import os
import sys
import random
import time
import numpy as np
import cv2

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

IM_WIDTH = 640
IM_HEIGHT = 480


# Show camera sensor result with raw data, reshape image, show image with opencv
def image(image):
    matrix_representational_data =
    reshape_of_image =
    live_feed_from_camera =
    cv2.imshow("", )
    cv2.waitKey(1)
    return


# camera sensor, width, height and fov
def camera(get_blueprint_of_world):
    camera_sensor =
    camera_sensor.
    camera_sensor.
    camera_sensor.
    return camera_sensor


data = []
actor_list = []
try:
    # Carla world defination which includes carla host, port, set timeout, Initialised carla world and get blueprint library
    client =
    client.
    world =
    get_blueprint_of_world =

    # Defination of car model, spawn point for car, address spawn point to car model, set driving mode as autopilot
    car_model =
    spawn_point =
    dropped_vehicle =
    dropped_vehicle.

    # Define carla simulation camera, location, rotation, forword focus, angle
    simulator_camera_location_rotation =
    simulator_camera_location_rotation.location +=
    simulator_camera_location_rotation.rotation.yaw +=
    simulator_camera_view =
    simulator_camera_view.

    # Define camera sensor, location for sensor, attach camera sensor to car, listen method to show result
    camera_sensor =
    sensor_camera_spawn_point =
    sensor =
    sensor.listen()

    # actor list for sensor and dropped vehicle
    actor_list.
    actor_list.

    # time sleep
    time.
finally:
    print('destroying actors')
    for actor in actor_list:
        actor.destroy()
    print('done.')

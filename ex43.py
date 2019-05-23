from sys import exit
from random import randint
from textwrap import dedent



class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement it enter().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        # assign current_scene in the first iteration the value CentralCorridor() object
        current_scene = self.scene_map.opening_scene()
        # assign last_scene the Finished() object
        last_scene = self.scene_map.next_scene('finished')
        # as long as both don't match do this:
        while current_scene != last_scene:
            # assign next_scene_name the return value of the enter method that has been evoked on current_scene which
            # in the first
            # iteration is CentralCorridor()
            next_scene_name = current_scene.enter()
            # reassign current_scene with the return value of the next_scene method that has been called
            # on the scene_map object
            print (current_scene)
            current_scene = self.scene_map.next_scene(next_scene_name)
            print (current_scene)

            # be sure to print out the last scene

        current_scene.enter()

class Death(Scene):


class CentralCorridor(Scene):


class LaserWeaponArmory(Scene):


class TheBridge(Scene):

class EscapePod(Scene):

class Finished(Scene):

    def enter(self):
        print("You did surprisingly well.")

        return 'finished'


class Map(object):

    scenes = {
    'central_corridor': CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'death': Death(),
    'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

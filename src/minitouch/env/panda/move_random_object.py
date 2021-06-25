from gym import spaces
import glob
import os, inspect
import pybullet as p
import numpy as np
import random
from minitouch.env.panda.panda_haptics import PandaHaptics
from minitouch.env.panda.common.bound_3d import Bound3d
from minitouch.env.panda.common.log_specification import LogSpecification

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
os.sys.path.insert(0, parentdir)
urdfRootPath = currentdir + "/assets/"


class MoveRandomObject(PandaHaptics):

    def __init__(self, min_num_cube=1, max_num_cube=5, min_scale=0.5, max_scale=1, min_mass=5, max_mass=50,
                 randomize_color=True, max_z=0.1, randomize_cube_pos=True, test=False, **kwargs):

        super(MoveRandomObject, self).__init__(**kwargs)
        self.space_limits = Bound3d(0.5, 0.75, -0.20, 0.25, 0, max_z)
        self.objectUid = None
        self.object_file_path = os.path.join(urdfRootPath, "objects/cube/cube.urdf")
        self.object_random_scale_range = (min_scale, max_scale)
        self.mass_range = (min_mass, max_mass)
        self.randomize_color = randomize_color
        self.randomize_cube_pos = randomize_cube_pos
        self.number_of_object_interval = (min_num_cube, max_num_cube)
        self.cube_size = 100
        self.cube_pos_distribution = spaces.Box(
            low=np.array([self.space_limits.x_low + 0.05, self.space_limits.y_low + 0.05, 0.02]),
            high=np.array([self.space_limits.x_high - 0.05, self.space_limits.y_high - 0.05, 0.02]))
        self.default_cube_pos = [0.7, 0, 0.05]
        self._urdfRoot = urdfRootPath
        self.test = test

        self.log_specifications = [
            LogSpecification("haptics", "compute_variance", 1, "variance_haptics"),
            LogSpecification("end_effector_pos", "compute_heat_map_x_y", 10, "end_effector_heatmap", [0.5, 0.95, -0.20, 0.25]),
            LogSpecification("cube_pos", "compute_heat_map_x_y", 10, "cube_pos_heatmap", [0.5, 0.75, -0.20, 0.25]),
            LogSpecification("cube_pos", "compute_variance", 1, "cube_pos_variance")
        ]

        self.last_cube_id = None

    def reset(self):
        state = super().reset()

        self.place_objects()
        return state

    def place_objects(self):
        num_objects = random.randint(self.number_of_object_interval[0], self.number_of_object_interval[1])
        for i in range(0, num_objects):
            random_object_scale = random.uniform(self.object_random_scale_range[0], self.object_random_scale_range[1])
            if self.randomize_cube_pos:
                new_cube_pos = self.cube_pos_distribution.sample()
            else:
                new_cube_pos = self.default_cube_pos

            random_object_path = self._get_random_object(num_objects=1)[0]

            self.objectUid = p.loadURDF(random_object_path, basePosition=new_cube_pos,
                                        globalScaling=random_object_scale)

            self.last_cube_id = self.objectUid

            if self.randomize_color:
                p.changeVisualShape(self.objectUid, -1,
                                rgbaColor=[random.uniform(0, 1), random.uniform(0, 1), random.randint(0, 1), 1])

            p.changeDynamics(self.objectUid, -1, random.uniform(self.mass_range[0], self.mass_range[1])
                             )

    def get_object_pos(self):
        return p.getBasePositionAndOrientation(self.last_cube_id)[0]

    def _get_info(self):
        return {"haptics": self._get_haptics(), "cube_pos": self.get_object_pos(),
                "fingers_pos": self.get_fingers_pos(), "end_effector_pos": self.get_end_effector_pos()}

    def _get_random_object(self, num_objects):
        """
        Randomly choose an object urdf from the random_urdfs directory.
        Args:
          num_objects:
            Number of graspable objects.
        Returns:
          A list of urdf filenames.
        """
        if self.test:
          urdf_pattern = os.path.join(self._urdfRoot, 'objects/random_urdfs/*0/*.urdf')
        else:
          urdf_pattern = os.path.join(self._urdfRoot, 'objects/random_urdfs/*[1-9]/*.urdf')

        found_object_directories = glob.glob(urdf_pattern)
        total_num_objects = len(found_object_directories)
        selected_objects = np.random.choice(np.arange(total_num_objects), num_objects)
        selected_objects_filenames = []
        for object_index in selected_objects:
          selected_objects_filenames += [found_object_directories[object_index]]
        return selected_objects_filenames
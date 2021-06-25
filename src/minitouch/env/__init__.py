import gym


gym.envs.register(
    id='Pushing-v0',
    entry_point='minitouch.env.panda.move_cube_easy:MoveCubeEasy',
    max_episode_steps=200,
    kwargs={
        "debug": False,
        "cube_spawn_distance":0.2,
        "sparse_reward_scale": 25,
        "random_side":True,
        "haptics_upper_bound": 50,
        "lf_force": 25,
        "rf_force": 20,
    }
)

gym.envs.register(
    id='PushingDebug-v0',
    entry_point='minitouch.env.panda.move_cube_easy:MoveCubeEasy',
    max_episode_steps=200,
    kwargs={
        "debug": True,
        "cube_spawn_distance":0.2,
        "sparse_reward_scale": 25,
        "random_side":True,
        "haptics_upper_bound": 50,
        "lf_force": 25,
        "rf_force": 20,
    }
)

gym.envs.register(
    id='Playing-v0',
    entry_point='minitouch.env.panda.haptics_exploration_multi:HapticsExplorationMulti',
    max_episode_steps=200,
    kwargs={
        "min_num_cube": 1,
        "max_num_cube": 1,
        "min_scale": 1.1,
        "max_scale": 1.1,
        "min_mass": 50,
        "max_mass": 50,
        "randomize_color": False,
        "randomize_cube_pos": True,
        "max_z": 0.1,
        "haptics_upper_bound": 50,
        "lf_force": 25,
        "rf_force": 20,
    }
)
gym.envs.register(
    id='PlayingDebug-v0',
    entry_point='minitouch.env.panda.haptics_exploration_multi:HapticsExplorationMulti',
    max_episode_steps=200,
    kwargs={
        "min_num_cube": 1,
        "max_num_cube": 1,
        "min_scale": 1.1,
        "max_scale": 1.1,
        "min_mass": 50,
        "max_mass": 50,
        "randomize_color": False,
        "randomize_cube_pos": True,
        "max_z": 0.1,
        "haptics_upper_bound": 50,
        "lf_force": 25,
        "rf_force": 20,
        "debug": True,
    }
)

gym.envs.register(
    id='OpeningDebug-v0',
    entry_point='minitouch.env.panda.door:DoorEnv',
    max_episode_steps=200,
    kwargs={
        "debug": True,
        "discrete_grasp":True,
        "grasp_threshold": 0.4,
        "haptics_upper_bound": 50,
        "lf_force": 25,
        "rf_force": 20,
    }
)

gym.envs.register(
    id='Opening-v0',
    entry_point='minitouch.env.panda.door:DoorEnv',
    max_episode_steps=200,
    kwargs={
        "debug": False,
        "discrete_grasp": True,
        "grasp_threshold": 0.4,
        "threshold_found": 0.58,
        "haptics_upper_bound": 50,
        "lf_force": 25,
        "rf_force": 20,
    }
)

gym.envs.register(
    id='MoveRandomObject-v0',
    entry_point='minitouch.env.panda.move_random_object:MoveRandomObject',
    max_episode_steps=200,
    kwargs={
        "debug": False,
        "min_num_cube": 1,
        "max_num_cube": 1,
        "min_scale": 1.1,
        "max_scale": 1.1,
        "min_mass": 50,
        "max_mass": 50,
        "randomize_color": False,
        "randomize_cube_pos": True,
        "max_z": 0.1,
        "haptics_upper_bound": 50,
        "lf_force": 25,
        "rf_force": 20,

    }
)

gym.envs.register(
    id='MoveRandomObjectTest-v0',
    entry_point='minitouch.env.panda.move_random_object:MoveRandomObject',
    max_episode_steps=200,
    kwargs={
        "debug": False,
        "test": True,
        "min_num_cube": 1,
        "max_num_cube": 1,
        "min_scale": 1.1,
        "max_scale": 1.1,
        "min_mass": 50,
        "max_mass": 50,
        "randomize_color": False,
        "randomize_cube_pos": True,
        "max_z": 0.3,
        "haptics_upper_bound": 50,
        "lf_force": 25,
        "rf_force": 20,

    }
)

gym.envs.register(
    id='MoveRandomObjectDebug-v0',
    entry_point='minitouch.env.panda.move_random_object:MoveRandomObject',
    max_episode_steps=200,
    kwargs={
        "debug": True,
        "test": True,
        "min_num_cube": 1,
        "max_num_cube": 1,
        "min_scale": 1.1,
        "max_scale": 1.1,
        "min_mass": 50,
        "max_mass": 50,
        "randomize_color": False,
        "randomize_cube_pos": True,
        "max_z": 0.3,
        "haptics_upper_bound": 50,
        "lf_force": 25,
        "rf_force": 20,
    }
)

gym.envs.register(
    id='MoveCubeEasyGeneralize-v0',
    entry_point='minitouch.env.panda.move_cube_easy_random:MoveCubeEasyRandom',
    max_episode_steps=200,
    kwargs={
        "debug": False,
        "cube_spawn_distance":0.2,
        "sparse_reward_scale": 25,
        "random_side":True,
        "haptics_upper_bound": 50,
        "lf_force": 25,
        "rf_force": 20,
    }
)

gym.envs.register(
    id='MoveCubeEasyGeneralizeTest-v0',
    entry_point='minitouch.env.panda.move_cube_easy_random:MoveCubeEasyRandom',
    max_episode_steps=200,
    kwargs={
        "debug": False,
        "test": True,
        "cube_spawn_distance":0.2,
        "sparse_reward_scale": 25,
        "random_side":True,
        "haptics_upper_bound": 50,
        "lf_force": 25,
        "rf_force": 20,
    }
)

gym.envs.register(
    id='Picking-v0',
    entry_point='minitouch.env.panda.grasp:Grasp',
    max_episode_steps=200,
    kwargs={
        "debug": False,
        "test": True,
        "min_num_cube": 1,
        "max_num_cube": 1,
        "min_scale": 0.8,
        "max_scale": 0.8,
        "min_mass": 10,
        "max_mass": 10,
        "randomize_color": False,
        "randomize_cube_pos": True,
        "max_z": 0.15,
        "haptics_upper_bound": 200,
        "lf_force": 350,
        "rf_force": 400,
        "discrete_grasp": False,
        "lift_threshold": 0.05,
    }
)


gym.envs.register(
    id='PickingDebug-v0',
    entry_point='minitouch.env.panda.grasp:Grasp',
    max_episode_steps=200,
    kwargs={
        "debug": True,
        "test": True,
        "min_num_cube": 1,
        "max_num_cube": 1,
        "min_scale": 0.8,
        "max_scale": 0.8,
        "min_mass": 10,
        "max_mass": 10,
        "randomize_color": False,
        "randomize_cube_pos": True,
        "max_z": 0.15,
        "haptics_upper_bound": 200,
        "lf_force": 350,
        "rf_force": 400,
        "discrete_grasp": False,
        "lift_threshold": 0.05,
    }
)
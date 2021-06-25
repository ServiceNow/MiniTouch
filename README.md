# MiniTouch benchmark
Benchmark proposed and used in: Touch-based Curiosity for Sparse-Reward Tasks.

<p align="center">
</p>

 **MiniTouch**, a manipulation benchmark of simulated tasks is comprised of four manipulation tasks 1)pushing 2)opening 3)picking 4)playing with simple objects. It allows evaluation of models' performance on different manipulation tasks that can leverage cross-modal learning. 
 
## How to install
Clone the repository then:
```bash
cd minitouch
pip install -e .
```

## Quick Start
```python
import minitouch.env
import gym

env = gym.make("Pushing-v0")
state = env.reset()

for i in range(0, 1000):
    state, reward, done, info = env.step(env.action_space.sample())
```

## Available tasks

<ul>
    <li>Pushing-v0</li>
    <li>Opening-v0</li>
    <li>Picking-v0</li>
    <li>Playing-v0</li>
</ul>

Note: If you want to see the GUI of the environment you have to use the
debug version of the environment. For example use "PushingDebug-v0" instead of 
"Pushing-v0".
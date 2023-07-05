*ServiceNow completed its acquisition of Element AI on January 8, 2021. All references to Element AI in the materials that are part of this project should refer to ServiceNow.*

# MiniTouch benchmark
Benchmark proposed and used in: Touch-based Curiosity for Sparse-Reward Tasks.

<p align="center">
	<img src="https://github.com/ElementAI/MiniTouch/blob/main/images/minitasks.png" width="350"/>
</p>
 MiniTouch, a manipulation benchmark of simulated tasks is comprised of four manipulation tasks:

- Pushing
- Opening
- Picking
- Playing with simple objects

It allows evaluation of models' performance on different manipulation tasks that can leverage cross-modal learning. 
 
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

- Pushing-v0
- Opening-v0
- Picking-v0
- Playing-v0

Note: If you want to see the GUI of the environment you have to use the
debug version of the environment. For example use "PushingDebug-v0" instead of 
"Pushing-v0".

## Vulnerability Reporting
Please notify psirt-oss@servicenow.com regarding any vulnerability reports in addition to following current reporting procedure.

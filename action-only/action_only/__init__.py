from gym.envs.registration import register

register(
    id='action-only-v0',
    entry_point='action_only.envs:ActionOnly',
)

from dosed.utils import h5_to_memmap
from settings import MINIMUM_EXAMPLE_SETTINGS

signals = [
    {
        "name": "signals",
        "h5_paths": [
            {
                'path': '/eeg_0',
                'processing': {
                    "type": "clip_and_normalize",
                    "args": {
                        "min_value": -150,
                        "max_value": 150,
                    }
                }
            },
            {
                'path': '/eeg_1',
                'processing': {
                    "type": "clip_and_normalize",
                    "args": {
                        "min_value": -150,
                        "max_value": 150,
                    }
                }
            }
        ],
        "fs": 64,
    }
]

events = [
    {
        "name": "spindle",
        "h5_path": "spindle",
    },
]

h5_to_memmap(h5_directory=MINIMUM_EXAMPLE_SETTINGS["h5_directory"],
             memmap_directory=MINIMUM_EXAMPLE_SETTINGS["memmap_directory"],
             signals=signals,
             events=events,
             parallel=True)
# Creates a JSON representation of the Easy #1 board.

import json

stars: list[int] = [130, 40, 257, 80, 5, 160, 10, 320, 20]
shapes: list[list[int]] = [[3, 1, 1],
                           [0, 0, 0, 3, 3, 3, 3, 3, 3],
                           [12, 30, 62, 60, 24, 16, 16],
                           [0, 0, 0, 0, 4, 12, 12, 60, 480],
                           [0, 0, 0, 0, 0, 0, 0, 0, 28],
                           [112, 224, 192, 448, 484, 256],
                           [0, 0, 0, 0, 96, 224, 480],
                           [0, 0, 0, 0, 0, 0, 0, 448],
                           [384, 256, 256]]

data: dict[str, list] = {'stars': stars, 'shapes': shapes}
data_json: str = json.dumps(data, indent=4)

print(data_json)

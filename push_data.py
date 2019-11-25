# jsonbox module required, install with:
# MacOS/Linux:   > python3 -m pip install jsonbox
# Windows (Py3): > pip install jsonbox
from jsonbox import JsonBox
import json

# Generated using the web interface
MY_BOX_ID = "box_089956cbd93379da18f8"


def run(jb):
    with open("data.json", "r") as data_file:
        data = json.loads(data_file.read())

    if len(jb.read(MY_BOX_ID)) == 0:
        jb.write([data], MY_BOX_ID)

    print(jb.read(MY_BOX_ID))


if __name__ == "__main__":
    jb = JsonBox()
    run(jb)

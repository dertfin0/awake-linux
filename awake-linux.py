from pyautogui import moveTo, position
from time import sleep

version = "1.2.1"

logo = f"""

##############################################
#  █████╗ ██╗    ██╗ █████╗ ██╗  ██╗███████╗ #
# ██╔══██╗██║    ██║██╔══██╗██║ ██╔╝██╔════╝ #
# ███████║██║ █╗ ██║███████║█████╔╝ █████╗   #
# ██╔══██║██║███╗██║██╔══██║██╔═██╗ ██╔══╝   #
# ██║  ██║╚███╔███╔╝██║  ██║██║  ██╗███████╗ #
# ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ #
##############################################
For Linux by dertfin1 | v{version}
"""


def main():
    while True:
        pos = [position().x, position().y]
        moveTo(pos[0] + 1, pos[1] + 1)
        moveTo(pos[0], pos[1])
        sleep(3*60)


if __name__ == '__main__':
    print(logo)
    try:
        main()
    except KeyboardInterrupt:
        print("")

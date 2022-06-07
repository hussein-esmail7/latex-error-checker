'''
latex_check.py
Hussein Esmail
Created: 2022 06 07
Updated: 2022 06 07
Description: [DESCRIPTION]
'''

import os
import sys

# ========= VARIABLES ===========

# ========= COLOR CODES =========
color_end               = '\033[0m'
color_darkgrey          = '\033[90m'
color_red               = '\033[91m'
color_green             = '\033[92m'
color_yellow            = '\033[93m'
color_blue              = '\033[94m'
color_pink              = '\033[95m'
color_cyan              = '\033[96m'
color_white             = '\033[97m'
color_grey              = '\033[98m'

# ========= COLORED STRINGS =========
str_prefix_q            = f"[{color_pink}Q{color_end}]"
str_prefix_y_n          = f"[{color_pink}y/n{color_end}]"
str_prefix_ques         = f"{str_prefix_q}\t "
str_prefix_err          = f"[{color_red}ERROR{color_end}]\t "
str_prefix_done         = f"[{color_green}DONE{color_end}]\t "
str_prefix_info         = f"[{color_cyan}INFO{color_end}]\t "


def yes_or_no(str_ask):
    while True:
        y_n = input(f"{str_prefix_q} {str_prefix_y_n} {str_ask}").lower()
        if y_n[0] == "y":
            return True
        elif y_n[0] == "n":
            return False
        if y_n[0] == "q":
            sys.exit()
        else:
            print(f"{str_prefix_err} {error_neither_y_n}")


def main():
    # CODE HERE
    args = sys.argv
    path = "" # LaTeX File path
    path_contents = [] # Contents of the LaTeX file will go here
    num_brackets_o = 0 # Count how many open brackets "{" there are
    num_brackets_c = 0 # Count how many closed brackets "}" there are
    print(len(args))
    if len(args) < 2:
        # The user hasn't given a file path
        print(f"{str_prefix_err} Please input your file path!")
        sys.exit(1)
    path = args[1] # File path of the LaTeX file
    if not os.path.exists(path):
        # Given file path does not exist
        print(f"{str_prefix_err} This file path does not exist!")
        sys.exit(1)



    sys.exit()


if __name__ == "__main__":
    main()

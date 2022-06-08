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
BOOL_DEV_PRINTS = True
BOOL_SHOW_LINES_ALL = False
BOOL_SHOW_LINES_ERRORS_ONLY = True
path_contents = [] # Lines of the file to check will go here

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
str_prefix_warn         = f"[{color_yellow}WARN{color_end}]\t "


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


def nComment(find, line):
    # Determine if the string is in a single-line comment if it is in it.
    if find not in line: # Substring not there
        return False
    i_find = line.index(find)
    if "%" not in line: # No '%' symbol, definitely not a comment
        return True
    else: # '%' found
        if "\\" in line:
            i_percent = line.index("%")
            i_slash = line.index("\\")
            if i_percent != 0 and line[i_percent-1] == "\\":
                # If % is not the first symbol, and '\' is one char behind it
                # % is an escape char in this case
                return True
            return False
        else:
            # No '\' present
            return False


def show_lines(line_nums, file_lines, color_hl):
    # This function shows the selected line and the 2 lines around it
    # line_nums: Integer array, even of length 1. Size 0 not supported
    # file_lines: Lines of the original file
    range_print = 2
    if BOOL_SHOW_LINES_ERRORS_ONLY or BOOL_SHOW_LINES_ALL:
        # If you want to show where there is an error
        for num in line_nums:
            for offset in range(range_print, 0, -1):
                if num-offset > 0: # If it is positive or 0
                    line = file_lines[num-offset-1]
                    if len(line) == 0:
                        line = "[BLANK]"
                    print(f"\t  {num-offset}\t{line}")
                else:
                    print("\t  0\t[START OF FILE]")
            print(f"\t  {num}\t{color_hl}{file_lines[num-1]}{color_end}")
            for offset in range(1, range_print+1):
                if num+offset <= len(file_lines) and num+offset > 0:
                    # Within file length
                    line = file_lines[num+offset-1]
                    if len(line) == 0:
                        line = "[BLANK]"
                    print(f"\t  {num+offset}\t{line}")
                else:
                    print("\t  {num+offset}\t[END OF FILE]")
            if num != line_nums[-1]:
                # Print a new line between entries but not after the last one
                print()

def warn(msg, line_nums, file_lines):
    # msg: Error message as string
    # line_nums: Integer array, even of length 1. Size 0 not supported
    # file_lines: Lines of the original file
    print(f"{str_prefix_warn} {msg}")
    show_lines(line_nums, file_lines, color_yellow)


def error(msg, line_nums, file_lines):
    # msg: Error message as string
    # line_nums: Integer array, even of length 1. Size 0 not supported
    # file_lines: Lines of the original file
    print(f"{str_prefix_err} {msg}")
    show_lines(line_nums, file_lines, color_red)

def hl(input):
    color_use = color_cyan
    return color_use + input + color_end

def main():
    args = sys.argv
    path = "" # LaTeX File path
    path_contents = [] # Contents of the LaTeX file will go here
    num_brackets_o = 0 # Count how many open brackets "{" there are
    num_brackets_c = 0 # Count how many closed brackets "}" there are

    # Verify the user gave an existing file path
    if len(args) < 2:
        # The user hasn't given a file path
        print(f"{str_prefix_err} Please input your file path!")
        sys.exit(1)
    path = args[1] # File path of the LaTeX file
    if not os.path.exists(path):
        # Given file path does not exist
        print(f"{str_prefix_err} This file path does not exist!")
        sys.exit(1)
    path_contents = open(path, "r").readlines() # Read the file

    # Array formatting
    for num, item in enumerate(path_contents):
        path_contents[num] = path_contents[num].replace("\n", "")
    # if BOOL_DEV_PRINTS:
    #     print(path_contents)
    #     for item in path_contents:
    #         print(item)

    # Check for errors and missing components here
    bool_has_documentclass = 0 # Check for "\documentclass{"
    bool_inside_comment = 0 # If "%" is before string or inside a `comment` env
    pos_documentclass = [] # Lines where "documentclass" is found
    arr_environments = [] # Environments that are used. Added when opened, removed when closed.

    for line_num, item in enumerate(path_contents):
        line_num_actual = line_num + 1 # Actual line number, starting at 1
        # Inside comment environment
        if nComment("\\begin{comment}", item): # Comment block start
            bool_inside_comment += 1
            if bool_inside_comment > 1:
                warn(f"Comment block inside comment block at line {line_num_actual}", [line_num_actual], path_contents)
        if nComment("\\end{comment}", item) and bool_inside_comment == 1:
            # Comment block end
            bool_inside_comment -= 1

        # Error checking here
        if bool_inside_comment == 0:
            # Times of documentclass must be 1
            if nComment("\\documentclass{", item):
                # Check for "\documentclass{"
                bool_has_documentclass += 1
                pos_documentclass.append(line_num_actual)
            # TODO: Count number of open brackets (that are not escaped)
            # TODO: Count number of closed brackets (that are not escaped)
            # TODO: Make sure all equations are closed ($ MATH $)

            # TODO: Make sure all environments are ended (itemize*, etc.)



    # Print errors that were calculated
    if bool_has_documentclass != 1:
        if bool_has_documentclass < 1:
            error("TODO", [-1], path_contents)
        if bool_has_documentclass > 1:
            pos_documentclass_str = ", ".join(str(x) for x in pos_documentclass)
            error(f"You have too many \'{hl('documentclass')}\' lines, at lines {pos_documentclass_str}", pos_documentclass, path_contents)

    sys.exit()


if __name__ == "__main__":
    main()

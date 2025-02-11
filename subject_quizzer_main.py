# Importing
import os
import time
import random
import sys
import math
import platform
import colorama
from colorama import Fore

# Variables
dash = "-" * 70
arrow_dash = "<" + "-" * 68 + ">"
arrow_mode = ""
dash_symbol = ""
debug_mode = ""
secret_matrix_mode = ""
matching_files = ""
current_question = ""
current_answer = ""
total_points = ""

# Ascii Art
azure_command_ascii = '''
                ╔═╗┌─┐┬ ┬┬─┐┌─┐  ╔═╗┌─┐┌┬┐┌┬┐┌─┐┌┐┌┌┬┐
                ╠═╣┌─┘│ │├┬┘├┤   ║  │ │││││││├─┤│││ ││
                ╩ ╩└─┘└─┘┴└─└─┘  ╚═╝└─┘┴ ┴┴ ┴┴ ┴┘└┘─┴┘
'''
subject_quizzer_ascii = '''
              ╔═╗┬ ┬┌┐  ┬┌─┐┌─┐┌┬┐  ╔═╗ ┬ ┬┬┌─┐┌─┐┌─┐┬─┐
              ╚═╗│ │├┴┐ │├┤ │   │   ║═╬╗│ ││┌─┘┌─┘├┤ ├┬┘
              ╚═╝└─┘└─┘└┘└─┘└─┘ ┴   ╚═╝╚└─┘┴└─┘└─┘└─┘┴└─
'''
start_quiz_ascii = '''
                    ╔═╗┌┬┐┌─┐┬─┐┌┬┐  ╔═╗ ┬ ┬┬┌─┐
                    ╚═╗ │ ├─┤├┬┘ │   ║═╬╗│ ││┌─┘
                    ╚═╝ ┴ ┴ ┴┴└─ ┴   ╚═╝╚└─┘┴└─┘
'''
add_questions_ascii = '''
                ╔═╗┌┬┐┌┬┐  ╔═╗ ┬ ┬┌─┐┌─┐┌┬┐┬┌─┐┌┐┌┌─┐
                ╠═╣ ││ ││  ║═╬╗│ │├┤ └─┐ │ ││ ││││└─┐
                ╩ ╩─┴┘─┴┘  ╚═╝╚└─┘└─┘└─┘ ┴ ┴└─┘┘└┘└─┘
'''
remove_questions_ascii = '''
          ╦═╗┌─┐┌┬┐┌─┐┬  ┬┌─┐  ╔═╗ ┬ ┬┌─┐┌─┐┌┬┐┬┌─┐┌┐┌┌─┐
          ╠╦╝├┤ ││││ │└┐┌┘├┤   ║═╬╗│ │├┤ └─┐ │ ││ ││││└─┐
          ╩╚═└─┘┴ ┴└─┘ └┘ └─┘  ╚═╝╚└─┘└─┘└─┘ ┴ ┴└─┘┘└┘└─┘
'''
questions_ascii = '''
                    ╔═╗ ┬ ┬┌─┐┌─┐┌┬┐┬┌─┐┌┐┌┌─┐
                    ║═╬╗│ │├┤ └─┐ │ ││ ││││└─┐
                    ╚═╝╚└─┘└─┘└─┘ ┴ ┴└─┘┘└┘└─┘
'''
leaderboard_ascii = '''
                  ╦  ┌─┐┌─┐┌┬┐┌─┐┬─┐┌┐ ┌─┐┌─┐┬─┐┌┬┐
                  ║  ├┤ ├─┤ ││├┤ ├┬┘├┴┐│ │├─┤├┬┘ ││
                  ╩═╝└─┘┴ ┴─┴┘└─┘┴└─└─┘└─┘┴ ┴┴└──┴┘
'''
settings_ascii = '''
                        ╔═╗┌─┐┌┬┐┌┬┐┬┌┐┌┌─┐┌─┐
                        ╚═╗├┤  │  │ │││││ ┬└─┐
                        ╚═╝└─┘ ┴  ┴ ┴┘└┘└─┘└─┘
'''
exit_ascii = '''
                            ╔═╗─┐ ┬┬┌┬┐
                            ║╣ ┌┴┬┘│ │ 
                            ╚═╝┴ └─┴ ┴ 
'''
arrow_mode_ascii = '''
                    ╔═╗┬─┐┬─┐┌─┐┬ ┬  ╔╦╗┌─┐┌┬┐┌─┐
                    ╠═╣├┬┘├┬┘│ ││││  ║║║│ │ ││├┤ 
                    ╩ ╩┴└─┴└─└─┘└┴┘  ╩ ╩└─┘─┴┘└─┘
'''
debug_mode_ascii = '''
                    ╔╦╗┌─┐┌┐ ┬ ┬┌─┐  ╔╦╗┌─┐┌┬┐┌─┐
                     ║║├┤ ├┴┐│ ││ ┬  ║║║│ │ ││├┤ 
                    ═╩╝└─┘└─┘└─┘└─┘  ╩ ╩└─┘─┴┘└─┘
'''
secret_matrix_ascii = '''
                ╔═╗┌─┐┌─┐┬─┐┌─┐┌┬┐  ╔╦╗┌─┐┌┬┐┬─┐┬─┐ ┬
                ╚═╗├┤ │  ├┬┘├┤  │   ║║║├─┤ │ ├┬┘│┌┴┬┘
                ╚═╝└─┘└─┘┴└─└─┘ ┴   ╩ ╩┴ ┴ ┴ ┴└─┴┴ └─
'''
subject_chooser_ascii = '''
          ╔═╗┬ ┬┌┐  ┬┌─┐┌─┐┌┬┐  ╔═╗┬ ┬┌─┐┌─┐┌─┐┌─┐┬─┐
          ╚═╗│ │├┴┐ │├┤ │   │   ║  ├─┤│ ││ │└─┐├┤ ├┬┘
          ╚═╝└─┘└─┘└┘└─┘└─┘ ┴   ╚═╝┴ ┴└─┘└─┘└─┘└─┘┴└─
'''
john_pork_ascii = '''⠀⡀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠄⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠄⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠠⠀⠀⠠⠀
⠀⢈⠀⠄⠁⠀⠀⠀⠠⠀⠀⠈⠀⢀⠈⢀⠀⠄⠁⢀⠀⠄⠀⠀⠄⠀⠀⠀⠀⡀⠀⠀⠀⠈⠀⠈⠀⠀⠀⠀⢀⠀⠀⠄⠀⠁⢀⠀⠐⠀⠀⠀⠀⠀⠈⠀⠈⠠⠀⠠⠀⠀⠀⡀⠀
⠀⢀⠀⠠⠀⠠⠈⠀⠀⠀⠀⠡⠈⠀⠄⠂⠠⢀⠈⢀⠀⡐⠈⠀⠄⠀⠂⠁⠀⠀⡀⠀⠂⠀⡈⠀⠠⠀⠂⠀⠀⠀⠄⠠⠀⢀⠀⢀⠠⠀⠂⠀⡈⠀⠁⡈⠀⠂⠄⠠⠀⠠⠁⠀⠀
⠀⠠⢀⠀⢀⠀⠀⠀⠄⠁⡈⠀⠄⠡⠌⢠⠁⢆⠨⢐⠠⡐⡉⢐⠈⡄⠡⠀⠄⠀⠀⠀⠀⠂⠀⠄⠀⠄⠀⠀⠁⠀⠀⠀⠐⠀⢀⠀⠀⠀⠀⢀⠀⢀⠐⠀⡀⠂⢄⣷⣾⣶⣮⣴⣥
⠀⠠⠀⠀⡀⠂⠀⡈⠄⡐⢠⠑⢌⠡⡚⢠⠍⢢⠑⡌⢢⠡⡘⡄⢣⠄⢃⠌⡀⠈⠄⠂⢀⠀⠂⠠⠀⢀⠐⠀⠐⠈⠀⠁⠈⠀⡀⠀⠄⠁⠀⠂⣠⣤⣤⣁⣐⣤⣼⣿⣿⣾⣿⣷⣿
⠀⢀⠀⠂⢀⢠⣱⡞⠄⡁⢆⡉⢆⠣⣉⠲⡈⢇⡚⢤⢃⠌⡱⢈⠦⡘⠔⠢⠄⡉⣦⡐⠀⠀⠄⢀⠐⠀⠀⢈⠠⠐⠀⡀⠂⡀⠀⠠⠀⢂⢡⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾
⠀⢠⠀⠰⣼⣷⣿⡷⣤⠳⣤⡸⣤⡷⣼⢳⡸⣦⡼⢦⣜⢞⣧⣛⢶⣣⢞⢳⡀⠰⣿⣧⡳⣷⣶⣄⣄⣆⠀⡄⠀⠀⠆⠀⠀⢠⠰⠀⢠⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠤⣸⣿⣿⣿⠹⢀⠣⠄⠣⢄⠇⡜⣘⠣⡜⣡⠛⣌⠻⢄⠋⡜⡡⠛⠤⣁⠛⢹⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣀⣤⢰⢿⣟⣻⠇⡃⠄⢲⠌⠃⣍⡲⣱⢊⡵⢸⢡⢋⠴⡩⢆⢯⠴⣁⣋⢒⢠⠲⠠⢿⣿⡎⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣾⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣉⡈⢧⣿⣉⡿⢈⠔⢪⡔⣯⡿⢿⣽⣏⣿⢺⡅⢫⠸⡰⢙⡮⣏⣿⣷⢿⢯⣟⡶⢍⠈⣿⣷⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠉⢱⢾⡏⡹⠌⡰⣙⢮⣿⡾⣿⣿⣿⣿⣟⢧⢋⢦⢃⡜⠱⢚⣽⣿⣿⣿⣿⣷⣿⠫⠴⡸⣿⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⢸⣻⡇⠧⢑⠠⡕⣊⠶⢻⠻⣿⠻⣯⢛⡜⠬⡀⢃⠌⡑⢊⠔⡻⢟⢯⠿⢱⠚⡅⢃⡐⢻⣷⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣻⣿⣿⣾⣿⣿⣿⣿⣿⣿⡿⣟⣿
⠀⢸⣿⢻⠐⣊⠱⡘⣆⠫⡎⡕⢎⡵⡸⢌⡰⢁⠊⡄⢚⠠⢊⠤⢉⠚⡆⢞⡡⢖⡱⢂⡱⠈⣿⢹⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣾⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣽⣟⡿⣯⣿
⠀⠸⣿⡀⡱⢌⡳⣙⠴⣋⡜⡜⢢⡅⡓⢤⢐⢢⣱⣘⣌⠶⣡⣊⠴⢕⡘⢦⡱⢎⡴⢣⡜⠡⣿⠀⠄⠉⠉⠉⠒⣻⣯⣿⣿⢿⣻⣿⣾⣿⣿⣿⡿⣿⣷⣿⣿⣿⣿⣿⣿⣹⣿⣽⣿
⠀⠀⠋⠣⡐⡱⣒⢭⣚⠴⡸⡌⠣⡔⢡⣒⡼⣦⣳⣚⡼⣝⣳⡭⣖⠦⡌⢢⢝⢶⣊⡕⣊⠉⡈⠀⠈⠀⢄⣐⣰⣾⣾⣿⣿⣿⣿⣿⣿⣿⢿⣿⣾⣿⣯⣿⣿⣷⣿⣻⣿⣿⢽⢿⣿
⠀⢈⠀⠡⣑⠱⡌⣒⢎⡯⣓⣌⠑⡌⣖⢮⣷⣷⣿⣫⡞⣝⣶⣿⣿⡷⣝⡆⣌⠳⢎⠖⡤⢃⠄⠁⠤⢞⢻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣻⣿⣿⣿⣿⣿⣾⣿⣷⣿⣿⣾⠿⣿⣿
⠀⠄⢀⠣⣐⡩⡸⣈⠞⡵⣫⢻⡴⡸⢮⣷⣻⣿⣿⢟⣼⣳⢟⡿⣿⣻⠽⣞⡞⢫⢜⢃⠐⡎⡀⠠⠐⠀⠐⠈⠛⡿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⡿⣿⣾⣿⣿⣿⣯⣟⣿⣿⣟⣽
⡀⠐⠀⢃⠶⣡⠳⡌⢯⣕⡣⢏⡾⣳⣟⣶⣳⡽⣞⣻⢾⡽⢯⣻⣵⣫⡿⣎⠹⢆⠏⠆⢭⡐⢁⠠⠀⠌⡠⢔⣶⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⠿⣏⣿⣿⣿
⢀⠐⠈⡴⢣⢇⠵⣩⢎⠶⣙⠧⡚⡭⡟⡿⣿⣟⡿⣟⣿⣻⣟⣯⢟⡳⡙⢄⠳⢎⡹⠜⢤⡙⡀⠄⠂⡐⠠⠘⡛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣯⣟⢿⣞⣿⣿⣿
⠤⢈⣠⢶⢩⣎⠳⣬⢚⡭⢧⣛⢥⠷⣙⢷⡳⢮⡟⣽⢺⢧⡻⣜⢫⡲⢩⠌⡝⡬⢕⡉⠖⡜⢀⠊⡂⠑⠉⡉⢒⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⡿
⠀⣼⣿⣿⣗⣮⢟⣶⣫⢷⣳⡼⣎⢿⣹⣎⣟⢧⣻⢵⣫⢮⠵⣎⠷⣬⢣⢟⡴⢭⡎⢼⣉⡶⡌⠡⠍⠼⠀⠔⡨⠜⣛⠝⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢯⣻⣿⣿⣾
⣾⣿⣿⣿⣿⣿⣿⣶⣻⣞⡷⣯⣟⣯⣷⣻⣾⢯⣟⣾⡽⣯⣛⣾⣻⡼⣏⡾⣸⣣⠞⡧⣵⣿⣦⡔⢈⠓⠬⠖⠄⢓⡁⠔⢂⣩⢛⣿⣿⣿⣷⣿⣾⣿⣿⣿⣿⣿⡷⣟⣾⣿⣿⣺⣯
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣽⣷⣿⣾⣻⣟⣯⣿⣟⣯⣿⣷⣟⣾⣧⣿⣹⢳⣧⣝⢣⣆⣿⣿⣿⣷⣤⠒⣶⢊⠁⣦⣡⣾⣫⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⢿⣿⣿⣿⣿⣿⡿⡾⣽⠿⣼⠟⣿⣿⣿⣿⣷⣽⠸⢸⠛⡿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣾⣟⣿⡾⣽⣞⣷⢫⡽⣹⡝⡾⣏⡿⣽⣿⣿⣿⣿⣿⣖⢧⡯⢙⢗⣾⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⡯⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣯⢿⣽⡻⣞⣭⢿⣙⠧⣝⣳⢯⣟⣷⣿⣿⣿⣿⣿⣿⣯⣶⣮⣾⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣟⣿⣿⣿⣿⣽⣾⣿⣿⣹⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⣽⢿⡾⣽⣻⢮⠷⣍⠾⣱⢫⣟⣾⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣟⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣷⣳⣭⣯⣿⣞⣿⣵⡿⣟⣿⣾⢿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣻⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣾⣻
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣽⣿⢿⢿⣿⣿⣿⢿⣿⣿⣿⣿⣿⡿⣟⣽⣾
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣻⣾⣷⣿⣾⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣟⣿⣿⣿⢟⣽⣿⣻⣿⣿⣿⡷⣻⣿⣯⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣟⣯⣷⣿⣷⣿⣻⣽⣿⣿⣿⣿⣿⣿⣿⣿⣟⢿⣿⣟⣯⣟⣿⣿⣿⣽⣿⣿⣾⣷⣻⣽⣷⣽⣿⡽⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣷⣿⣞⣿⣻⣼⣿⣿⣿⣿⣿⣿⣿⣽⣿⣾⣿⣽⡿'''
gay_goose_ascii = '''⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬛⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬛⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛🏽⬛⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜
⬜⬜⬜⬜⬜⬛🟥🟥⬛🏽🏽⬛⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬛⬛⬛⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜
⬜⬜⬜⬜⬜⬛🟥🟧🟧⬛🏽🏽⬛⬜⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜
⬜⬜⬜⬛⬛🟥🟥🟧🟨🟨⬛🏽🏽⬛⬜⬛🟧⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬛⬜⬜⬜
⬜⬜⬛🟥🟥🟥🟧🟨🟨🟩🟩⬛🏽🏽⬛⬛🟧🟧⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜
⬜⬛🟥🟥🟧🟧🟧🟨🟩🟩🟩🟦⬛🏽⬛🟧🟧🟧🟧⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜
⬛🟥🟥🟧🟧🟨🟨🟩🟩🟩🟦🟦🟦⬛🟧🟧🟧🟧🟧⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜
⬛🟥🟧🟧🟨🟨🟩🟩🟩🟦🟦🟦⬛🟧🟧🟧🟧🟧🟧🟧⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜
⬛🟥🟧🟨🟨🟩🟩🟦🟦🟦🟦🟪🟪⬛⬛🟧🟧🟧⬛⬛⬛⬛⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜
⬜⬛🟨🟨🟩🟩🟦🟦🟦🟪🟪🟪🟪⬛⬜⬛⬛⬛🏽⬛⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜
⬜⬛🟩🟩🟩🟦🟦🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬛🏽🏽⬛⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜
⬜⬜⬛🟩🟦🟦🟪🟪⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬛🏽⬛⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜
⬜⬜⬜⬛🟦🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟧⬛⬜⬜
⬜⬜⬜⬜⬛🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟧🟧⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟧🟧⬛⬜
⬜⬜⬜⬜⬜⬛🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧⬛⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟧🟧🟧⬛
⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟧🟧🟧🟧⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟧🟧🟧⬛
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧⬛
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧⬛
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧⬛
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧⬛
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜'''
gay_girl_ascii = '''🟥🟥🟥⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬛⬛🟥🟥🟥🟥🟥🟥
🟥🟥⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬛⬛🟥🟥🟥🟥🟥
🟥🟥⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛⬛⬜⬜⬛⬛⬛⬛⬛⬜⬛⬛⬛⬛🟥🟥🟥🟥
🟥🟥⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬛⬜🟩⬛⬛⬛⬛🟩⬛⬛⬛⬛🟥🟥🟥
🟧⬛⬛⬛⬛⬛⬛⬛⬜⬛⬛⬛⬛🟩⬛⬛🟩🟩⬛⬛⬛🟩🟩🟩⬛🟩⬛🟧🟧
🟧⬛⬛⬛⬛⬛⬜⬛⬜⬜⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩⬛⬛🟩🟩🟩🟩⬛🟧🟧
🟧⬛⬛⬛⬛⬛⬛⬜⬛🟩🟩🟩⬛🟩🟩🟩🟩🟩🟩🟩🟩⬛🟩🟩⬛🟩⬛🟧🟧
🟧⬛⬛⬛⬛🟩🟩⬜⬜⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟪🟩⬛🟧🟧🟧
🟧⬛⬛⬛⬛🟪🟩⬜⬜⬜⬛⬛⬛🟩🟩🟩🟪🟩🟩🟪🟪🟩🟩🟪🟪⬛🟧🟧🟧
🟨🟨⬛⬛⬛🟪🟪⬜⬜⬛⬜⬜⬛⬛⬛🟪🟪🟩🟩🟪🟪🟪🟩🟪🟪⬛🟨🟨🟨
🟨🟨⬛⬛⬛🟩🟩⬜⬛⬜⬛⬜⬜⬜⬛⬛🟪🟪🟩🟪🟪🟪🟪🟪🟪⬛🟨🟨🟨
🟨🟨⬛⬛⬛🟪🟪⬜⬜⬛⬜⬜⬜⬜⬜⬛⬛🟪🟪🟪🟪🟪🟪🟪🟪⬛🟨🟨🟨
🟨🟨⬛⬛⬛🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟪🟪🟪🟪🟪⬛🟪⬛🟨🟨🟨
🟨🟨⬛⬛⬛🟪🟪⬜⬜⬜⬜⬜⬛⬜⬜⬜⬛⬛⬛🟪🟪🟪🟪⬛🟪⬛🟨🟨🟨
🟩🟩⬛⬛⬛🟩🟩⬜⬜⬜⬜⬜⬛⬜⬛⬜⬛⬜⬛🟪🟪⬛🟪⬛⬛🟩🟩🟩🟩
🟩⬛⬛⬛⬛🟪🟪⬛⬜⬜⬜⬜⬜⬛⬜⬛⬜⬜⬛🟪⬛⬛⬛🟩🟩🟩🟩🟩🟩
⬛⬛⬛⬛⬛⬛🟪⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟩⬛🟩🟩🟩🟩🟩🟩🟩
🟩⬛⬛⬛⬛⬛🟪⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛🟦⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩⬛⬛⬛🟦🟦🟦⬛⬜⬛⬛⬜⬜⬛🟦🟦🟦⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩
🟦⬛⬛⬛⬛⬛🟦🟦🟦⬛⬜⬜⬜⬛⬛🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦🟦🟦🟦🟦
⬛⬛🟦🟦🟦🟦🟦🟦🟦⬛⬜⬜⬜⬛🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦🟦🟦🟦🟦
⬛🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛⬛⬜⬛🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦🟦🟦🟦🟦
⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦⬛⬛⬛⬛🟦🟦🟦🟦🟦🟦🟦
🟪⬛⬛🟦⬛⬛🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛⬛⬛🟦🟦⬛⬛⬛🟪🟪🟪🟪🟪🟪
🟪⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟦⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦⬛🟪🟪🟪🟪🟪🟪
🟪⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟪🟪🟪🟪🟪🟪
🟪⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟪🟪🟪🟪🟪🟪'''
gay_frog_ascii = '''⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟥🟥🟥⬛⬛🟥🟥🟥⬛🟥⬛🟥⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟨⬛⬛⬛⬛🟨⬛🟨⬛🟨⬛🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟨⬛🟨🟨⬛🟨🟨🟨⬛🟨⬛🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟩⬛⬛🟩⬛🟩⬛🟩⬛⬛🟩⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬛⬛⬛⬛🟦🟦🟦🟦⬛🟦⬛🟦⬛⬛🟦⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛
⬛🟥⬛⬛⬛🟥⬛⬛⬛🟥🟥⬛⬛🟥🟥⬛⬛⬛🟥🟥⬛⬛⬛🟥⬛
⬛🟧⬛🟧🟧🟧⬛🟧⬛🟧⬛🟧🟧⬛🟧⬛🟧🟧🟧🟧⬛🟧🟧🟧⬛
⬛🟨⬛⬛🟨🟨⬛⬛🟨🟨⬛🟨🟨⬛🟨⬛🟨⬛⬛🟨⬛⬛⬛🟨⬛
⬛🟩⬛🟩🟩🟩⬛🟩⬛🟩⬛🟩🟩⬛🟩⬛🟩🟩⬛🟩🟩🟩⬛🟩⬛
⬛🟦⬛🟦🟦🟦⬛🟦⬛🟦🟦⬛⬛🟦🟦⬛⬛⬛⬛🟦⬛⬛⬛🟦⬛
⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛'''


# Function - get_base_path()
def get_base_path():
  if getattr(sys, 'frozen', False):
    return sys._MEIPASS
  else:
    return os.path.dirname(os.path.abspath(__file__))


base_path = get_base_path()
folders_and_files = {
    "subject_quizzer": {
        "questions": {
            "a_math_questions.txt": "",
            "biology_questions.txt": "",
            "chemistry_questions.txt": "",
            "chinese_questions.txt": "",
            "computing_questions.txt": "",
            "english_questions.txt": "",
            "e_math_questions.txt": "",
            "physics_questions.txt": ""
        },
        "answers": {
            "a_math_answers.txt": "",
            "biology_answers.txt": "",
            "chemistry_answers.txt": "",
            "chinese_answers.txt": "",
            "computing_answers.txt": "",
            "english_answers.txt": "",
            "e_math_answers.txt": "",
            "physics_answers.txt": ""
        },
        "others": {
            "leaderboard.txt":
            "",
            "settings.txt":
            "Dash Symbol =-=~= -\nArrow Mode =-=~= on\nDebug Mode =-=~= off\n⎎ℇ⍧☈ℇ⍑ ⍓⍲⍑☈⟟🝍 =-=~= off"
        }
    }
}


# Function - check_and_create_files()
def check_and_create_files():
  for folder, subfolders in folders_and_files.items():
    main_folder_path = os.path.join(base_path, folder)

    if not os.path.exists(main_folder_path):
      print(f"Folder '{main_folder_path}' not found. Creating it now...")
      os.makedirs(main_folder_path)

    for subfolder, files in subfolders.items():
      subfolder_path = os.path.join(main_folder_path, subfolder)

      if not os.path.exists(subfolder_path):
        print(f"Subfolder '{subfolder_path}' not found. Creating it now...")
        os.makedirs(subfolder_path)

      for file, data in files.items():
        file_path = os.path.join(subfolder_path, file)

        if not os.path.exists(file_path):
          print(f"File '{file_path}' not found. Creating it now...")
          with open(file_path, 'w') as f:
            f.write(data)
            print(f"Specific data written to '{file_path}'")


check_and_create_files()


# Function - find_file(target_filename)
def find_file(target_filename):
  global matching_files
  for root, dirs, files in os.walk(os.path.dirname(__file__)):
    if target_filename in files:
      matching_files = str(os.path.join(root, target_filename))


# Function - get_settings_value()
def get_settings_value():
  global arrow_mode, debug_mode, dash_symbol, secret_matrix_mode
  find_file("settings.txt")
  with open(matching_files, 'r') as file:
    for line in file:
      if ' =-=~= ' in line:
        key, value = line.strip().split(' =-=~= ', 1)
        if key == "Arrow Mode":
          arrow_mode = str(value)

        elif key == "Debug Mode":
          debug_mode = str(value)

        elif key == "Dash Symbol":
          dash_symbol = str(value)

        elif key == "⎎ℇ⍧☈ℇ⍑ ⍓⍲⍑☈⟟🝍":
          secret_matrix_mode = str(value)


# Function - clear_screen()
def clear_screen():
  if platform.system() == "Windows":
    os.system("cls")
  else:
    os.system("clear")


# Function - arrow_dash_or_no(thing)
def arrow_dash_or_no(thing):
  if thing == 'on':
    print(arrow_dash)
  elif thing == 'off':
    print(dash)


# Function - secret_matrix_main()
def secret_matrix_main():
  print(f"\n{Fore.RED}Verifying identity...{Fore.WHITE}")
  time.sleep(1)
  print(f"{Fore.RED}.{Fore.WHITE}")
  time.sleep(1)
  print(f"{Fore.RED}.{Fore.WHITE}")
  time.sleep(1)
  print(f"{Fore.RED}.{Fore.WHITE}")
  time.sleep(1)
  print(f"{Fore.RED}.{Fore.WHITE}")
  time.sleep(1)
  print(f"{Fore.RED}.{Fore.WHITE}")
  time.sleep(1)
  print(
      f"{Fore.GREEN}Identity verified. {Fore.CYAN}Opening matrix...{Fore.WHITE}"
  )
  time.sleep(1.5)
  clear_screen()
  time.sleep(1)
  arrow_dash_or_no(arrow_mode)
  time.sleep(2)
  print(f"{Fore.RED}{secret_matrix_ascii}{Fore.WHITE}")
  time.sleep(1)
  arrow_dash_or_no(arrow_mode)
  time.sleep(1)
  print(
      f"\n{Fore.LIGHTGREEN_EX}Matrix unlocked. {Fore.RED}Initializing...{Fore.WHITE}"
  )
  time.sleep(1.5)
  print(f"\n{Fore.LIGHTBLUE_EX}Initalization complete.{Fore.WHITE}")
  time.sleep(1)
  while True:
    clear_screen()
    arrow_dash_or_no(arrow_mode)
    print(f"{Fore.RED}{secret_matrix_ascii}{Fore.WHITE}")
    arrow_dash_or_no(arrow_mode)
    secret_matrix_status = f"{Fore.LIGHTGREEN_EX}{secret_matrix_mode}{Fore.WHITE}" if secret_matrix_mode == "on" else f"{Fore.RED}{secret_matrix_mode}{Fore.WHITE}"
    print(f"\n                      Secret Matrix | {secret_matrix_status}\n")
    arrow_dash_or_no(arrow_mode)
    secret_matrix_option = str(
        input("\nNew Mode ('return' to go back) -> ")).lower()
    if secret_matrix_option == "on":
      print()
      arrow_dash_or_no(arrow_mode)
      print(
          f"\n{Fore.LIGHTGREEN_EX}The Hidden Matrix Protocol is now live and fully operational.\n{Fore.WHITE}"
      )
      arrow_dash_or_no(arrow_mode)
      find_file("settings.txt")
      with open(matching_files, "w") as file:
        file.write(f"Dash Symbol =-=~= {dash_symbol}\n")
        file.write(f"Arrow Mode =-=~= {arrow_mode}\n")
        file.write(f"Debug Mode =-=~= {debug_mode}\n")
        file.write("⎎ℇ⍧☈ℇ⍑ ⍓⍲⍑☈⟟🝍 =-=~= on")
        file.close()
      get_settings_value()
      time.sleep(2)
      quizzer_main()

    elif secret_matrix_option == "off":
      print()
      arrow_dash_or_no(arrow_mode)
      print(
          f"\n{Fore.RED}The Hidden Matrix Protocol has been deactivated and is no longer operational.\n{Fore.WHITE}"
      )
      arrow_dash_or_no(arrow_mode)
      find_file("settings.txt")
      with open(matching_files, "w") as file:
        file.write(f"Dash Symbol =-=~= {dash_symbol}\n")
        file.write(f"Arrow Mode =-=~= {arrow_mode}\n")
        file.write(f"Debug Mode =-=~= {debug_mode}\n")
        file.write("⎎ℇ⍧☈ℇ⍑ ⍓⍲⍑☈⟟🝍 =-=~= off")
        file.close()
      get_settings_value()
      time.sleep(2)
      quizzer_main()

    else:
      print(f"\n{Fore.RED}{'~'*28}Invalid Choice{'~'*28}{Fore.WHITE}")
      time.sleep(1)


# Function - settings_main()
def settings_main():
  clear_screen()
  arrow_dash_or_no(arrow_mode)
  print(f"{Fore.RED}{settings_ascii}{Fore.WHITE}")
  arrow_dash_or_no(arrow_mode)
  print(
      f"\nDash Symbol | {dash_symbol}\nArrow Mode | {arrow_mode}\nDebug Mode | {debug_mode}\n⎎ℇ⍧☈ℇ⍑ ⍓⍲⍑☈⟟🝍 | {secret_matrix_mode}\n"
  )
  arrow_dash_or_no(arrow_mode)
  settings_option = str(
      input("\nSetting to change ('return' to go back) -> ")).lower()
  if settings_option == "debug mode":
    while True:
      clear_screen()
      arrow_dash_or_no(arrow_mode)
      print(f"{Fore.RED}{debug_mode_ascii}{Fore.WHITE}")
      arrow_dash_or_no(arrow_mode)
      debug_status = f"{Fore.LIGHTGREEN_EX}{debug_mode}{Fore.WHITE}" if debug_mode == "on" else f"{Fore.RED}{debug_mode}{Fore.WHITE}"
      print(f"\nCurrent Debug Mode - {debug_status}\n")
      arrow_dash_or_no(arrow_mode)
      debug_mode_option = str(
          input("\nNew mode ('return' to go back) -> ")).lower()
      if debug_mode_option == "on":
        print()
        arrow_dash_or_no(arrow_mode)
        print(f"\n{Fore.LIGHTGREEN_EX}Debug mode is now active.{Fore.WHITE}\n")
        arrow_dash_or_no(arrow_mode)
        with open(matching_files, "w") as file:
          file.write(f"Dash Symbol =-=~= {dash_symbol}\n")
          file.write(f"Arrow Mode =-=~= {arrow_mode}\n")
          file.write("Debug Mode =-=~= on\n")
          file.write(f"⎎ℇ⍧☈ℇ⍑ ⍓⍲⍑☈⟟🝍 =-=~= {secret_matrix_mode}")
          file.close()
        get_settings_value()
        time.sleep(2)
        settings_main()

      elif debug_mode_option == "off":
        print()
        arrow_dash_or_no(arrow_mode)
        print(
            f"\n{Fore.LIGHTGREEN_EX}Debug mode is now inactive.{Fore.WHITE}\n")
        arrow_dash_or_no(arrow_mode)
        with open(matching_files, "w") as file:
          file.write(f"Dash Symbol =-=~= {dash_symbol}\n")
          file.write(f"Arrow Mode =-=~= {arrow_mode}\n")
          file.write("Debug Mode =-=~= off\n")
          file.write(f"⎎ℇ⍧☈ℇ⍑ ⍓⍲⍑☈⟟🝍 =-=~= {secret_matrix_mode}")
          file.close()
        get_settings_value()
        time.sleep(2)
        settings_main()

      else:
        print(f"\n{Fore.RED}{'~'*28}Invalid Choice{'~'*28}{Fore.WHITE}")
        time.sleep(1)

  elif settings_option == "arrow mode":
    while True:
      clear_screen()
      arrow_dash_or_no(arrow_mode)
      print(f"{Fore.RED}{arrow_mode_ascii}{Fore.WHITE}")
      arrow_dash_or_no(arrow_mode)
      arrow_status = f"{Fore.LIGHTGREEN_EX}{arrow_mode}{Fore.WHITE}" if arrow_mode == "on" else f"{Fore.RED}{arrow_mode}{Fore.WHITE}"
      print(f"\nCurrent Arrow Mode - {arrow_status}\n")
      arrow_dash_or_no(arrow_mode)
      arrow_mode_option = str(
          input("\nNew mode ('return' to go back) -> ")).lower()
      if arrow_mode_option == "on":
        print()
        arrow_dash_or_no(arrow_mode)
        print(f"\n{Fore.LIGHTGREEN_EX}Arrow mode is now active.{Fore.WHITE}\n")
        arrow_dash_or_no(arrow_mode)
        with open(matching_files, "w") as file:
          file.write(f"Dash Symbol =-=~= {dash_symbol}\n")
          file.write("Arrow Mode =-=~= on\n")
          file.write(f"Debug Mode =-=~= {debug_mode}\n")
          file.write(f"⎎ℇ⍧☈ℇ⍑ ⍓⍲⍑☈⟟🝍 =-=~= {secret_matrix_mode}")
          file.close()
        get_settings_value()
        time.sleep(2)
        settings_main()

      elif arrow_mode_option == "off":
        print()
        arrow_dash_or_no(arrow_mode)
        print(f"\n{Fore.RED}Arrow mode is now inactive.{Fore.WHITE}\n")
        arrow_dash_or_no(arrow_mode)
        with open(matching_files, "w") as file:
          file.write(f"Dash Symbol =-=~= {dash_symbol}\n")
          file.write("Arrow Mode =-=~= off\n")
          file.write(f"Debug Mode =-=~= {debug_mode}\n")
          file.write(f"⎎ℇ⍧☈ℇ⍑ ⍓⍲⍑☈⟟🝍 =-=~= {secret_matrix_mode}")
          file.close()
        get_settings_value()
        time.sleep(2)
        settings_main()

      else:
        print(f"\n{Fore.RED}{'~'*28}Invalid Choice{'~'*28}{Fore.WHITE}")
        time.sleep(1)

  elif settings_option == "dash symbol":
    clear_screen()
    print("dash symbol")

  elif settings_option == "101 secret matrix unlock":
    secret_matrix_main()

  elif settings_option == "return":
    clear_screen()
    quizzer_main()

  else:
    print(f"\n{Fore.RED}{'~'*28}Invalid Choice{'~'*28}{Fore.WHITE}")
    time.sleep(1)
    settings_main()


# Function - ian_joshua_goh_is_very_fat_main():
def ian_joshua_goh_is_very_fat_main():
  count = 0
  while True:
    count = random.randint(1, 15)
    time.sleep(0.25)
    clear_screen()
    clear_screen()
    if count == 1:
      print(f"{Fore.RED}{john_pork_ascii}{Fore.WHITE}")
    elif count == 2:
      print(f"{Fore.WHITE}{john_pork_ascii}{Fore.WHITE}")
    elif count == 3:
      print(f"{Fore.BLACK}{john_pork_ascii}{Fore.WHITE}")
    elif count == 4:
      print(f"{Fore.GREEN}{john_pork_ascii}{Fore.WHITE}")
    elif count == 5:
      print(f"{Fore.YELLOW}{john_pork_ascii}{Fore.WHITE}")
    elif count == 6:
      print(f"{Fore.BLUE}{john_pork_ascii}{Fore.WHITE}")
    elif count == 7:
      print(f"{Fore.MAGENTA}{john_pork_ascii}{Fore.WHITE}")
    elif count == 8:
      print(f"{Fore.CYAN}{john_pork_ascii}{Fore.WHITE}")
    elif count == 9:
      print(f"{Fore.LIGHTRED_EX}{john_pork_ascii}{Fore.WHITE}")
    elif count == 10:
      print(f"{Fore.LIGHTGREEN_EX}{john_pork_ascii}{Fore.WHITE}")
    elif count == 11:
      print(f"{Fore.LIGHTBLUE_EX}{john_pork_ascii}{Fore.WHITE}")
    elif count == 12:
      print(f"{Fore.LIGHTMAGENTA_EX}{john_pork_ascii}{Fore.WHITE}")
    elif count == 13:
      print(f"{Fore.LIGHTCYAN_EX}{john_pork_ascii}{Fore.WHITE}")
    elif count == 14:
      print(f"{Fore.LIGHTWHITE_EX}{john_pork_ascii}{Fore.WHITE}")
    elif count == 15:
      print(f"{Fore.LIGHTBLACK_EX}{john_pork_ascii}{Fore.WHITE}")


# Function - gay_glorious_goose_tastic_main()
def gay_glorious_goose_tastic_main():
  clear_screen()
  print(gay_girl_ascii)
  print(gay_goose_ascii)
  print(gay_frog_ascii)
  print(gay_girl_ascii)
  print(gay_goose_ascii)
  print(gay_frog_ascii)
  while True:
    print(gay_girl_ascii)
    print(gay_goose_ascii)
    print(gay_frog_ascii)

    
# Function - education_level()
def education_level():
  while True:
    clear_screen()
    arrow_dash_or_no(arrow_mode)
    print(f"{Fore.RED}{questions_ascii}{Fore.WHITE}")
    arrow_dash_or_no(arrow_mode)
    print('''\nEducation Level:
- Primary School
- Secondary School
- Polytechnic
- Junior College
- University\n''')
    arrow_dash_or_no(arrow_mode)
    education_level_option = str(input("\nChoice ('return' to go back) -> ")).lower()
    if education_level_option == "primary school":
      clear_screen()
      return "primary"
    elif education_level_option == "secondary school":
      clear_screen()
      return "secondary"
    elif education_level_option == "polytechnic":
      clear_screen()
      return "polytechnic"
    elif education_level_option == "junior college":
      clear_screen()
      return "junior"
    elif education_level_option == "university":
      clear_screen()
      return "university"
    elif education_level_option == "return":
      clear_screen()
      quizzer_main()
    else:
      print(f"\n{Fore.RED}{'~'*28}Invalid Choice{'~'*28}{Fore.WHITE}")
      time.sleep(1)


# Function - subject_chooser()
def subject_chooser():
  while True:
    clear_screen()
    arrow_dash_or_no(arrow_mode)
    print(f"{Fore.RED}{subject_chooser_ascii}{Fore.WHITE}")
    arrow_dash_or_no(arrow_mode)
    extra_subjects = education_level()
    print("\nSubjects avaliable:\n- English\n- Chinese")
    if extra_subjects == "primary":
      print("- Math\n- Science\n")
    elif extra_subjects == "secondary":
      print("- A-Math\n- E-Math\n- Physics\n- Chemistry\n- Biology\n- History\n- Geography\n- Computing\n")
    elif extra_subjects == "polytechnic":
      print("- Biology\n- Chemistry\n- Physics\n- E-Math\n- A-Math\n- Computing\n- History\n- Geography\n")
    elif extra_subjects == "junior":
      print("- Biology\n- Chemistry\n- Physics\n- E-Math\n- A-Math\n- Computing\n- History\n- Geography\n")
    elif extra_subjects == "university":
      print("- Biology\n- Chemistry\n- Physics\n- E-Math\n- A-Math\n- Computing\n- History\n- Geography\n")
    arrow_dash_or_no(arrow_mode)
    
    


# Function - add_questions_main()
def add_questions_main():
  exit()
  


# Function - quizzer_main()
def quizzer_main():
  get_settings_value()
  clear_screen()
  arrow_dash_or_no(arrow_mode)
  print(f"{Fore.RED}{subject_quizzer_ascii}{Fore.WHITE}")
  arrow_dash_or_no(arrow_mode)
  print('''\nOptions:
- Start Quiz
- Questions
- Leaderboard
- Settings
- Exit\n''')
  arrow_dash_or_no(arrow_mode)
  quizzer_options_choice = str(input("\nChoice -> ")).lower()
  if quizzer_options_choice == "start quiz":
    clear_screen()
    arrow_dash_or_no(arrow_mode)
    print(f"{Fore.RED}{start_quiz_ascii}{Fore.WHITE}")
    arrow_dash_or_no(arrow_mode)

  elif quizzer_options_choice == "questions":
    clear_screen()
    arrow_dash_or_no(arrow_mode)
    print(f"{Fore.RED}{questions_ascii}{Fore.WHITE}")
    arrow_dash_or_no(arrow_mode)

  elif quizzer_options_choice == "leaderboard":
    clear_screen()
    arrow_dash_or_no(arrow_mode)
    print(f"{Fore.RED}{leaderboard_ascii}{Fore.WHITE}")
    arrow_dash_or_no(arrow_mode)

  elif quizzer_options_choice == "settings":
    settings_main()

  elif quizzer_options_choice == "exit":
    clear_screen()
    arrow_dash_or_no(arrow_mode)
    print(f"{Fore.RED}{exit_ascii}{Fore.WHITE}")
    arrow_dash_or_no(arrow_mode)
    print(
        f"{Fore.RED}Exiting...{Fore.GREEN} Time remaining - {random.randint(5,9)} seconds{Fore.WHITE}"
    )
    time.sleep(0.5)
    print(f"{Fore.RED}.{Fore.WHITE}")
    time.sleep(0.5)
    print(f"{Fore.RED}.{Fore.WHITE}")
    time.sleep(0.5)
    print(f"{Fore.RED}.{Fore.WHITE}")
    time.sleep(0.5)
    print(f"{Fore.RED}.{Fore.WHITE}")
    time.sleep(0.5)
    print(
        f"{Fore.RED}Halfway done exiting...{Fore.GREEN} Time remaining - {random.randint(2,3)} seconds{Fore.WHITE}"
    )
    time.sleep(0.5)
    print(f"{Fore.RED}.{Fore.WHITE}")
    time.sleep(0.5)
    print(f"{Fore.RED}.{Fore.WHITE}")
    time.sleep(0.5)
    print(f"{Fore.RED}.{Fore.WHITE}")
    time.sleep(0.5)
    print(f"{Fore.RED}.{Fore.WHITE}")
    time.sleep(0.5)
    print(f"{Fore.RED}Exited.{Fore.GREEN} Goodbye.{Fore.WHITE}")
    arrow_dash_or_no(arrow_mode)
    exit()

  elif secret_matrix_mode == "on" and quizzer_options_choice == "ian joshua goh is very fat":
    ian_joshua_goh_is_very_fat_main()
    
  elif secret_matrix_mode == "on" and quizzer_options_choice == "gay, glorious, goose-tastic":
    gay_glorious_goose_tastic_main()

  else:
    print(f"\n{Fore.RED}{'~'*28}Invalid Choice{'~'*28}{Fore.WHITE}")
    time.sleep(1)
    quizzer_main()


# Calling main function
quizzer_main()

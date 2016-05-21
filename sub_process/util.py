'''
utils for asr and interpreter scripts.


                                                                    Written by Hyungwon Yang
                                                                                2016. 05. 02
                                                                                   EMCS Labs
'''

import requests
import os
import re

from sub_process.dialogues import language_form


# Internet connection check.
def internet_check():

    try:
        requests.get("http://www.google.com", timeout=3)
    except IOError:
        print('\n Internet is not connected. Please connect the internet first.')
        os.system('say Internet is not connected. Please check the internet connection and try again.')
        return False

def lang_check(sentence):
    ref_dict = language_form()
    lang_list = list(ref_dict.keys())
    box,tmp = [],[]
    for line in lang_list:
        tmp = re.findall(line,sentence)
        if tmp:
            box.append(tmp[0])
    return box



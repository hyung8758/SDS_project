# SDS_project (Theona) + Interpreter
                                                                         Hyungwon Yang
                                                                            2016.05.20
                                                                              EMCS lab    

MacOSX (This script is not tested on Window and Linux)
----------------------------------------------------------------

Python 3.5
(This script was not tested on the other versions.)


PREREQUEISTE
------------
### SDS_project & Interpreter

- python 3 is required. This package is not running on python 2.
- Download the package and navigate to the SDS_project directory.
- Type '$python3 setup.py install' in the command line. (It only works on python3)


DIRECTION
---
### SDS_project


### Interpreter
1. Due to the tts issue, this program is running on mac.
    - voice : samantha
    - To install samantha voice..
        - Go System preference.
        - Click Dictation & Speech.
        - In the text to speech section, click customize.. or samantha in system voice bar.
        - Choose samantha and install the voice.

2. Two options are provided. 'slow' and 'fast'
    - slow(default): type '$python3 interpreter.py' or '$python3 interpreter.py slow'
                   in the terminal command line. It is tutorial mode which shows
                   all the procedures of interpretation.
    - fast: type '$python3 interpreter.py fast' then it will skip all the tutorial lines
          and activate fast translating mode.

3. Usage.
- 'slow' option: 
    - Tell your source and target languages to computer when it asks you. 
      Source language is input language (to be interpreted), and target
      language is output language (translated source language).
      ex) computer: What is your source language?
          You : English / It is English / My source language is English.
- 'fast' option:
    - Select your source and target languages directly and wait until computer
      set the language option. 
    - After beep sound, (you must wait 2-3 seconds after beep sound) speak 
      the sentence. 
    - Different beep sound will be generated and the translated sentence will
      be written on the screen and spoken simultaneously.
       
4. language Support.
    - Korean, English, Japanese, Chinese.

CONTENTS
---
Spoken Dialogue System: Theona.


Interpreter.


CONTACTS
---

Hosung Nam / hnam@korea.ac.kr

Hyungwon Yang / hyung8758@gmail.com


VERSION HISTORY
---
1.0. (2016.05.20)
1. It has three main scripts.
- simple_sds.py: simple sds tutorial that shows users of the procedures of the system.
- Theona.py: This is main script for sds project. I will focuse on this script.
- interpreter.py: Just for fun, this is basic interpreting system.



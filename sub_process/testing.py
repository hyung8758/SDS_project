'''
Testing system.


                                                                    Written by Hyungwon Yang
                                                                                2016. 05. 22
                                                                                   EMCS Labs
'''

import speech_recognition as sr

def speak_test():

    # Use recognizer to record the speech.
    recorder = sr.Recognizer()
    with sr.Microphone() as mike:
        print('Hello. Please speaking.')
        my_sound = recorder.listen(mike)
    tmp_words = recorder.recognize_google(my_sound)
    words = str(tmp_words)
    print(words)
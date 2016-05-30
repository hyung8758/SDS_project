'''
Testing system.


                                                                    Written by Hyungwon Yang
                                                                                2016. 05. 22
                                                                                   EMCS Labs
'''

import speech_recognition as sr

def speak_test(lang_opt='en'):

    # Use recognizer to record the speech.
    recorder = sr.Recognizer()
    with sr.Microphone() as mike:
        print('Please speaking.')
        my_sound = recorder.listen(mike)
    tmp_words = recorder.recognize_google(my_sound,language=lang_opt)
    words = str(tmp_words)
    print(words)

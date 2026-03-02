import os
import eel

eel.init('www')

eel.start('index.html', mode='chrome', host='localhost', block=True)
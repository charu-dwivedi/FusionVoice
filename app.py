import sys
sys.path.append("/usr/local/lib/python3.5/site-packages/")
from .LangProcess import speech
from .FusionVC import FusionVoiceCommands as fvc

def run(context):
    print("Imports work")
    print(speech.speechrec())
    fvc.run()
    
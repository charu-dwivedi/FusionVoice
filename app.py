import sys
sys.path.append("/usr/local/lib/python3.5/site-packages/")
from .LangProcess import nlpparse
from .LangProcess import speech
from .FusionVC import CommandSelect as cs
import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    '''
    print("Imports work")
    app = adsk.core.Application.get()
    ui  = app.userInterface 
    qatToolbar = ui.toolbars.itemById('NavToolbar')

    buttonExample = cmdDefs.addButtonDefinition('VoiceAssistant', 'Sample Button', 'Sample button tooltip', \
                                                 './/Resources//Sample')
    '''


    try:
        command = speech.speechrec() #'draw a circle with a radius of 16 inches'
        print('draw a circle with a radius of 16 inches')
        command_list = nlpparse.parse_sentence(command)
        cs.run_command(command_list)
    except ValueError as e:
        print('The machine does not seem to recognize some of the words in the command, try again.')
        print(e)
        
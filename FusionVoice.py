import sys
sys.path.append("/usr/local/lib/python3.5/site-packages/")
from .LangProcess import nlpparse
from .LangProcess import speech
from .FusionVC import CommandSelect as cs
import adsk.core, adsk.fusion, adsk.cam, traceback

handlers = []

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        # Get the CommandDefinitions collection.
        cmdDefs = ui.commandDefinitions
        
        # Create a button command definition.
        buttonSample = cmdDefs.addButtonDefinition('FusionVC2', 
                                                   'FusionVC', 
                                                   'Fusion Voice Control',
                                                   './Resources/Microphone')
        
        # Connect to the command created event.
        sampleCommandCreated = SampleCommandCreatedEventHandler()
        buttonSample.commandCreated.add(sampleCommandCreated)
        handlers.append(sampleCommandCreated)
        
        # Get the ADD-INS panel in the model workspace. 
        addInsPanel = ui.allToolbarPanels.itemById('SolidScriptsAddinsPanel')
        
        # Add the button to the bottom of the panel.
        buttonControl = addInsPanel.controls.addCommand(buttonSample)
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


# Event handler for the commandCreated event.
class SampleCommandCreatedEventHandler(adsk.core.CommandCreatedEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        eventArgs = adsk.core.CommandCreatedEventArgs.cast(args)
        cmd = eventArgs.command

        # Connect to the execute event.
        onExecute = SampleCommandExecuteHandler()
        cmd.execute.add(onExecute)
        handlers.append(onExecute)


# Event handler for the execute event.
class SampleCommandExecuteHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        eventArgs = adsk.core.CommandEventArgs.cast(args)

        # Code to react to the event.
        app = adsk.core.Application.get()
        ui  = app.userInterface
        prompt_command()
        #ui.messageBox('In command execute event handler.')



def stop(context):
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        
        # Clean up the UI.
        cmdDef = ui.commandDefinitions.itemById('MyButtonDefIdPython')
        if cmdDef:
            cmdDef.deleteMe()
            
        addinsPanel = ui.allToolbarPanels.itemById('SolidScriptsAddinsPanel')
        cntrl = addinsPanel.controls.itemById('MyButtonDefIdPython')
        if cntrl:
            cntrl.deleteMe()
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc())) 
  

def prompt_command():
    try:
        command = speech.speechrec() #'draw a circle with a radius of 16 inches'
        print(command)
        #print('draw a circle with a radius of 16 inches')
        command_list = nlpparse.parse_sentence(command)
        if len(command_list) > 0:
            cs.run_command(command_list)
        else:
            app = adsk.core.Application.get()
            ui  = app.userInterface
            ui.messageBox('Command not valid: ' + command)
    except ValueError as e:  
        app = adsk.core.Application.get()
        ui  = app.userInterface
        ui.messageBox('Command not valid: ' + command)

        
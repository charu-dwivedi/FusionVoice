
from . import FusionVoiceCommands as fvc
import adsk.core, adsk.fusion, adsk.cam, traceback


COMMAND_VERBS = {"saw":{}, "ate":{}, "walked":{}, "draw":{"circle":{"diameter":{}, "radius":fvc.draw_circle}}, "square":{"side":fvc.draw_square, None:fvc.draw_square}, \
    "design":{"gear":{}, "spring":{}}, "extrude":{"circle":fvc.extrude_object, "square":fvc.extrude_object, None:fvc.extrude_object, "sketch":fvc.extrude_object, "inches":fvc.extrude_object, "inch":fvc.extrude_object, "centimeter":fvc.extrude_object, "centimeters":fvc.extrude_object}, "millimeter":fvc.extrude_object, "millimeters":fvc.extrude_object,\
    "meters":fvc.extrude_object, "meters":fvc.extrude_object}, "open":{ "sketch":{None:fvc.open_sketch, "plane":fvc.open_sketch }}} 


def run_command(command_arr):
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface   
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        plane = "xy"
        rootComp = design.rootComponent
        sketches = rootComp.sketches
        numsketches = sketches.count
        curr_dict = COMMAND_VERBS
        command_arr = command_arr[0]
        for x in range(len(command_arr)):
            if (callable(curr_dict)):
                if numsketches > 0:
                    curr_dict(rootComp, sketches.item(numsketches-1), command_arr[x:])
                else:
                    curr_dict(rootComp, None, command_arr[x:])
            elif type(command_arr[x]) is list or type(command_arr[x]) is tuple:
                if len(command_arr[x]) > 0:
                    for y in command_arr[x]: 
                        if y in curr_dict:
                            curr_dict = curr_dict[y]
                            break
                else:
                    curr_dict = curr_dict[None]
            else:
                #print(type(command_arr[x]))
                if command_arr[x] in curr_dict:
                    curr_dict = curr_dict[command_arr[x]]
                else:
                    return 0
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
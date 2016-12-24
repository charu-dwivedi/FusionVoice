#Author-Charu Dwivedi
#Description-Writing the fusion drawing commands 

import adsk.core, adsk.fusion, adsk.cam, traceback


def open_sketch(designRootComp, lastsketch, command_arr):
    sketches = designRootComp.sketches
    plane = designRootComp.xYConstructionPlane
    if len(command_arr[0] > 0):
        if command_arr[0][0] == "yz" or command_arr[0][0] == "zy":
            plane = designRootComp.yZConstructionPlane
        elif command_arr[0][0] == "xz" or command_arr[0][0] == "zx":
            plane = designRootComp.xZConstructionPlane
    sketch = sketches.add(plane)
    
def draw_circle(designRootComp, lastsketch, command_arr, x=0, y=0, z=0):
    circles = lastsketch.sketchCurves.sketchCircles
    if len(command_arr[0] > 0):
        radius = float(command_arr[0][0][0])
    else:
        radius = 5
    circle1 = circles.addByCenterRadius(adsk.core.Point3D.create(x, y, z), radius)

def extrude_object(designRootComp, lastsketch, command_arr):
    prof = lastsketch.profiles.item(0)
    extrudes = designRootComp.features.extrudeFeatures
    extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewComponentFeatureOperation)
    distance = adsk.core.ValueInput.createByReal(5)
    extInput.setDistanceExtent(False, distance)
    ext = extrudes.add(extInput)



'''

COMMAND_VERBS = {"saw":{}, "ate":{}, "walked":{}, "draw":{"circle":{"diameter":{}, "radius":draw_circle}}, "square":{"side":{}}, \
    "design":{"gear":{}, "spring":{}}, "extrude":{"circle":{}, "square":{}, "(none)":{} }, "open":{ "sketch":{"(none)":{}} }} 


def run_command(command_arr):
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        ui.messageBox('New sketch?')        
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        plane = "xy"
        rootComp = design.rootComponent
        open_sketch(plane, rootComp)
        sketches = rootComp.sketches
        numsketches = sketches.count
        curr_dict = COMMAND_VERBS
        command_arr = command_arr[0]
        for x in range(len(command_arr)):
            if (callable(curr_dict)):
                curr_dict(rootComp, sketches.item(numsketches-1), command_arr[x:])
            elif type(command_arr[x]) is list or type(command_arr[x]) is tuple:
                for y in command_arr[x]: 
                    if y in curr_dict:
                        curr_dict = curr_dict[y]
                        break
            else:
                #print(type(command_arr[x]))
                if command_arr[x] in curr_dict:
                    curr_dict = curr_dict[command_arr[x]]
                else:
                    return 0
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
'''
'''
def run():
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        ui.messageBox('New sketch?')        
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        plane = "xy"
        rootComp = design.rootComponent
        openSketch(plane, rootComp)
        sketches = rootComp.sketches
        numsketches = sketches.count
        drawCircle(rootComp, sketches.item(numsketches-1), 0, 0, 0, 3)
        extrudeObject(rootComp, sketches.item(numsketches-1))
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

'''


#print(type(COMMAND_VERBS["draw"]["circle"]["radius"]))
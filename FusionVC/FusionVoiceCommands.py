#Author-Charu Dwivedi
#Description-Writing the fusion drawing commands 

import adsk.core, adsk.fusion, adsk.cam, traceback



def run():
    ui = None
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

def openSketch(plane, designRootComp):
    sketches = designRootComp.sketches
    xyPlane = designRootComp.xYConstructionPlane
    sketch = sketches.add(xyPlane)
    
def drawCircle(designRootComp, lastsketch, x, y, z, radius):
    circles = lastsketch.sketchCurves.sketchCircles
    circle1 = circles.addByCenterRadius(adsk.core.Point3D.create(x, y, z), radius)

def extrudeObject(designRootComp, lastsketch):
    prof = lastsketch.profiles.item(0)
    extrudes = designRootComp.features.extrudeFeatures
    extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewComponentFeatureOperation)
    distance = adsk.core.ValueInput.createByReal(5)
    extInput.setDistanceExtent(False, distance)
    ext = extrudes.add(extInput)
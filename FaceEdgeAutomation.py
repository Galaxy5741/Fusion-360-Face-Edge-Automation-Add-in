#Description-Simple auto-starting face/edge automation add-in

import adsk.core, adsk.fusion, traceback
import ctypes
import time

# Global variables
app = adsk.core.Application.get()
ui = app.userInterface
isRunning = False
last_selection_id = None

def check_and_process_selection():
    """Our proven working detection logic"""
    global last_selection_id
    
    try:
        # IF a command dialog is open, don't interfere
        if ui.activeCommand != 'SelectCommand':
            return False
            
        # IF nothing selected, do nothing
        if ui.activeSelections.count == 0:
            last_selection_id = None
            return False
        
        # Get current selection
        selection = ui.activeSelections.item(0)
        entity = selection.entity
        current_id = id(entity)
        
        # IF same selection as before, do nothing
        if current_id == last_selection_id:
            return False
            
        # Something new selected - update tracking
        last_selection_id = current_id
        
        # IF it's a face THEN trigger extrude
        face = adsk.fusion.BRepFace.cast(entity)
        if face:
            # Trigger extrude (E key) immediately
            ctypes.windll.user32.keybd_event(0x45, 0, 0, 0)
            ctypes.windll.user32.keybd_event(0x45, 0, 0x0002, 0)
            return True
        
        # IF it's an edge THEN trigger fillet  
        edge = adsk.fusion.BRepEdge.cast(entity)
        if edge:
            # Trigger fillet (F key) immediately
            ctypes.windll.user32.keybd_event(0x46, 0, 0, 0)
            ctypes.windll.user32.keybd_event(0x46, 0, 0x0002, 0)
            return True
            
        return False
        
    except:
        return False

def run(context):
    """Add-in startup - run the simple monitoring loop"""
    global isRunning, last_selection_id
    
    try:
        isRunning = True
        last_selection_id = None
        
        # Infinite monitoring loop - just like the working 30-second version
        while isRunning:
            try:
                # Check for selection changes
                if check_and_process_selection():
                    # Something was triggered - brief pause
                    time.sleep(0.5)
                    last_selection_id = None
                else:
                    # Nothing happened - short check interval
                    time.sleep(0.2)
                
                # Let Fusion process other events
                adsk.doEvents()
                
            except:
                # Keep running even if errors occur
                time.sleep(0.5)
                
    except Exception as e:
        isRunning = False
        if ui:
            ui.messageBox(f'Face/Edge automation stopped: {str(e)}')

def stop(context):
    """Add-in shutdown"""
    global isRunning
    isRunning = False
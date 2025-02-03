import maya.cmds as cmds
import os
from maya.mel import eval as mel_eval
from PySide2 import QtWidgets

def debug_import_set():
    """Debugging version of import_set to show errors and ensure correct execution."""
    file_dialog = QtWidgets.QFileDialog()
    file_path, _ = file_dialog.getOpenFileName(
        caption="Open Set Data",
        filter="Text Files (*.txt)"
    )

    if not file_path:
        cmds.warning("Import cancelled.")
        return

    print(f"Reading from file: {file_path}")

    # Read set data from file
    with open(file_path, 'r') as f:
        lines = f.readlines()

    if not lines:
        cmds.warning("The selected file is empty.")
        return

    for line in lines:
        line = line.strip()
        if not line:
            continue  # Skip empty lines

        # Ensure correct format
        if ':' not in line:
            cmds.warning(f"Skipping malformed line: {line}")
            continue

        # Splitting safely: Set name is the first part, rest are members
        split_index = line.index(':')  # Find first colon
        set_name = line[:split_index].strip()
        members = line[split_index+1:].split(',')

        # Print debug information
        print(f"Set Name: {set_name}")
        print(f"Members: {members}")

        # Ensure members exist in the scene
        valid_members = [m for m in members if cmds.objExists(m)]

        if not valid_members:
            cmds.warning(f"Skipping set '{set_name}' because no valid members exist in the scene.")
            continue

        # Create the set if it doesn't exist
        if not cmds.objExists(set_name):
            cmds.sets(name=set_name)
            print(f"Created new set: {set_name}")

        # Add members to the set
        cmds.sets(valid_members, add=set_name)
        print(f"Added members to set: {set_name}")

    cmds.confirmDialog(title="Import Complete", message=f"Set imported from:\n{file_path}")

# Run the debug import function
debug_import_set()

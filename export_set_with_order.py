import maya.cmds as cmds
import os
from maya.mel import eval as mel_eval
from PySide2 import QtWidgets

def export_selected_set_with_order():
    """Exports the selected set with the order preserved based on current selection."""
    selected_objects = cmds.ls(sl=True)  # Get current selection in order
    selected_sets = cmds.ls(sl=True, sets=True)

    if not selected_sets:
        cmds.warning("No set selected. Please select a set and try again.")
        return

    selected_set = selected_sets[0]  # Use the first selected set
    set_members = cmds.sets(selected_set, q=True)  # Get all members of the set

    if not set_members:
        cmds.warning(f"Selected set '{selected_set}' has no members.")
        return

    # Filter the selection to ensure it matches only valid set members
    ordered_members = [obj for obj in selected_objects if obj in set_members]

    if not ordered_members:
        cmds.warning("No valid set members found in the current selection.")
        return

    # Get project root directory
    project_root = mel_eval('workspace -q -rd')

    # Open a file dialog for user to choose save location
    file_dialog = QtWidgets.QFileDialog()
    file_path, _ = file_dialog.getSaveFileName(
        caption="Save Set Data",
        dir=os.path.join(project_root, f"{selected_set}.txt"),
        filter="Text Files (*.txt)"
    )

    # If the user cancels, exit
    if not file_path:
        cmds.warning("Export cancelled.")
        return

    # Save set data to file in the selection order
    with open(file_path, 'w') as f:
        f.write(f"{selected_set}:{','.join(ordered_members)}\n")

    cmds.confirmDialog(title="Export Complete", message=f"Set '{selected_set}' saved to:\n{file_path}")

export_selected_set_with_order()

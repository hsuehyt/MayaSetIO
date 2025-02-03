# MayaSetIO

**Tools for exporting and importing Maya sets with preserved order.**

---

## Overview

MayaSetIO is a simple Python-based toolkit for **Autodesk Maya** that allows users to:
- Export selected sets while preserving the order of selection.
- Import sets back into Maya from text files.

This repository is useful for animators, riggers, and technical artists who need to transfer selection sets across projects while maintaining the exact order of objects.

---

## Features

- **Export Sets:** Save selected sets and their members to a `.txt` file with order intact.
- **Import Sets:** Recreate sets in Maya from exported `.txt` files.
- Supports **custom directory and file naming** for exports.
- Uses the Maya **project root directory** as the default location.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hsuehyt/MayaSetIO.git
   ```

2. Copy the `export_set_with_order.py` and `import_set.py` scripts into your desired directory.

3. Open **Maya** and load the scripts into the **Script Editor** or Maya's Python environment.

---

## Usage

### Exporting a Set
1. **Select a Set and Its Members:**
   - Select the desired set in the **Outliner**.
   - Select the set's members in the desired order in Maya.

2. **Run the Export Script:**
   - Load and execute `export_set_with_order.py` in the Script Editor.
   - Choose the file location and name via the file dialog (default: project root).

3. **Output File:**
   - A `.txt` file is generated containing the set name and ordered members.

---

### Importing a Set
1. **Run the Import Script:**
   - Load and execute `import_set.py` in the Script Editor.
   - Select the exported `.txt` file via the file dialog.

2. **Check the Imported Set:**
   - The set and its members will be recreated in Maya.

---

## File Format

Exported `.txt` files have the following format:
```
SetName:member1,member2,member3,...
```

Example:
```
Set_Spines:Dragon:FKRoot_M,Dragon:FKNeck1_M,Dragon:FKSpine5_M
```

---

## Scripts

### `export_set_with_order.py`
Exports the selected set to a `.txt` file while preserving the order of selection.

### `import_set.py`
Imports a set from a `.txt` file and recreates it in Maya.

---

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this toolkit. Contributions are welcome!

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Author

Created by [hsuehyt](https://github.com/hsuehyt). 🚀
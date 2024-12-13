# Rename-SEMpics
Add the missing name parts to the SEM pictures.
Currently, only the date is missing when SEM pictures are taken.

## How to interact with the script
### Preparation
Copy `main.py` in the directory with the `.tif` files that are newly copied from the SEM devivce. 
### Scipt
1. Run the script by executing `main.py`.
2. You will be prompted to select a mode:
   - Enter `0` to insert a date into the filenames of `.tif` files.
   - Enter `1` to change the date in the filenames of `.tif` files.
3. Enter the date in the format `YYMMDD` when prompted.
4. The script will rename the `.tif` files in the current directory and attempt to do the same in the `PlainImages` directory if it exists.
5. Press Enter to exit the script.
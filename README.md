# face-recognition

This project contains a script for usage with ageitgey/face_recognition app.


1. Follow the guidelines in https://github.com/ageitgey/face_recognition project 
   and install the app.

2. Add all pictures of identified faces to ./img/known directory.

3. Pull the script rename.py from this project and run it.
   Since the app works by having all the images of different people in one directory (not in separate subdirectories),
   then all image files should have identifiers in the filename.
   This script renames all files in subdirectories by the directory name + number in series, e.g Jon Bovi1, Jon Bovi2 etc.

4. Move all image files out from their subdirectories to directory ./img/known :
   ```bash
   find . -mindepth 2 -type f -print -exec mv {} . \;
   ```
5. Run the app!
   ```bash
   face_recognition ./img/known ./img/unknown
   ```

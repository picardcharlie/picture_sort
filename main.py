# Sort pictures in a file, move camera photos into one folder and not camera photos (memes)
# into a different one.  Will add features later.  yeet.
#

import os
import re

# get current directory, want to add option to find it with QT interface later.
basedir = os.path.abspath(os.path.dirname(__file__))

# lists all files inside of the directory
all_files = os.listdir(basedir)

# iterate over all files
for file in all_files:

    #if it's a camera photo
    if file == True:
        print("it's a camera photo")

        # will add separating them into different folders based off of date.

    #if it's not a camera photo
    else:
        print("it's a meme")
        memes_dir = os.path.join(basedir, "memes")
        if "memes" not in all_files:
            os.mkdir(memes_dir)
            os.rename((os.path.join(basedir, file)), (os.path.join(memes_dir, file)))

        else:
            os.rename((os.path.join(basedir, file)), (os.path.join(memes_dir, file)))



# gotta figure out regex for photos.  current format is ########_######.jpg
# the first eight digits are year, month, date. 20220913 example.
file_name = "20211004_184567.jpg"

check_picture = re.findall("[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9][0-9][0-9].jpg", file_name)

if check_picture != None:
    print(check_picture)
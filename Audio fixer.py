"""
Audio fixer.py is a python script file which uses the meta data to rename the audio files and based on their metadata
stores them in their individual directories created as per their album names.
"""

import os
import eyed3
import shutil

def nomenclature(fname):
    """
    The function takes a string as an argument and process the string to make it an eligible file name as per the
    windows specification. The following are reserved characters in windows and can't be used:
    < (less than)
    > (greater than)
    : (colon)
    " (double quote)
    / (forward slash)
    \ (backslash)
    | (vertical bar or pipe)
    ? (question mark)
    * (asterisk)

    :return: a string which can be used as a file name in as per Windows namespace
    """
    filename = ""
    Reserved = ['<','>','"','/','\\','|','?','*']
    #Iterate over each character of the string given as the argument
    for letter in fname:
        if letter in Reserved: # if the letter is a reserved character then replace it with space " "
            filename = filename + " "
        elif letter == ':': #if the letter is a colon(:) reserved character then replace it with "-"
            filename = filename + "-"
        else: # if it is neither of them then just process it normally
            filename = filename + letter
    return filename

def file_mover(audiofilename,albumname):
    """
    It moves the audio file to the specified directory as per the album name. If the directory already exists then it
    moves the file in that directory else it creates a new directory and moves it there.

    :return: Nothing
    """
    source = os.path.join('E:\\backup\\mp3\\',audiofilename)#audiofilename should be with .mp3 extension
    destination = os.path.join('E:\\','albumname')
    if os.path.isdir(destination) is True:
        shutil.move(source, destination)
    else:
        os.makedirs(destination)
        shutil.move(source, destination)

files = os.listdir('E:\\backup\\mp3')
for file in files:
    try:
        audio = eyed3.load(file)
        tag = eyed3.id3.Tag()
        title = tag.title
        track_num = tag.track_num
        album = tag.album

        if (title is not None) | (album is not None):
            newfilename = title + " - " + album
            newfilename = nomenclature(newfilename)
            newfilename = '.'.join([newfilename,'mp3'])
            os.rename(file, newfilename)
            file_mover(newfilename,album)

        else:
            shutil.move(file,'E:\\backup\\Unsupported MP3')

    except:
        print " error found with the file"

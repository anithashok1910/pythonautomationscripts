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
    windows specification. The following reserved characters:
    < (less than)
    > (greater than)
    : (colon)
    " (double quote)
    / (forward slash)
    \ (backslash)
    | (vertical bar or pipe)
    ? (question mark)
    * (asterisk)

    :return: a string which can be used as a file name in windows
    """
    filename = ""
    Reserved = ['<','>',':','"','/','\','|','?','*']
    for letter in fname:
        if letter in
def file_mover():
    """

    :return:
    """

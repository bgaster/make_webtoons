# Create index.html for very basic "webtoon"
# 
# The idea is that you provide a set of JPGs, in a directory, which must be 
# formated to 750x1000px and it will stitch them together into a webpage.
#
# NOTE: It uses relative paths and so must be run from the directory where index.html is to be created
#       relative to the images themselves.

import sys
import glob
import os

# handle command line args first, we are only expecting one, the directory with the images in
arguments = len(sys.argv) - 1

if arguments != 1:
    print("USAGE: make_webtoon.py <images directory>")
    sys.exit()

directory = sys.argv[1]

# script directory as this is where the HTML templates are
script_path = os.path.dirname(os.path.realpath(__file__))

with open(script_path + '/prefix_html', 'r') as file:
    prefix_data = file.read()

jpegs = [f for f in glob.glob(directory + "/*.jpg")]
jpegs.reverse()

print(prefix_data)

for file in jpegs:
    print("<tr>\n  <td>\n    <img src=\"" + file + "\" width=\"750\" height=\"1000\" alt=\"\">\n  </td>\n</tr>")

with open(script_path + '/postfix_html', 'r') as file:
    postfix_data = file.read()

print(postfix_data)
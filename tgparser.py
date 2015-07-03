import re
import pdb
import optparse
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-i", "--FileIn", action="store", type="string", dest="filename", help="File to read in")

parser.add_option("-o", "--FileOut", action="store", type="string", dest="fileout", help="File output")

parser.add_option("-c", "--contact", action="store", type="string", dest="contact", help="Contact Name")

(options, args) = parser.parse_args()

def tgParse(filename, fileout, contact):
    log = open(filename, "r")
    output = open(fileout, "w")

    for line in log:
        name = re.findall(contact, line)
        text = re.findall('\>(.*?)\x1b', line)
        text2 = re.findall('\<(.*?)\x1b', line)
        
        list1 = name + text + text2
        string = " ".join(list1)
        output.write(string + '\n')
        
    log.close()
    output.close()

tgParse(options.filename, options.fileout, options.contact)

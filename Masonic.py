import os
import sys

from optparse import OptionParser
from masonic import Build

def main(argv):
    
    parser = OptionParser(usage="%prog [-f] [-q]", version="%prog 0.0.1")
    parser.add_option("-s", "--source", dest="source",
                      help="read content from source PATH",  metavar="PATH")
    parser.add_option("-d", "--destination", dest="destination",
                      help="write site to destination PATH", metavar="PATH")
    parser.add_option("-l", "--layouts", dest="layouts",
                      help="Folder containing layout files")
    
    (options, args) = parser.parse_args()
    
    if len(args):
        parser.error("Incorrect number of arguments.")
        
    if not options.layouts:
        options.layouts = "layouts"
    
    build = Build(options.source, options.destination, options.layouts)
    build.deploy()

if __name__ == "__main__":
    main(sys.argv[1:]) # Skips program name
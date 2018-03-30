import argparse
import ConfigParser
import subprocess
from MonitorClient import MonitorClient

def ConfigSectionMap(Config,section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f",help="File name")
    args = parser.parse_args()
    filename=args.f
    print filename    
    Config = ConfigParser.ConfigParser()
    Config.read(filename)

    for section in Config.sections():
        print section
        dict1=ConfigSectionMap(Config,section)

        c1=MonitorClient(dict1)
        c1.start()
        c1.join()

if __name__=='__main__':
    main()
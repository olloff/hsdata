#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, getopt, xml.etree.ElementTree as ElementTree;

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

def parseXml(inputfile, outputfile):

    xmlTree = ElementTree.parse(inputfile)
    xmlRoot = xmlTree.getroot();

    for Entity in xmlRoot.iter('Entity'):
        for Tag in Entity.findall('Tag'):
            for Lang in list(Tag):
                try:
                    if Lang.tag != 'ruRU':
                        Tag.remove(Lang);
                        uprint('removed ',Tag.get('enumID'),Lang.tag);
                except IndexError:
                    continue;

    xmlTree.write(outputfile, encoding="utf-8",);

        #raise Exception('ERR: ',Tag.attrib,' is not iterable');
        #root.remove(deDE);

    #
    #print(xmlRoot[0][1][10].text);


def main(argv):
    #global inputfile, outputfile;
    inputfile = '';
    outputfile = '';
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="]);
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>');
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>');
            sys.exit();
        elif opt in ("-i", "--ifile"):
            inputfile = arg;
        elif opt in ("-o", "--ofile"):
            outputfile = arg;
        if inputfile == outputfile:
            raise Exception('ERR: input- and outputfiles cannot be the same');
            sys.exit();
    print('Input file is ', inputfile);
    print('Output file is ', outputfile);

    parseXml(inputfile, outputfile);

if __name__ == "__main__":
    main(sys.argv[1:]);

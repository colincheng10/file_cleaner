import os
import hashlib
import logging
import sys
import getopt
import csv

def get_md5(filename):
    s = os.path.getsize(filename)
    m = hashlib.md5()
    
    mfile = open(filename, "rb")

    if s > 100*1000*1000:
        print ("file > 100MB: ", s)
        m.update(mfile.read(100*1000*1000))
    else:
        # print ("file size = ", s)
        m.update(mfile.read())

    mfile.close()

    md5_value = m.hexdigest()
    
    return md5_value

def get_urllist(dirname):
    urlList=[]
    for dirpath,dirnames,filenames in os.walk(dirname):
        for filename in filenames:
            url = os.path.join(dirpath,filename)

            #if os.path.isfile(url) == True and os.path.getsize(url) > 4096: 
            if os.path.isfile(url) == True : 
                urlList.append(url)
    return  urlList

def main(argv):
    baseDir = ''
    outFile = ''

    if len(sys.argv) != 5:
        print ('scanner.py -i dir -o output.csv')
        return

    try:
        opts, args = getopt.getopt(argv, "hi:o:")
    except getopt.GetoptError:
        print ('scanner.py -i dir -o output.csv')
        return

    for opt, arg in opts:
        if opt == '-h':
            print ('scanner.py -i dir -o output.csv')
            sys.exit()
        elif opt == '-i':
            baseDir = arg
        elif opt == '-o': 
            outFile = arg

    print ("base dir = ", baseDir)
    print ("output csv = ", outFile)

    print ("procsss: ", baseDir)
    baseList = get_urllist(baseDir)

    # csv line: dirpath/filename, md5
    print ("write: ", outFile)
    with open(outFile, 'w', newline='') as outF: 
        outWriter = csv.writer(outF)

        for a in baseList: 
            md5 = get_md5(a)
            outWriter.writerow([a, md5])

if __name__ == '__main__':
    main(sys.argv[1:])
    

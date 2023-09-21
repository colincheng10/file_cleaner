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
    extrDir = ''

    if len(sys.argv) != 5:
        print ('scanner.py -b dir1 -e dir2')
        return

    try:
        opts, args = getopt.getopt(argv, "hb:e:")
    except getopt.GetoptError:
        print ('scanner.py -b dir1 -e dir2')
        return

    for opt, arg in opts:
        if opt == '-h':
            print ('scanner.py -b dir1 -e dir2')
            sys.exit()
        elif opt == '-b':
            baseDir = arg
        elif opt == '-e': 
            extrDir = arg

    print ("base dir = ", baseDir)
    print ("extr dir = ", extrDir)

    baseList = get_urllist(baseDir)
    extrList = get_urllist(extrDir)

    baseFile = "base.csv"
    extrFile = "extr.csv"

    # csv line: dirpath/filename, md5
    print ("procsss: ", baseDir)
    with open(baseFile, 'w', newline='') as baseF: 
        baseWriter = csv.writer(baseF)

        for a in baseList: 
            md5 = get_md5(a)
            baseWriter.writerow([a, md5])

    print ("procsss: ", extrDir)
    with open(extrFile, 'w', newline='') as extrF:
        extrWriter = csv.writer(extrF)
        
        for b in extrList:
            md5 = get_md5(b)
            extrWriter.writerow([b, md5])

if __name__ == '__main__':
    main(sys.argv[1:])
    

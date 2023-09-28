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

    if s > 20*1000*1000:
        print ("file > 20MB: ", s)
        m.update(mfile.read(20*1000*1000))
    else:
        # print ("file size = ", s)
        m.update(mfile.read())

    mfile.close()

    md5_value = m.hexdigest()
    
    return md5_value,s

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
    total = len(baseList)
    print ("total: ", total)

    # csv line: dirpath/filename, md5
    print ("write: ", outFile)
    with open(outFile, 'w', newline='', encoding = 'utf-8') as outF: 
        outWriter = csv.writer(outF)

        index = 0
        count = total / 100
        percent = 0
        
        for a in baseList: 
            md5,size = get_md5(a)
            outWriter.writerow([a, md5, size])
            index += 1
            if index >= count:
                percent += 1
                index = 0
                print ('- %d %%' %(percent))

if __name__ == '__main__':
    main(sys.argv[1:])
    

import os
import logging
import sys
import getopt
import csv

def get_urllist(dirname):
    urlList=[]
    for dirpath,dirnames,filenames in os.walk(dirname):
        for filename in filenames:
            url = os.path.join(dirpath,filename)

            #if os.path.isfile(url) == True and os.path.getsize(url) > 4096: 
            if os.path.isfile(url) == True : 
                urlList.append(url)
    return  urlList

def skip_urllist(ignofile):
    ignoList = []
    print ("read config from ", ignofile)
    file = open(ignofile, 'r') 
    lines = file.readlines()
    for l in lines:
        #e = l.split(".")[-1]
        if len(l) > 1:
            #print('|->',l[:-1])
            ignoList.append(l[:-1])
    file.close()
    return ignoList

def main(argv):

    # to-be-del 
    delList=[]

    if len(sys.argv) != 5:
        print ('cleaner.py -b base.csv -e extr.csv')
        return

    try:
        opts, args = getopt.getopt(argv, "hb:e:")
    except getopt.GetoptError:
        print ('cleaner.py -b base.csv -e extr.csv')
        return

    for opt, arg in opts:
        if opt == '-h':
            print ('cleaner.py -b base.csv -e extr.csv')
            sys.exit()
        elif opt == '-b':
            baseFile = arg
        elif opt == '-e': 
            extrFile = arg

    print ("base csv = ", baseFile)
    print ("extr csv = ", extrFile)

    ignoList = skip_urllist("ignore.cfg")
    print ("ignore:", ignoList)

    # csv line: dirpath/filename, md5, size
    fieldnames = ['url', 'md5', 'size']

    with open(baseFile, 'r', encoding = 'utf-8') as baseF: 
        baseReader = csv.DictReader(baseF, fieldnames)
        baseList = [ row for row in baseReader]
        #print (baseList)
        #for line in baseReader:
        #    print (f" md5 of {line['url']} is {line['md5']}")

    with open(extrFile, 'r', encoding = 'utf-8') as extrF:
        extrReader = csv.DictReader(extrF, fieldnames)
        extrList = [ row for row in extrReader]
        #print (extrList)
        #for line in extrReader:
        #    print (f" md5 of {line['url']} is {line['md5']}")

    for aline in extrList:

        skip = 0
        for suffix in ignoList:
            if aline['url'].endswith(suffix):
                #print (f"skip: {aline['url']}")
                skip = 1
                break
        if skip == 1:
            continue

        for bline in baseList:
            if aline['md5'] == bline['md5'] and aline['size'] == bline['size'] and aline['url'] != bline['url']:
                print (f" md5 match: {aline['md5']} : [1] {aline['url']}, [2] {bline['url']}")
                delList.append(aline['url'])
                break
            else:
                continue
                #print (f" mismatch: {aline['md5']} and {bline['md5']}")

    # confirm to delete
    choice = input ("confirm to delete: [y|n]")
    if choice == 'y' :
        for url in delList:
            if os.path.exists(url):
                print (f" delete:", url)
                try:
                    os.remove(url)
                except Exception as e:
                    print ("Error:", e)
                    continue
            else:
                print(" The file does not exist: ", url)
    elif choice == 'n' :
        print ("skip delete")

if __name__ == '__main__':
    main(sys.argv[1:])
    

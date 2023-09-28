import os
import sys
import getopt

def scan_dir(dirPath):

    dirList = []

    for root, dirs, files in os.walk(dirPath):
        for d in dirs:
            dir_path = os.path.join(root, d)

            if os.path.isdir(dir_path):
                dirList.append(dir_path)

    return dirList

def remove_dir(dir_path):

    # Designate the directory path
    #dir_path = "/path/to/directory"

    # Check if the directory exists
    if os.path.exists(dir_path):
        # Get a list of files and subdirectories in the directory
        contents = os.listdir(dir_path)
    
        # Check if the directory is empty
        if not contents:
            # Remove the directory
            os.rmdir(dir_path)
            print(f"Directory '{dir_path}' removed successfully.")
        else:
            print(f"Directory '{dir_path}' is not empty.")
    else:
        print(f"Directory '{dir_path}' does not exist.")
    return

def main(argv):

    targetDir = ''

    if len(sys.argv) != 3:
        print ('remove_empty_dirs.py -d dir')
        return

    try:
        opts, args = getopt.getopt(argv, "hd:")
    except getopt.GetoptError:
        print ('remove_empty_dirs.py -d dir')
        return

    for opt, arg in opts:
        if opt == '-h':
            print ('remove_empty_dirs.py -d dir')
            sys.exit()
        elif opt == '-d':
            targetDir = arg

    print ("scan dir = ", targetDir)
    dirList = scan_dir(targetDir)

    #print (dirList)
    for d in dirList:
        try:
            remove_dir(d)
        except Exception as e:
            print ("Error:", e)
            continue

    print ("finished")

if __name__ == '__main__':
    main(sys.argv[1:])
    

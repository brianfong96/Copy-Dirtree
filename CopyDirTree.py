from shutil import copyfile

import argparse
import os

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Copies files of a certain type from source directory to destination directory while retaining the source directory subtree strucure')
    parser.add_argument('--src', type=str, required=True, 
                        action="store", dest="source_dir",
                        help='source directory, can either be relative or absolute')
    parser.add_argument('--dst', type=str, required=True, 
                        action="store", dest="dest_dir",
                        help='destination directory, can either be relative or absolute')
    parser.add_argument('--ft', type=str, required=True,
                        action="store", dest="file_type",
                        help='file type to copy')                    

    args = parser.parse_args()

    assert(os.path.isdir(args.source_dir)), "Source directory cannot be found."
    assert(os.path.isdir(args.dest_dir)), "Destination directory cannot be found."

    to_copy_dir = set()
    to_copy_file = list()
    # r=root, d=directories, f = files
    for root, dirs, files in os.walk(args.source_dir):
        for f in files:
            if f.endswith(args.file_type):                    
                to_copy_dir.add(root)
                to_copy_file.append(os.path.join(root, f))

    # Create Directories before copying files
    for d in to_copy_dir:
        relative = os.path.relpath(d, args.source_dir)
        dest = os.path.join(args.dest_dir, relative)
        try:
            os.makedirs(dest)
        except:
            print(d + " was already made")

    for f in to_copy_file:
        source = f
        relative = os.path.relpath(source, args.source_dir)
        dest = os.path.join(args.dest_dir, relative)        
        copyfile(source, dest)
        
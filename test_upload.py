#!/usr/bin/python
import flickr_api as f
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description='''Upload one file to a user.''')
    parser.add_argument('-f', '--filepath', help='Path to file.', required=True)

    args = parser.parse_args()

    if args.filepath:
        file_path = args.filepath
        auth_file_name = '.flickr_auth'
        home_dir = os.path.expanduser('~')
        auth_file = os.path.join(home_dir, auth_file_name)
        f.set_auth_handler(auth_file)
        f.upload(photo_file = file_path, title='Cake!!')

if __name__ == "__main__":
    main()

#!/usr/bin/python
import argparse
import flickr_api as f
import os
import stat

def main():
    parser = argparse.ArgumentParser(description='''Takes flickr API key and secret in order to create an access token file. \n
                                                See: http://www.flickr.com/services/api/keys/ for more information. \n
                                                Once key and secret are passed through arguments a URL will be printed where you \n
                                                need to authenticate with your flickr credentials to authorize permissions for \n
                                                py_flickr_backup_tool. When this is done a XML is generated where you need to \n
                                                extract the value of the <oath_verifier> tag and provide it to this script when \n
                                                prompted.''')
    parser.add_argument('-k', '--api_key', help='API key provided by flickr.', required=True)
    parser.add_argument('-s', '--api_secret', help='API secret provided by flickr.', required=True)

    args = parser.parse_args()

    if args.api_key and args.api_secret:
        auth_file_name = '.flickr_auth'
        f.set_keys(api_key = args.api_key, api_secret = args.api_secret) 
        auth_handler = f.auth.AuthHandler()
        url = auth_handler.get_authorization_url('write')
        print '\nPaste this url into your browser and authorize the app. Once that is done, copy and paste the value of <oath_verifier>.\n'
        print url
        #Hack for python 2 and 3 compability
        try: 
            input = raw_input
        except NameError: 
            pass
        oauth_verifier = input('\nOauth_verifier: ')
        auth_handler.set_verifier(oauth_verifier)

        home_dir = os.path.expanduser('~')
        auth_file = os.path.join(home_dir, auth_file_name)
        auth_handler.save(auth_file, include_api_keys = True)
        #Set filepermissions to 0600.
        os.chmod(auth_file, stat.S_IRUSR | stat.S_IWUSR)

        print 'Access token and key/secret is saved in file: %s' % auth_file

if __name__ == "__main__":
    main()

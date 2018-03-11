import sys
import argparse
import yaml
import deathbycaptcha


DEFAULT_TIMEOUT = 60
POLLS_INTERVAL = 5


def solve_captcha(username, password, file, type):
    client = deathbycaptcha.SocketClient(username, password)
    client.is_verbose = False

    try:
        print ('[*] Your balance is {} US cents'.format(client.get_balance()))
        captcha = client.decode(file, DEFAULT_TIMEOUT, type=type)
        if captcha:
            print ('[*] CAPTCHA {} solved: {}'.format(captcha['captcha'], captcha['text']))
    except deathbycaptcha.AccessDeniedException:
        print ('[*] AccesDeniedException: Access to DBC API denied, check your credentials and/or balance')

    return captcha['text']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('type', help='Which type of CAPTCHA', type=str, choices=['text', 'image'])
    parser.add_argument('file', help='Filename of CAPTCHA image', type=str)
    args = parser.parse_args()

    with open('creds.yaml') as file:
        creds = yaml.load(file)
    username = creds['DBCAPI']['USERNAME']
    password = creds['DBCAPI']['PASSWORD']

    if args.type=='text': typ = 0
    else:                 typ = 2

    solve_captcha(username, password, args.file, typ)



if __name__=='__main__':
    main()

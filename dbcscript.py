import sys
import deathbycaptcha


# Default CAPTCHA timeout and decode() polling interval
DEFAULT_TIMEOUT = 60
POLLS_INTERVAL = 5

def main():
    
    # sys.argv[1] will be the DBC account username and sys.argv[2] will be the account password
    client = deathbycaptcha.SocketClient(sys.argv[1], sys.argv[2])
    client.is_verbose = False

    # Printing the balance in the DBC account
    print ('Your balance is {} US cents'.format(client.get_balance()))
    try:
        for fn in sys.argv[3:]:
            try:
                # CAPTCHA image file name in sys.argv[3:]
                # DEFAULT TIMEOUT : the timeout
                captcha = client.decode(fn, DEFAULT_TIMEOUT)
            except Exception as e:
                sys.stderr.write('Failed uploading CAPTCHA: {}\n'.format(e))
                captcha = None

            if captcha:
                print('CAPTCHA {} solved: {}'.format(captcha['captcha'], captcha['text']))
                try:
                    client.report(captcha['captcha'])
                except Exception as e:
                    sys.stderr.write('Failed reporting CAPTCHA: {}\n'.format(e))

    except deathbycaptcha.AccessDeniedException:
        print('AccesDeniedException : Access to DBC API denied, check your credentials and/or balance')


if __name__=='__main__':
    main()

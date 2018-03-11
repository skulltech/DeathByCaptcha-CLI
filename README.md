# DeathByCaptcha-CLI
A CLI client for the DeathByCaptcha API

## Usage

```console
$ python3 dbcscript.py -h
usage: dbcscript.py [-h] {text,image} file

positional arguments:
  {text,image}  Which type of CAPTCHA
  file          Filename of CAPTCHA image

optional arguments:
  -h, --help    show this help message and exit
```


### Example usages

__For conventional text-based CAPTCHA__
```console
$ python3 dbcscript.py text captcha-conventional.jpg
[*] Your balance is 688.5848 US cents
[*] CAPTCHA 29683296 solved: following finding
```

__For image-based reCAPTCHA__
```console
$ python3 dbcscript.py image captcha-images.jpg
[*] Your balance is 688.3801 US cents
[*] CAPTCHA 1407357462 solved: [[75,237],[188,201],[180,440]]
```

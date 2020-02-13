try: # python 2
    while True:
        import urllib2 as req
        from sys import exit

        about_page = req.urlopen("http://localhost/builds-hackme/www/about.php").read()
        three = False
        if "KEY" in about_page:
            print(about_page)
            exit(0)

except ImportError: # python 3
    while True:
        import urllib.request as req
        from sys import exit

        about_page = req.urlopen("http://localhost/builds-hackme/www/about.php").read()
        three = True
        if b'KEY' in about_page:
            print(about_page)
            exit(0)

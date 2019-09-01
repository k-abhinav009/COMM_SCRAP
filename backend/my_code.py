def run(curr_wid, mainwin):
    def prog(url,out):
        import requests
        import re
        finds = []
        comments = "<\W*--.*?--\W*>"
        a = re.sub("\n|%0a", "", url)

        response = requests.get(a, allow_redirects=True)
        for comment in re.findall(comments, response.text):
            finds.append(comment)

        result = ''
        if len(finds) > 0:
            result += "\n[+] " + str(response.status_code) + " " + url+'\n'
            for find in finds:

                if len(find) > 240:
                    result += find[:240] + '\n'
                    result += "[...]\n" + '\n'
                else:
                    result += find + '\n'
        out(result)

    def get():
        disp = curr_wid.tb_display.setText
        inp = curr_wid.le_link.text().strip()
        from re import compile
        patt = compile(r"^(https:\/\/|http:\/\/)(www.)?(\w+\.)+([a-z]{2,4})(\/\w+)*(\/)*$")
        if inp:
            if patt.match(inp):
                prog(inp, disp)
            else:
                disp('<h1>Wrong Link</h1>')
        else:
            disp('<h1>Empty </h1>')

    curr_wid.bt_get.clicked.connect(get)

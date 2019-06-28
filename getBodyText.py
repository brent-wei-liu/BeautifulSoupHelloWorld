from bs4 import BeautifulSoup
import os
import json
html = '''<html>
<head><title>Irish finmin sees no issue in reprofiling Greek debt | Reuters News</title></head>
<body>
<p>
<p>LUXEMBOURG, June 15 (Reuters) - Ireland sees no issue with  reprofiling Greece's debt</p><p>Ireland has no difficulty with proposals in relation to the  reprofiling of Greek debt,\" .</p>\n
</p>
</body>
</html>'''
soup = BeautifulSoup(html, features="html.parser")
print('Title Text:[%s]\n' % soup.title.get_text().strip())
print('Body Text:[%s]' % soup.body.get_text(separator='\n').strip())

i = 0
for root, dirs, files in os.walk('cap_requests', topdown=False):
    for name in files:
        path = os.path.join(root, name)
        print(i, path)
        with open(path, 'r') as f:
            obj = json.load(f)
            html = obj['parameters']['text']
            soup = BeautifulSoup(html, features="html.parser")
            print('Title Text:[%s]\n' % soup.title.get_text().strip())
            i += 1
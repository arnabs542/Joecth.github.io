import re
import os
from glob import glob
from datetime import datetime

def writeinfile(path, cont, line=0):
    lines = []
    with open(path, 'r', encoding='utf-8') as r:
        for l in r:
            lines.append(l)
    if line == 0:
        lines.insert(0, '{}\n'.format(cont))
    else:
        lines.insert(line-1, '{}\n'.format(cont))
    s = ''.join(lines)
    # print(s)
    with open(path, 'w') as m:
        m.write(s)
        print('writeInFile Success!')

def foo(path):
    mds = glob(os.path.join(path, "[!_site]*/*md"))
    # mds = glob(os.path.abspath(os.path.join(path, "ML/*md")))

    print('\n'.join(mds))
    for md in mds:
        print(md)
        match = re.search(r'\d{4}-\d{2}-\d{2}', md)
        if match:
            date = datetime.strptime(match.group(), '%Y-%m-%d').date()
        else:
            date = "2019-08-24"

        msg = "date: {}".format(str(date))
        writeinfile(md, msg, 4)


if __name__ == "__main__":
    path = "../source/_posts"
    foo(path)
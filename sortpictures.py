"""
(C) Matthias Pallhon
MIT Licence v3

"""

import os
import time, datetime
import shutil
import platform

path = "."
orgsource = "bilderzumsortieren/"
orgoutput = "bildersortiert/"


def creation_date(path):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        #return os.path.getctime(path)
        return os.path.getmtime(path)
    else:
        stat = os.stat(path)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime




for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".NEF") or file.endswith(".dng"):
             print(os.path.join(root, file))
             #print "created: %x" % time.strftime("%d.%b.%Y %H:%M:%s %Z", time.localtime(creation_date(path))
             epoch = creation_date(path)
             year = time.strftime("%Y", time.localtime(epoch))
             month = time.strftime("%m", time.localtime(epoch))
             print month
             print year
             if os.path.exists(year):
                 if os.path.exists(month):
                     # merge month and year to a path
                     output = orgoutput + year + "/" + month + "/"
                     shutil.copy2(orgsource, output)
                 else:
                     os.mkdir(month)
             else:
                 os.mkdir(year)

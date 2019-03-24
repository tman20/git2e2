# author Tyler Lunyou
# March 2019
__virsion__ = "1.0"

import os


# checks if txt file has variable if variable == null then it writes a zero to be able to be incrased
def checkmtfiletozero(filename):
    if os.stat(filename).st_size == 0:
        with open(filename, 'w+') as f:
            f.write('0')
            f.close()


def filez(filename, dirpath):
    # filename string and directory path string
    checkmtfiletozero(filename)  # previously known as filz funcion
    with open(filename, 'r') as f:
        x = int(f.read())

        xa = int(x + 1)
        print xa  # add one to the tree.txt file

    with open(filename, 'w+') as f:
        f.write(unicode(xa))
        f.close()

    # -------- previously known as filzAdd funcion
    dirlist = os.listdir(dirpath)
    print dirlist, '   direcory list'

    print 'saved as ', str(x) + '_t.txt'
    name = str(x) + '_t.txt'
    xname = dirpath  # t'+str(x) +'.txt'
    print 'path location', xname, ' xname '

    opener = os.path.dirname(dirpath + '/t' + str(x) + '.txt')
    os.chdir(xname)  # the directory containing your .jpegs
    print opener, '   opener'

    with open(name, 'w+') as f:
        p = []
        for i in xrange(0, 1000, x):
            p.append(i)
        f.write(unicode(p))

        # f.(unicode(p))
        f.close()
        # ----------------------------
    print dirlist
    return x, dirlist


def versionfileworks():
    return __virsion__

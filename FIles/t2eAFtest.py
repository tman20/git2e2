# python 2.7 . on ubuntu laptop 
import cv2
import os
import time
import imutils
import numpy as np
import matplotlib
import t2eDIR as t2e           #my dir


def Start():
    print 'ESC to exit (press it a few times or hold it for a sec), \n' \
          'press "a" to take a picture, saved all three. The GUI at the beginning \n' \
          'if doesnt work just close it, may need to use "ctrl-c".        Enjoy'

    yesorno = raw_input('hit y to start t2e')
    print yesorno

    if yesorno == "y":
        print('go on')

    else:
        exit()


def show_webcam(mirror=False):
    global cam
    try:
        cam = cv2.VideoCapture(0)

    except NameError:
        print 'ERROR with camera, it may be busy with another process, blocked by a anti-virus program, or not set as default'

    c = 0
    # -------------------------------------------------------------------------------
    while True:

        ret_val, img = cam.read()

        if mirror:
            gimg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

            gimg2 = np.zeros_like(img)
            gimg2[:, :, 0] = gimg
            gimg2[:, :, 1] = gimg
            gimg2[:, :, 2] = gimg

            rimg = imutils.resize(img, width=400)  # IN USE r means RESIZED to fit
            rgimg = imutils.resize(gimg2, width=400)  # IN USE

            print("IMG", img.shape, 'gimg2', gimg2.shape, 'rimg', rimg.shape, '  rgimg', rgimg.shape)
            gimg = imutils.resize(gimg, width=400)
            Gimg = imutils.resize(gimg, width=400)  # this can be optomized its kinda a mess. Gimg and stuff
            edges = cv2.Canny(Gimg, 100, 190)
            print ('\nedges', edges.shape)
            edge = np.zeros_like(rgimg)  # IN USE
            edge[:, :, 0] = edges
            edge[:, :, 1] = edges
            edge[:, :, 2] = edges
            print ('\nedge', edge.shape)
            print ('\ngimg2', gimg2.shape)
            print ('\nrimg', rimg.shape)
            print ('\nedge', edge.shape)

            # cv2.imshow('my webcam', gimg)
            # cv2.imshow('img', img)
            # cv2.imshow('edges', edges)

            merge = np.concatenate((rimg, rgimg, edge), axis=1)

            cv2.imshow('Title-merge', merge)

            c = c + 1
            print c
            if cv2.waitKey(1) == ord('a'):
                i = c

                with open('tree.txt', 'r') as f:
                    x = int(f.read())

                f = '/home/tyler/PycharmProjects/t2eu/edges-file/' + 'edge' + str(x) + str(i) + '.png'
                ff = '/home/tyler/PycharmProjects/t2eu/edges-file/' + 'rgimg' + str(x) + str(i) + '.png'
                fff = '/home/tyler/PycharmProjects/t2eu/edges-file/' + 'rimg' + str(x) + str(i) + '.png'

                cv2.imwrite(f, edge)
                cv2.imwrite(ff, rgimg)
                cv2.imwrite(fff, rimg)

                i = i + 1

                print 'PIC IS TAKEN', i

            if cv2.waitKey(1) == 27:  # waitkey == ESC key-->(27)
                mirror = False
                break  # esc to quit


def main():
    Start()

    show_webcam(mirror=True)
    fdir = os.path.dirname(os.path.realpath(__file__))
    if os.path.exists(fdir + '/tree.txt'):
        open(fdir + '/tree.txt', 'a')
    else:
        open(fdir + '/tree.txt', 'w+')


    t2e.filez('tree.txt', '/home/tyler/PycharmProjects/t2exe/tree.exe')  #idk what is happening here...should be going to tree.txt and 
                                                                         #change to new dir- or just make it unpackage its self and not have this issue

    time.sleep()
    print 'done with t2e'


if __name__ == '__main__':
    main()

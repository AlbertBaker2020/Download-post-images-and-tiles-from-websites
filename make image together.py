from PIL import Image,ImageDraw
import collections
import os
import re
from itertools import groupby
g=[]

def get_concat_v_multi_resize(im_list, resample=Image.BICUBIC):
    min_width = min(im.width for im in im_list)
    im_list_resize = [im.resize((min_width, int(im.height * min_width / im.width)),resample=resample)
                      for im in im_list]
    total_height = sum(im.height for im in im_list_resize)
    dst = Image.new('RGB', (min_width, total_height))
    pos_y = 0
    for im in im_list_resize:
        dst.paste(im, (0, pos_y))
        pos_y += im.height
    return dst
def maketogetherimage(source,destination,numberofdir):
    directory = str(numberofdir)
    parent_dir = destination
    pathh = os.path.join(parent_dir, directory)
    os.mkdir(pathh)
    #filelist = os.listdir('store/6')
    filelist = os.listdir(source+str(numberofdir))
    list1=filelist
    mydict={}
    for k, g in groupby(list1, key=lambda x: x[:2]):
        if k in mydict:
            mydict[k] += g
        else:
            mydict[k]=list(g)
    
    for i in mydict:
        im=[]
        filename=i
        for j in mydict[i]:
            print('j',j)
            im.append(Image.open(source+str(numberofdir)+'/'+ j ))
        get_concat_v_multi_resize(im).save(destination+str(numberofdir)+'/'+i+'.jpg')
for i in range(1,88):
    maketogetherimage('store/','image2/',i)
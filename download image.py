import requests
from bs4 import BeautifulSoup
from PIL import Image,ImageDraw
import shutil
from PIL import Image,ImageDraw
import os, glob

def download(address,page,path):
    #address='https://www.mrsexe.com/videos/'
    #page='page5'
    #path='new image/'
    pagenumber=page[4:] 
    directory = pagenumber
    parent_dir = 'new image'
    pathh = os.path.join(parent_dir, directory)
    os.mkdir(pathh)
    originaladdress='//img.mrsexe.com/thumbs/mf006446_1/300x200_0298.jpg'
    address1='https://img.mrsexe.com/thumbs'
    #statv3['mf006446_1_386770']=0; picv3['mf006446_1_386770']=new Array(); picsv3['mf006446_1_386770']=new Array('0298','0172','0298','0428','0516','0614','0676','0740','0800','0836','1034','1210','012','012','012','012','0146','0212','0448');#
    x = requests.get(address+page+'.html')
    soup = BeautifulSoup(x.text,"html.parser")
    pos = -1 
    countpos=[]
    id=0
    #

    dir = path[:-1]

    filelist = glob.glob(os.path.join(dir, "*"))
    for f in filelist:
        os.remove(f)
    #
    while True:
        pos = str(soup).find('<a class="thumbnail"', pos + 1)
        countpos.append(str(pos))
        if pos == -1:
            break
    #    do_something
    countpos=countpos[:-1]

    for j in countpos:
        find1=j
        find2=str(soup).find('</a>',int(find1))
        content=str(soup)[int(find1):int(find2)]
        findpicnum1=content.find("new Array('")
        if (findpicnum1==-1):
            break
        else:
            findvideo1=content.find('a class="thumbnail" href="')
            findvideo2=content.find('.html">')
            video=content[27:findvideo2+5]
            print('https://mrsexe.com'+video)
            findpicnum2=content.find('</script>',findpicnum1)
            picturenumbers=content[findpicnum1+10:findpicnum2-2]
            findpictureaddress1=content.find("src='")
            findpictureaddress2=content.find('jpg',findpictureaddress1)
            pictureadress=content[findpictureaddress1+7:findpictureaddress2+3]
            allpictureadress=pictureadress.rfind('_')
            picturestr=pictureadress[:allpictureadress]+'_'
            picturesnumbers = eval('[' + picturenumbers + ']')
            picturesnumbers.sort()
            id+=1
            strid=str(id)
            if len(strid)>1:
                pass
            elif len(strid)==1:
                strid='0'+strid
            videotextlengh=len(video)//2
            videotext1=video[:videotextlengh]
            videotext2=video[videotextlengh:]
            img = Image.new('RGB', (300, 40), color = (128, 128, 128))
            d = ImageDraw.Draw(img)
            #d.text((10,10), "Hello World this is test,this is a story", fill=(255,255,255))
        #un-couple-se-paye-un-producteur-porno-rien-que-pour-eux-636
            d.text((10,10), videotext1 + "\n"+videotext2, fill=(255,255,0))
            img.save(path + strid+'_'+'.jpg' )
            for i in picturesnumbers:
                
                image_url=picturestr+i+'.jpg'
                #filename = image_url.split("/")[-1]
                strid=str(id)
                if len(strid)>1:
                    pass
                elif len(strid)==1:
                    strid='0'+strid

                filename=path+strid+'_'+str(i)+ '.jpg'
                print(image_url)
                rr = requests.get('http://'+image_url, stream = True)
                if rr.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
                    rr.raw.decode_content = True
                    with open(filename,'wb') as f:
                        shutil.copyfileobj(rr.raw, f)
                    print('Image sucessfully Downloaded: ',filename)
                else:
                    print('Image Couldn\'t be retreived')

  #page=7

for i in range(1,88):
    page=i
    download('https://www.mrsexe.com/videos/','page'+str(page),'new image/'+str(page)+'/')
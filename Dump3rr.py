import os
from functools import partial
import re
from typing import final
try:
    import requests
except:
    os.system('pip install requests')
finally:
    import requests
try:
    from bs4 import BeautifulSoup
except:
    os.system('pip install beautifulsoup4')
    os.system('pip install lxml')
finally:
    from bs4 import BeautifulSoup


########   USER CHANGES ###########

url='https....your url'
vimeo=True
youtube=False
pagetoavoid=['news']

cookies = {'cookie name': 'cookie value'}

########   USER CHANGES ###########


######## ######## ######## ######## ######## ######## ######## ######## 
######## AUTHOR ----- https://github.com/ch-ckmate/Dump3rr
######## ######## ######## ######## ######## ######## ######## ######## 


proxylist={}
headersdefault={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36','Accept-Language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6','Accept-Encoding': 'gzip, deflate, br','Referer': url,'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Connection': 'keep-alive'}
sitename=url.split('://')[1].split('.')[0]
domain=url.split('://')[1].split('/')[0]
badsitelist=['instagram','tiktok','facebook','twitter']
if not os.path.isdir(os.getcwd()+'\\'+sitename):
    os.mkdir(os.getcwd()+'\\'+sitename)
if not os.path.isdir(os.getcwd()+'\\'+sitename+'\\websiteimages'):
    os.mkdir(os.getcwd()+'\\'+sitename+'\\websiteimages')
if not os.path.isdir(os.getcwd()+'\\'+sitename+'\\websitevideo'):
    os.mkdir(os.getcwd()+'\\'+sitename+'\\websitevideo')
make_directory = partial(os.makedirs, exist_ok=True)



def functiongetvideo(urlofvideo):
    listtest=[]
    if vimeo:
            pagevideopriv=session.get(urlofvideo,cookies=cookies,headers={'Referer': url.split(domain)[0]+domain})
            soup = BeautifulSoup(pagevideopriv.content, 'html.parser')
            for i in soup.find_all('script'):
                for ii in re.findall('(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})',str(i)):
                    if 'vod' in str(ii):
                        listtest=ii.split('"')
                        listtest=[s for s in listtest if "vod" in s]
                        listtest=[s for s in listtest if ".mp4" in s]
            
            if listtest: 
                print('Downloading video: '+str(listtest[-1]))
                with requests.get(listtest[-1],stream=True) as r:
                    with open(os.getcwd()+'\\'+sitename+'\\websitevideo\\'+str(urlofvideo).split('?')[0].split('/')[-1]+'.mp4', 'wb') as f:
                        f.write(r.content)
            
def functiongetimages(immagine):
        try:
            if not os.path.exists(os.getcwd()+'\\'+sitename+'\\websiteimages\\'+immagine.split('/')[-1]):
                imgget=requests.get('http://'+domain+immagine,stream=True)
                print('Dumping '+str(immagine.split('/')[-1]))
                with open(os.getcwd()+'\\'+sitename+'\\websiteimages\\'+immagine.split('/')[-1], 'wb') as f:
                    f.write(imgget.content)
        except:
            pass


def iterateoverresult(xxxx):    
    for urltoget in xxxx:
            if all(x not in urltoget for x in badsitelist):
                if all(x not in urltoget for x in pagetoavoid):
                    if domain in urltoget:
                        print('Checking: '+str(urltoget))
                        listadirtocreate=urltoget.split(domain)[1].split('/')
                        listadirtocreate=[x for x in listadirtocreate if x]
                    
                        if len(listadirtocreate)==1:
                            
                            if not os.path.isdir(os.getcwd()+'\\'+sitename+'\\'+listadirtocreate[0].replace('?','')):
                                os.mkdir(os.getcwd()+'\\'+sitename+'\\'+listadirtocreate[0].replace('?',''))

                            pagenewtoget=urltoget.split(domain)[1].split('/')[-1]
                            pagegetted=session.get(urltoget,cookies=cookies,headers=headersdefault)
                            soup = BeautifulSoup(pagegetted.content, 'html.parser')

                            for img in soup.find_all('img'):
                                if domain not in img['src']:
                                    functiongetimages(img['src'])
                                    img['src']=os.getcwd()+'\\'+sitename+'\\websiteimages\\'+img['src'].split('/')[-1]

                            for a in soup.find_all('a', href=True):
                                if sitename in a['href']:
                                    listtogetnew.append(a['href'])
                                    a['href']=a['href'].replace('https://','').replace('http://','').replace(domain,'')
                                    a['href']=os.getcwd()+'\\'+sitename+a['href'].replace('?','')+'/'+sitename+a['href'].replace('?','')+'.html'

                            for videouid in re.findall('(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})',str(soup)):
                                
                                if 'vimeo' in videouid:
                                    videouid=videouid.split('")')[0]
                                    videopath=(os.getcwd()+'/'+sitename+'\\websitevideo\\'+str(videouid).split('?')[0].split('/')[-1]+'.mp4').replace('\\','\\\\')
                                    soup=BeautifulSoup(str(soup).replace(videouid,videopath),features="lxml")
                                    soup=BeautifulSoup(str(soup).replace('mp4 title=','mp4'),features="lxml")
                                    if not os.path.exists(os.getcwd()+'\\'+sitename+'\\websitevideo\\'+str(videouid).split('?')[0].split('/')[-1]+'.mp4'):
                                        functiongetvideo(videouid)

                            if not os.path.exists(os.getcwd()+'\\'+sitename+'\\'+listadirtocreate[0].replace('?','')+'\\'+pagenewtoget.replace('?','')+'.html'):
                                for script in soup.find_all('script'):
                                    if ' src' in str(script):
                                        if 'src="http' not in str(script):
                                            try:
                                                if '.js' in script['src']:
                                                    if domain not in script['src']:
                                                        script['src']=url.split(domain)[0]+domain+script['src']
                                            except:
                                                pass
                                    
                                print('Dumping '+listadirtocreate[0].replace('?','')+'\\'+str(pagenewtoget)+'.html')
                                with open(os.getcwd()+'\\'+sitename+'\\'+listadirtocreate[0].replace('?','')+'\\'+pagenewtoget.replace('?','')+'.html', 'w', encoding="utf-8") as f:
                                    f.write(soup.prettify( formatter="html" ))
                            
                        else:
                            
                            treedir=[]
                            for i in range(len(listadirtocreate)):
                                treedir.append('\\')
                                treedir.append(listadirtocreate[i])
                            
                            treedir = ''.join([str(elem) for elem in treedir])
                            
                            make_directory(os.getcwd()+'\\'+sitename+treedir)

                            pagenewtoget=urltoget.split(domain)[1].split('/')[-1]
                            pagegetted=session.get(urltoget,cookies=cookies,headers=headersdefault)
                            soup = BeautifulSoup(pagegetted.content, 'html.parser')

                            for img in soup.find_all('img'):
                                if domain not in img['src']:
                                    functiongetimages(img['src'])
                                    img['src']=os.getcwd()+'\\'+sitename+'\\websiteimages\\'+img['src'].split('/')[-1]

                            for a in soup.find_all('a', href=True):
                                if sitename in a['href']:
                                    listtogetnew.append(a['href'])
                                    a['href']=a['href'].replace('https://','').replace('http://','').replace(domain,'')
                                    a['href']=os.getcwd()+'\\'+sitename+a['href'].replace('?','')+'/'+a['href'].split('/')[-1]+'.html'
                                
                            for videouid in re.findall('(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})',str(soup)):
                                if 'vimeo' in videouid:
                                   
                                    videouid=videouid.split('")')[0]
                                   
                                    videopath=(os.getcwd()+'\\'+sitename+'\\websitevideo\\'+str(videouid).split('?')[0].split('/')[-1]+'.mp4').replace('\\','\\\\')
                                    
                                    soup=BeautifulSoup(str(soup).replace(videouid,videopath),features="lxml")
                                    soup=BeautifulSoup(str(soup).replace('mp4 title=','mp4'),features="lxml")
                                    if not os.path.exists(os.getcwd()+'\\'+sitename+'\\websitevideo\\'+str(videouid).split('?')[0].split('/')[-1]+'.mp4'):
                                        functiongetvideo(videouid)

                            if not os.path.exists(os.getcwd()+'\\'+sitename+treedir+'\\'+pagenewtoget.replace('?','')+'.html'):
                                for script in soup.find_all('script'):
                                    if ' src' in str(script):
                                        if 'src="http' not in str(script):
                                            try:
                                                if '.js' in script['src']:
                                                    if domain not in script['src']:
                                                        script['src']=url.split(domain)[0]+domain+script['src']
                                            except:
                                                pass
                            
                                print('Dumping '+treedir+'\\'+pagenewtoget.replace('?','')+'.html')
                                with open(os.getcwd()+'\\'+sitename+treedir+'\\'+pagenewtoget.replace('?','')+'.html', 'w', encoding="utf-8") as f:
                                    f.write(soup.prettify( formatter="html" ))
    listtotest=[]
    for tent in listtogetnew:
        if tent not in listtoget:
            listtotest.append(tent)
            listtoget.append(tent)
    listtotest=list(set(listtotest))
    if listtotest:
        iterateoverresult(listtotest)
    else:
        print('No more page found :)')
    


with requests.session() as session:
    
    listtoget=[]
    page=session.get(url,cookies=cookies,headers=headersdefault)

    soup = BeautifulSoup(page.content, 'html.parser')
    for img in soup.find_all('img'):
        if domain not in img['src']:
            functiongetimages(img['src'])
            img['src']=os.getcwd()+'\\'+sitename+'\\websiteimages\\'+img['src'].split('/')[-1]

    for script in soup.find_all('script'):
        if ' src' in str(script):
            if 'src="http' not in str(script):
                if '.js' in script['src']:
                    if domain not in script['src']:
                        script['src']=url.split(domain)[0]+domain+script['src']

    for a in soup.find_all('a', href=True):
            if sitename in a['href']:
                listtoget.append(a['href'])
                
                a['href']=a['href'].replace('https://','').replace('http://','').replace(domain,'')
                a['href']=os.getcwd()+'/'+sitename+'/'+a['href']+'/'+a['href'].split('/')[-1]+'.html'

    with open(os.getcwd()+'\\'+sitename+'\\'+'home.html', 'w') as f:
        f.write(soup.prettify( formatter="html" ))

    listtogetnew=[]
    iterateoverresult(list(set(listtoget)))
       

        

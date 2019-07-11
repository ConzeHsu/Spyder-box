import os
import urllib
def download_file(download_url):
    abspath = os.path.abspath('.')
    dir_download = os.path.join(abspath,"download")
    if not os.path.isdir(dir_download):
        os.mkdir(dir_download)
    name = os.path.join(dir_download,download_url.split('/')[-1])
    
    web_file = urllib.urlopen(download_url)
    with open(name,'w') as f:
        f.write(web_file.read())
    web_file.close()

if __name__ == "__main__":
    m, n = map(int, raw_input("Enter the range you want to download, such as\n1-10\nthen press Enter to end\n").split('-'))
    for i in range(m, n+1):
        temp = i // 10
        if temp == 0:
            number = "000"+str(i)
        elif temp >= 1 and temp < 10:
            number = "00"+str(i)
        elif temp >=10:
            number = "0"+str(i)
        url = 'https://ia800103.us.archive.org/31/items/englishpod_all/englishpod_{}.pdf'.format(number)
        download_file(url)

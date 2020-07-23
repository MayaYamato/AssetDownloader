import os
import requests
import urllib.error
import urllib.request

### my library ###

def introduce(local_version):
    print(os.path.basename(__file__)+' ver '+str(local_version))
    print('Created By : VERSUS.log')
    print('Twitter : @227_VS')
    print('Blog : https://raspberrypi422.mydns.jp')
    print('Github : https://github.com/MayaYamato')

def download_file(url,dst_path):
    try:
        file = urllib.request.urlopen(url).read()
        with open(dst_path,'wb') as f0:
            f0.write(file)
    except urllib.error.URLError as __e:
        pass

def download_content(url,dst_path):
    try:
        file = requests.get(url)
        with open(dst_path,'wb') as f0:
            f0.write(file.content)
    except urllib.error.URLError as __e:
        pass

def update_check(local_version,url_version,url_github):
    print('Version Checking ... ')
    with urllib.request.urlopen(url_version) as response:
        html = response.read().decode() 
        remote_version = html[:-1]
    if float(remote_version) - float(local_version) > 0:
        print('New Version Released:'+str(remote_version)+'\n')
        tmp =input('Do Upgrade? yes or no\n>>')
        if tmp == 'yes':
            download_dir_exe = os.getcwd()+r'\update_exe'
            if not os.path.exists(download_dir_exe):
                os.makedirs(download_dir_exe)
            dst_path_exe = os.path.join(download_dir_exe, os.path.basename(os.path.abspath(__file__))[-3]+'.exe')
            url_download_exe = url_github+r'/'+str(remote_version)+r'/'+os.path.basename(os.path.abspath(__file__))[:-3]+'.exe'
            download_content(url_download_exe,dst_path_exe)
            print('Download Complete')
        else:
            pass
    else:
        print('Latest Version\n')
from __init__ import os,request,time
def table(pwd):
    folder =[]
    file = []
    for item in os.listdir(pwd):
        fileitem = {'filename': '', 'filetype': '', 'filesize': '', 'filetime': ''}
        fileitem['filename'] = item
        fileitem['filetime'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.path.getctime(pwd + item)))
        fileitem['url'] = str(request.path + '/' + item).replace('//', '/')
        if os.path.isdir(pwd + item):
            fileitem['filetype'] = 'folder'
            fileitem['filesize'] = '-'
            fileitem['url'] =fileitem['url'] + '/'
            folder.append(fileitem)
        elif os.path.isfile(pwd + item):
            fileitem['filetype'] = 'file'
            filesize = os.path.getsize(pwd+item)
            if filesize < 1024*1024:
                fileitem['filesize'] = '{0:.2f}KB'.format(filesize/1024)
            elif filesize >= 1024*1024:
                fileitem['filesize'] = '{0:.2f}MB'.format(filesize/1024/1024)
            elif filesize >= 1024*1024*1024:
                fileitem['filesize'] = '{0:.2f}GB'.format(filesize/1024/1024/1024)
            file.append(fileitem)
    table = folder + file
    # print('[+] Table:',table)
    return table
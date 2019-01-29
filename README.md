# XMorbid
> XMorbid是利用flask与python基础模块，快速开发的项目。目前比较简陋，

#### python依赖环境
- Click==7.0
- dominate==2.3.5
- Flask==1.0.2
- Flask-Bootstrap==3.3.7.1
- Flask-Extension==1.0
- itsdangerous==1.1.0
- Jinja2==2.10
- MarkupSafe==1.1.0
- visitor==0.1.3
- Werkzeug==0.14.1

---


### 以下是 app.py 注释

#### # index()
```
@app.route('/')
def index(folder_path='',path_list=''):
    if folder_path == '':
        folder_path = os.getcwd() + '\\'
    return render_template(
        'base.html',
        title='NMTech资源服务器,
        web_path=path_list,
        table=getfilemap.table(folder_path)
        )
```
#### @app.route('/<path:folder_path>')
> 这个是遍历 route的path，从而映射目录与Table之间的关系

```
@app.route('/<path:folder_path>')
def dir_folder(folder_path):
    path_url = str(request.path)
    pwd = os.getcwd() + '\\'
    if str(path_url)[:1] == '/':
        path_url = path_url[:-1]
    path = path_url.split('/')
    path_list =[]
    # 下面这行的是 返回上一层的功能
    path_list.append({'name':'..','value':path_url[:len(path_url) - len(path[len(path)-1])],'time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.path.getctime(pwd + str(path_url[:len(path_url) - len(path[len(path)-1])]).replace('/','\\'))))})
    url = '/'
    # 构造导航栏部分
    for i in range(1,len(path)):
        tmp = {}
        url = url  + path[i] +'/'
        tmp['name'],tmp['value'] = path[i],url
        path_list.append(tmp)
    file_path = pwd + folder_path.replace('/', '\\')
    # 下面判断是否为文件，如果是文件就提供下载，否则再次遍历目录
    if os.path.isfile(file_path):
        return send_file(file_path)
    else:
        folder_path = file_path + '\\'
        app.logger.debug('[+] index() folder:', folder_path)
        return index(folder_path,path_list)
```
## 功能模块 getfilemap.py 
> 主要负责将目录内的信息，存放至 List供 Base.html 模板使用。


```
def table(pwd):
    folder =[]
    file = []
    # print('[+] getfilemap(pwd) pwd:',pwd)
    for item in os.listdir(pwd):
        fileitem = {'filename': '', 'filetype': '', 'filesize': '', 'filetime': ''}
        fileitem['filename'] = item
        fileitem['filetime'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.path.getctime(pwd + item)))
        fileitem['url'] = str(request.path + '/' + item).replace('//', '/')
        if os.path.isdir(pwd + item):
            fileitem['filetype'] = 'folder'
            #getfilemap(pwd + item + '\\',flag + 1)
            fileitem['filesize'] = '-'
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
```
##### 作者的第一个自己完成的完整小项目，后期会陆续添加模块。

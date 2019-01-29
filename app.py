#!
# -*- encoding:utf-8 -*-
from __init__ import *
from __init__ import getfilemap

app = Flask(__name__)
bootstrap = Bootstrap(app)
@app.route('/')
def index(folder_path='',path_list=''):
    if folder_path == '':
        folder_path = os.getcwd() + '\\'
    return render_template('base.html',
                title='NMTech 资源服务器',
                web_path=path_list,
                table=getfilemap.table(folder_path))

@app.route('/<path:folder_path>')
def dir_folder(folder_path):
    path_url = str(request.path)
    pwd = os.getcwd() + '\\'
    if str(path_url)[:1] == '/':
        path_url = path_url[:-1]
    path = path_url.split('/')
    path_list =[]
    print(path_url)
    path_list.append({'name':'..','value':path_url[:len(path_url) - len(path[len(path)-1])],'time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.path.getctime(pwd + str(path_url[:len(path_url) - len(path[len(path)-1])]).replace('/','\\'))))})
    url = '/'
    for i in range(1,len(path)):
        tmp = {}
        url = url  + path[i] +'/'
        tmp['name'],tmp['value'] = path[i],url
        path_list.append(tmp)
    file_path = pwd + folder_path.replace('/', '\\')
    if os.path.isfile(file_path):
        return send_file(file_path)
    else:
        folder_path = file_path + '\\'
        app.logger.debug('[+] index() folder:', folder_path)
        return index(folder_path,path_list)

if __name__ == '__main__':
    app.run(host='172.168.1.21')

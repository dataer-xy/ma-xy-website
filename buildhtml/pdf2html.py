"""pip install docker

docker run -ti --rm -v /c/Users/Administrator/pdf:/pdf pdf2htmlex/pdf2htmlex:0.18.8.rc2-master-20200820-ubuntu-18.04-x86_64 --zoom 1.3 test.pdf
"""
import glob
import os 
import docker
client = docker.from_env()

bathPath = os.path.dirname(
    os.path.dirname(
        __file__
    )
)

# pdfFileDir = os.path.join(bathPath,"docs",".vuepress","public","texpdf")
pdfFileDir = r"C:\Users\Administrator\pdf" # test
# pdfFileDir = r"G:\pdf" 

# 构建docker需要的路径格式
# NOTE: /c/Users/Administrator/pdf
# NOTE: c 不能大写 C

drive,other = os.path.splitdrive(pdfFileDir)
if drive:
    drive = drive[0].lower()

other = other.replace("\\","/")

pdfFileDirForVolunmes = "/" + drive + other

# 

fileList = glob.glob(pdfFileDir+"\\*.pdf")
skipFileNameList = [
    "ma-all.pdf",
    "part-de.pdf",
    "part-mldl.pdf",
    "part-opt.pdf",
    "part-sxjm.pdf"
] # 不需要转换的pdf

for iFile in fileList:
    _,pdfFileName = os.path.split(iFile) # "test.pdf"

    # 已经存在，则跳过
    iHtml = iFile.replace(".pdf",".html")
    if os.path.exists(iHtml):
        continue

    # 不需要转换，则跳过
    if pdfFileName in skipFileNameList:
        continue
    
    # run
    client.containers.run(
        'pdf2htmlex/pdf2htmlex:0.18.8.rc2-master-20200820-ubuntu-18.04-x86_64', 
        command='--zoom 1.3 {pdfFileName}'.format(pdfFileName=pdfFileName),
        auto_remove=True, 
        volumes={
            pdfFileDirForVolunmes: {
                'bind': '/pdf',
                'mode': 'rw'
            }
        }, # 挂载
    ) # detach=True, auto_remove=True, # 在容器启动时设置--rm选项，这个容器就被删除了，方便在临时测试使用。
    # error
    # win宿主无法挂载
    # https://segmentfault.com/q/1010000009469821

    # No such container: 5bb


    # out
    print("{pdfFileName} file convert to html end".format(pdfFileName=pdfFileName))



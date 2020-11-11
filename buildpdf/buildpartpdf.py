"""
构建整体pdf
每个part要在main.tex中进行选择，然后再构建
"""
import subprocess
import os 


basePath = r"D:\GODEYES\INCUBATORS\ma-xy-website"
texFilePath = os.path.join(basePath,"texsrc","src") # tex文件路径
# texFilePath = os.path.join(basePath,"texsrc") # tex文件路径

pwd = os.getcwd()

os.chdir(texFilePath) # 修改当前工作目录


fullPathTex = os.path.join(texFilePath,"main.tex")


fileNameHasExt = os.path.split(fullPathTex)[1]
fileNameNoExt = os.path.splitext(fileNameHasExt)[0]


dirOutput = os.path.join(texFilePath,"out") # 当前工作目录下的 out 

cmd = "xelatex -interaction=nonstopmode -output-directory={} {}".format(
    dirOutput, 
    fullPathTex
)

# 编译出 aux
code = subprocess.run(
    cmd, 
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True
)
# 编译参考文献 BibTex
# 如果有对应的的bib文件，则尝试编译，没有bib则跳过

os.chdir(dirOutput) # 修改当前工作目录

cmd2 = "bibtex {fileNameNoExt}".format(
    fileNameNoExt=fileNameNoExt
)
code = subprocess.run(
    cmd2, 
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True
)
os.chdir(texFilePath) # 修改当前工作目录

# 编译目录等
code = subprocess.run(
    cmd, 
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True
)
code = subprocess.run(
    cmd, 
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True
)
code = subprocess.run(
    cmd, 
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True
)




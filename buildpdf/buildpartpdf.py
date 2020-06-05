"""
构建整体pdf

"""



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

cmd2 = "bibtex {fileNameNoExt}".format(
    fileNameNoExt=fileNameNoExt
)
code = subprocess.run(
    cmd2, 
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True
)

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





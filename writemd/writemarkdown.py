"""
向各个 markdown 中写入信息 
NOTE:
pdf 格式
markdown格式
"""
import glob
import os

basePath = os.path.dirname(
    os.path.dirname(
        __file__
    )
)

def markdown_use_html():
    """pdf转html"""

    partNameList = ["de","mldl","opt","sxjm"]

    for partName in partNameList:

        a = os.path.join(basePath,"docs",partName,"*.md")
        
        mkFileList = glob.glob(a)

        for mkFile in mkFileList:

            _,mkFileName = os.path.split(mkFile)
            if mkFileName == "README.md":
                continue
            _mkFileName,_ = os.path.splitext(mkFileName)
    
            with open(mkFile,"r",encoding="utf-8") as mkF:
                mkStr = mkF.read()

            oldStr = r"[全页打开](/texpdf/{_mkFileName}.pdf) (_self形式)".format(_mkFileName=_mkFileName)
            newStr = r"""<a href="/texpdf/{_mkFileName}.html" target="_blank">全页打开</a> (_blank形式)""".format(_mkFileName=_mkFileName)
            mkStr = mkStr.replace(oldStr,newStr)
            mkStr = mkStr.replace(".pdf",".html")
            
            ## 写 mk 到 文件夹下，哪个 part ?
            with open(mkFile,"w",encoding="utf-8") as mkF:
                mkF.write(mkStr)



def markdown_use_pdf():
    """html转pdf"""

    partNameList = ["de","mldl","opt","sxjm"]

    for partName in partNameList:

        a = os.path.join(basePath,"docs",partName,"*.md")
        
        mkFileList = glob.glob(a)

        for mkFile in mkFileList:

            _,mkFileName = os.path.split(mkFile)
            if mkFileName == "README.md":
                continue
            _mkFileName,_ = os.path.splitext(mkFileName)
    
            with open(mkFile,"r",encoding="utf-8") as mkF:
                mkStr = mkF.read()

            oldStr = r"""<a href="/texpdf/{_mkFileName}.html" target="_blank">全页打开</a> (_blank形式)""".format(_mkFileName=_mkFileName)
            newStr = r"""<a href="/texpdf/{_mkFileName}.pdf" target="_blank">全页打开</a> (_blank形式)""".format(_mkFileName=_mkFileName)
            mkStr = mkStr.replace(oldStr,newStr)
            mkStr = mkStr.replace(".html",".pdf")
            
            ## 写 mk 到 文件夹下，哪个 part ?
            with open(mkFile,"w",encoding="utf-8") as mkF:
                mkF.write(mkStr)





def __main():
    markdown_use_html()
    # markdown_use_pdf()
    print("end")


if __name__ == "__main__":
    __main()


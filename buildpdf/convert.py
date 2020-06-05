"""将tex转化为pdf


目录要编译两遍?

"""

import subprocess
import os 

basePath = r"D:\GODEYES\INCUBATORS\ma-xy-website"
texFilePath = os.path.join(basePath,"docs",".vuepress","public","texpdf") # tex pdf 文件路径

def build_tex_str(documentStr,bibFileName=""):
    """
    TODO:
        添加bibliography
    """

    str1 = r"#1@}"
    str2 = r"#1#2{\textsuperscript{[{#1\if@tempswa , #2\fi}]}}"

    texTemplateStr = r"""
\documentclass[UTF8]{ctexbook}

\ctexset{
    part/number = \chinese{part}
}
%% 符号及公式设置
\usepackage{multirow}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{bbm}
\usepackage{amssymb,latexsym}
\usepackage{mathrsfs}

%% 定理引理证明
\usepackage{ntheorem}
    \theoremstyle{nonumberplain}
    \theoremheaderfont{\bfseries}
    \theorembodyfont{\normalfont}
    \theoremsymbol{$\square$}
    \newtheorem{Proof}{\hskip 2em 证明}
    \newtheorem{theorem}{\hspace{2em}定理}[chapter]
    \newtheorem{definition}{\hspace{2em}定义}[chapter]
    \newtheorem{axiom}[definition]{\hspace{2em}公理}
    \newtheorem{lemma}[definition]{\hspace{2em}引理}
    \newtheorem{proposition}[definition]{\hspace{2em}命题}
    \newtheorem{corollary}[definition]{\hspace{2em}推论}
    \newtheorem{remark}{\hspace{2em}注}
    \newtheorem{Assumption}{\hspace{2em}假设}[chapter]
    \newtheorem{example}{\hspace{2em}示例}[chapter]

%% 算法伪代码
\usepackage{algorithm}
\usepackage{algorithmicx}
\usepackage{algpseudocode}
    \floatname{algorithm}{算法}
    \renewcommand{\algorithmicrequire}{\textbf{输入:}}
    \renewcommand{\algorithmicensure}{\textbf{输出:}}

%%  罗马数字：示例：\rom{2}
\makeatletter
\newcommand*{\rom}[1]{\expandafter\@slowromancap\romannumeral \%(str1)s 
\makeatother

%% 文本下划线
\usepackage{ulem}

%% 列表环境
\usepackage{enumerate}
\usepackage{enumitem}

%% 参考文献(上标)
\usepackage{cite}
    \bibliographystyle{plain}
    \makeatletter
    \def\@cite\%(str2)s
    \makeatother

%% 圆圈，并设置圆圈脚注
\usepackage{pifont}
\renewcommand\thefootnote{\ding{\numexpr171+\value{footnote}}}

%% 超链接
\usepackage{hyperref}
\hypersetup{
    colorlinks=false,
    pdfborder=0 0 0
}

%% 图片
\usepackage{graphicx}
\usepackage{caption}
\usepackage{subcaption}
\graphicspath{{images/}}
\usepackage{float,varwidth}
\usepackage{caption}

%% 表格
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{longtable}
\setlength{\abovecaptionskip}{4pt}
\setlength{\belowcaptionskip}{-8pt}

\usepackage{extarrows}
\usepackage{xfrac,upgreek}
\usepackage{mathtools}
\usepackage{harpoon}
\usepackage{bookmark}


%% 代码高亮
\usepackage{listings}
\usepackage{xcolor}
\usepackage{colortbl}
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}
\lstset{
    commentstyle=\color{codegreen},
    keywordstyle=\color{magenta},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\footnotesize,
    breakatwhitespace=false,
    breaklines=true,
    captionpos=b,
    keepspaces=true,
    numbers=left,
    numbersep=5pt,
    showspaces=false,
    showstringspaces=false,
    showtabs=false,
    tabsize=2
}
%% 调用PDF文件
\usepackage{pdfpages}
%% 页面设置
\usepackage{geometry}
\geometry{paperwidth=185mm,paperheight=260mm,left=15mm,right=15mm, bottom=10mm}
\raggedbottom

%% 页眉页脚设置
\usepackage{fancyhdr}
\pagestyle{headings}

%% 章节格式设置
\CTEXsetup[format={\zihao{-3}\raggedright\bfseries}]{section}
\renewcommand{\headwidth}{\textwidth}

%% 水印
\usepackage{draftwatermark}
\SetWatermarkScale{1}

\begin{document}
\tableofcontents

\clearpage
\pagenumbering{arabic}

%(documentStr)s

\bibliography{%(bibFileName)s}

\end{document}
"""



    texStr = texTemplateStr % {
        "str1":str1,
        "str2":str2,
        "documentStr":documentStr,
        "bibFileName":bibFileName
    }

    return texStr


# OK 清除无用文件
def remove_temp_files(dirOutput, name):
    try:
        delete_file(os.path.join(dirOutput,"{}.aux".format(name)))
    except:
        pass
    try:
        delete_file(os.path.join(dirOutput,"{}.log".format(name)))
    except:
        pass
    try:
        delete_file(os.path.join(dirOutput,"{}.thm".format(name)))
    except:
        pass
    try:
        delete_file(os.path.join(dirOutput,"{}.fls".format(name)))
    except:
        pass
    try:
        delete_file(os.path.join(dirOutput,"{}.fdf_latexmk".format(name)))
    except:
        pass
    try:
        delete_file(os.path.join(dirOutput,"{}.toc".format(name)))
    except:
        pass
    
    # try:
    #     delete_file(os.path.join(dirOutput,"{}.pdf".format(name)))
    # except:
    #     pass
    # try:
    #     delete_file(os.path.join(dirOutput,"{}.tex".format(name)))
    # except:
    #     pass


# OK 生成pdf
def build_tex_pdf(dirOutput,fullPathTex,DEVNULL):
    """tex生成pdf"""

    # 切换空间 pwd 然后切回来
    # 不然 tex 的图片无法加载

    pwd = os.getcwd()

    os.chdir(texFilePath)   #修改当前工作目录

    try:
        cmd = "xelatex -interaction=nonstopmode -output-directory={} {}".format(
            dirOutput, 
            fullPathTex
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
    except:
        code = subprocess.call(
            ["xelatex", '-interaction=nonstopmode', fullPathTex],
            stdout=DEVNULL, 
            stderr=DEVNULL
        )
        code = subprocess.call(
            ["xelatex", '-interaction=nonstopmode', fullPathTex],
            stdout=DEVNULL, 
            stderr=DEVNULL
        )
    finally:
        os.chdir(pwd)
    return code




import glob
import re
import os 
from os import remove as delete_file


selectLevel = "chapter"

DEVNULL = open(os.devnull, "w")


texFileList = glob.glob(basePath+r"\texsrc\src\*.tex")



for fileNamei in texFileList:
    print("正在处理文件{fileNamei}...".format(fileNamei=fileNamei))

    # 获取 partName
    fileName = os.path.splitext(os.path.split(fileNamei)[1])[0] # 文件名
    partchapName = fileName.split("-")
    partName = partchapName[1]
    chaptName = partchapName[3]

    # 对第 i 个 tex 文件
    with open(fileNamei,"r",encoding="utf-8") as fi:
        documentStr = fi.read()
    
    # 等级
    # line = '''
    # \chapter{倒向随机微分方程}\label{cha:bsde}
    # \section{符号注记}
    # \chapter{test}
    # '''

    patt = r"\\chapter\{.*?\}" # r'/\*((?:.|\n)*?)\*/'
    
    matchObjIter = re.finditer(patt,documentStr)

    matchObjList = [matchObj for matchObj in matchObjIter]
    matchNum = len(matchObjList)

    for i,matchObj in enumerate(matchObjList):
        # 第i个chapter的位置，名称
        chapSpan = matchObj.span()
        chapName = re.findall(r"\\chapter\{(.*?)\}",matchObj.group())[0]

        # 将中文名称变为英文chapName
        if selectLevel == "chapter":
            chapEnglishName = chaptName
        else:
            chapEnglishName = None # TODO


        # chap 的内容
        if i < matchNum-1:
            nextChapStart = matchObjList[i+1].start()
        else:
            nextChapStart = None 
        
        chapContent = documentStr[chapSpan[0]:nextChapStart] # 1:None 可用

        # chap 的内容写入tex
        name = "part-{partName}-chap-{chapName}".format(
            partName=partName,
            chapName=chapEnglishName
        )
        texFileName = name + ".tex" # TODO: 怎样设置文件名称？
        texFile = os.path.join(texFilePath,texFileName)

        chapTexStr = build_tex_str(chapContent,name)

        with open(texFile,"w",encoding="utf-8") as texF:
            texF.write(chapTexStr)
        
        # tex 生成 pdf
        fullPathTex = texFile
        dirOutput = texFilePath
        code = build_tex_pdf(dirOutput,fullPathTex,DEVNULL)
        if code != 0:
            # delete_file(os.path.join(dirOutput,"{}.tex".format(name)))
            print("失败{filename}".format(filename=texFile))
            # continue
        remove_temp_files(dirOutput,name)


        # 写入 markdown 

        ## 获取级别数
        docLevel = 1
        mkLevel = "#" * docLevel

        ## 

        mkTemplate = r"""
{mkLevel} {chapName}
<div class="pdf-class">
    <iframe  src={pdfFile} width="1100" height="1100">
    </iframe>
</div>
"""
        
        mkStr = mkTemplate.format(
            mkLevel=mkLevel,
            chapName=chapName,
            pdfFile = os.path.join(r"\texpdf","{pdfFileName}.pdf".format(pdfFileName=name))
        )

        ## 写 mk 到 文件夹下，哪个 part ?
        mkFileName = "{fileName}.md".format(fileName=name)
        mkFile = os.path.join(
            basePath,
            "docs",
            partName,
            mkFileName
        )
        with open(mkFile,"w",encoding="utf-8") as mkF:
            mkF.write(mkStr)


        # 添加节点
        if selectLevel == "chapter":
            pass
        else:
            pass # TODO 创建节点并添加到父节点上





# 中英文件对照 以及config

# 每个节点以及下面的子节点

# 将节点提取成 part-chap-sect-subs 的形式 写入 js 文件 （深度优先遍历）

## 对 第 part 根节点而言，写入 js


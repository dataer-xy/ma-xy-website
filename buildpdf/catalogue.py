import os

basePath = r"D:\GODEYES\INCUBATORS\ma-xy-website"

partChapDict = {
    "sxjm":[
        "FBrate",
        "xueguan",
        "taiyangyingzi",
        "xipoxitong",
        "change3hao"
    ],
    "opt":[
        "noconst",
        "nols",
        "consnl",
        "linprog",
        "intprog",
        "qprog",
        "socp",
        "sdp",
        "gp",
        "mulopt",
        "minmaxopt",
        "gmlp",
        "glopt",
        "GA",
        "yalmip",
    ],
    "de":[
        "ode",
        "pde",
        "oie",
        "sde",
        "bsde",
    ],
    "mldl":[
        "Stoc",
        "svm1",
        "svm2",
        "RVM",
        "ANN",
        "DeepLearn",
        "boost",
    ]
}




class LevelNode(object):

    def __init__(self,name,level="part"):
        self.name = name
        self.level = level
        self.childNode = []
    
    def add_childNode(self,childNode):
        self.childNode.append(childNode)



sxjmPartNode = LevelNode("sxjm")
sxjmPartNode.add_childNode(LevelNode("FBrate","chap"))
sxjmPartNode.add_childNode(LevelNode("xueguan","chap"))
sxjmPartNode.add_childNode(LevelNode("taiyangyingzi","chap"))
sxjmPartNode.add_childNode(LevelNode("xipoxitong","chap"))
sxjmPartNode.add_childNode(LevelNode("change3hao","chap"))


optPartNode = LevelNode("opt")
optPartNode.add_childNode(LevelNode("noconst","chap"))
optPartNode.add_childNode(LevelNode("nols","chap"))
optPartNode.add_childNode(LevelNode("consnl","chap"))
optPartNode.add_childNode(LevelNode("linprog","chap"))
optPartNode.add_childNode(LevelNode("intprog","chap"))
optPartNode.add_childNode(LevelNode("qprog","chap"))
optPartNode.add_childNode(LevelNode("socp","chap"))
optPartNode.add_childNode(LevelNode("sdp","chap"))
optPartNode.add_childNode(LevelNode("gp","chap"))
optPartNode.add_childNode(LevelNode("mulopt","chap"))
optPartNode.add_childNode(LevelNode("minmaxopt","chap"))
optPartNode.add_childNode(LevelNode("gmlp","chap"))
optPartNode.add_childNode(LevelNode("glopt","chap"))
optPartNode.add_childNode(LevelNode("GA","chap"))
optPartNode.add_childNode(LevelNode("yalmip","chap"))


dePartNode = LevelNode("de")
dePartNode.add_childNode(LevelNode("ode","chap"))
dePartNode.add_childNode(LevelNode("pde","chap"))
dePartNode.add_childNode(LevelNode("oie","chap"))
dePartNode.add_childNode(LevelNode("sde","chap"))
dePartNode.add_childNode(LevelNode("bsde","chap"))


mldlPartNode = LevelNode("mldl")
mldlPartNode.add_childNode(LevelNode("Stoc","chap"))
mldlPartNode.add_childNode(LevelNode("svm1","chap"))
mldlPartNode.add_childNode(LevelNode("svm2","chap"))
mldlPartNode.add_childNode(LevelNode("RVM","chap"))
mldlPartNode.add_childNode(LevelNode("ANN","chap"))
mldlPartNode.add_childNode(LevelNode("DeepLearn","chap"))
mldlPartNode.add_childNode(LevelNode("boost","chap"))


partNodeList =[
    sxjmPartNode,
    optPartNode,
    dePartNode,
    mldlPartNode
]


for partNode in partNodeList:

    partName = partNode.name
    partLevel = partNode.level
    partS = "{level}-{name}".format(
        level=partLevel,
        name=partName
    )

    jsFilePath = os.path.join(basePath,"docs",".vuepress","nav")
    jsFile = os.path.join(jsFilePath,"{jsFileName}.js".format(jsFileName=partName))

    # require('./nav/en')
    with open(jsFile,"w",encoding="utf-8") as jsF:
        jsF.write(
            r"""
let {partName} = [
    '',
""".format(partName=partName)
# +"\n"
        )

        for childNode in partNode.childNode:
            chapS = "{level}-{name}".format(
                level=childNode.level,
                name=childNode.name
            )

            nameS = "{partS}-{chapS}".format(
                partS=partS,
                chapS=chapS
            )

            # 将 nameS 写入 js
            jsF.write("'" + nameS + "'" + "," + "\n")
        
        # 写结尾
        jsF.write(
            r"""
]

module.exports = %s ;

        """ % (partName)
        )


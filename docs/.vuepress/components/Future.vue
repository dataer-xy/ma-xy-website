<template>
<div class="features">
  <div class="feature">
    <h2>内容简介</h2>
    <p>
        主要包含了计算机和数值计算方向的一些模型和算法。暂时将整体分成了4个部分，包括机器学习问题、最优化问题、各种微分方程和一些数学建模。
        每个章节的书写逻辑大概可以描述为：引例（生活中的问题）、规范的模型、模型的求解算法、程序实例等。
        后期的开发目标可以参考
        <a href="/devexp/" target="_self" rel="noopener">
        这里
        </a>
        。
    </p>
     
  </div>
  <div class="feature">
    <h2>Logo 说明</h2>
    <p>
        ma-xy: ma 是 model and algorithm 的简写，而 xy 则是为了标明项目出处。
        无论是机器学习还是微分方程，最终研究的都是量与量之间的关系，因此有了这里的 xy。 
        <br>
        另外，logo 是我手绘的，是大写的 MA 组合在一起，
        原本是打算在底部画一个圆弧，结果手抖了一下，就成了蒙娜丽莎的微笑~
        （画完之后我总觉得这个微笑似乎在哪里见到过）
    </p>
  </div>
</div>
</template>
<script>
export default {
    
}
</script>
<style>
.features {
    border-top: 1px solid #eaecef;
    padding: 1.2rem 0;
    margin-top: 2.5rem;
    display: flex;
    flex-wrap: wrap;
    align-items: flex-start;
    align-content: stretch;
    justify-content: space-between;
}
.feature {
    flex-grow: 1;
    flex-basis: 30%;
    max-width: 45%;
}

.feature h2 {
    font-size: 1.4rem;
    font-weight: 500;
    border-bottom: none;
    padding-bottom: 0;
    color: #3a5169;
}
h2 {
    font-size: 1.65rem;
    padding-bottom: .3rem;
    border-bottom: 1px solid #eaecef;
}
h1, h2, h3, h4, h5, h6 {
    font-weight: 600;
    line-height: 1.25;
}
h2 {
    display: block;
    font-size: 1.5em;
    margin-block-start: 0.83em;
    margin-block-end: 0.83em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    font-weight: bold;
}
.feature p {
    color: #4e6e8e;
}
ol, p, ul {
    line-height: 1.7;
}
p {
    display: block;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
}
</style>

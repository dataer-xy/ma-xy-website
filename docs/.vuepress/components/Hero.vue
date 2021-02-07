<template>
  <div id="hero">
    <div class="inner">
      <div class="left">
        <img class="hero-logo"
             src="/ma-logo-215-215.png"
             alt="ma logo">
      </div>
      <div class="right">
        <h1>
          ~模型与算法~
        </h1>
        <h2>
          model and algorithm，开源的数学与计算机书籍
        </h2>
        <p>
          <a class="button white" href="/texpdf/ma-all.pdf" target="_blank" rel="noopener"> 
            下载整个 pdf
          </a>
          <a class="button white" href="https://github.com/dataer-xy/ma-xy-website" target="_blank" rel="noopener">
            <!-- button gray has-icon -->
            <!-- <svg aria-labelledby="simpleicons-github-dark-icon" lang="" role="img" viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title id="simpleicons-github-dark-icon" lang="en">GitHub Dark icon</title><path fill="#7F8C8D" d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg> -->
            <!-- <embed src="/github.svg" type="image/svg+xml" /> -->
            <!-- <img src="/github-icon.png" alt="" height="28" width="28"> -->
            GITHUB
          </a>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
#hero {
  padding: 40px 40px 30px;
  background-color: #fff;
}
#hero .inner{
  max-width: 1260px;
  margin: 0 auto;
}
#hero .left,
#hero .right{
  display: inline-block;
  vertical-align: top;
  /* width: 60%; */
  margin-right: 30px;
  margin-left: 30px;
}


#hero .button:not(:last-child){
    margin-right: 1%;
}
#hero .button{

    margin: 1em 0;
        margin-right: 0px;
    font-size: 1.05em;
    font-weight: 600;
    letter-spacing: 0.1em;
    min-width: 8em;
    text-align: center;

}

/* #hero h1{
    font-weight: 300;
    margin: 0;
    font-size: 3.2em;
} */




/* h1, h2, h3, h4, strong {
    font-weight: 600;
    color: #273849;
} */

/* h1 {
    display: block;
    font-size: 2em;
    margin-block-start: 0.67em;
    margin-block-end: 0.67em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    font-weight: bold;
} */

a.button.white, input.button.white {
    background-color: #fff;
    color: #42b983;
}



a.button.gray, input.button.gray {

    background-color: #f6f6f6;
    color: #4f5959;
    border-color: #f6f6f6;

}
a.button.has-icon, input.button.has-icon {

    position: relative;
    text-indent: 1.4em;

}

a.button, input.button {

    padding: 0.75em 2em;
    border-radius: 2em;
    display: inline-block;
    color: #fff;
    background-color: #4fc08d;
    transition: all 0.15s ease;
    box-sizing: border-box;
    border: 1px solid #4fc08d;
        border-top-color: rgb(79, 192, 141);
        border-right-color: rgb(79, 192, 141);
        border-bottom-color: rgb(79, 192, 141);
        border-left-color: rgb(79, 192, 141);

}
/* 
a {
    text-decoration: none;
    color: #304455;
}
p {
    word-spacing: 0.05em;
}

p {
    display: block;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
} */


</style>

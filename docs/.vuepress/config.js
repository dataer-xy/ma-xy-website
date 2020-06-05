// 网站信息及主题配置

let logoPath = "/icon/ma-logo-215-215-icon.png";

module.exports = {

    // base : "/dist/",

    // 网站基础信息
    title: 'ma-xy', // 网站的标题，它将会被用作所有页面标题的前缀，同时，默认主题下，它将显示在导航栏（navbar）上
    description: 'ma-xy 主页',
    head: [ // 注入到当前页面的 HTML <head> 中的标签
      // 增加一个自定义的 favicon(网页标签的图标)
      ['link', { rel: 'icon', href: `${logoPath}` }], 
      // PWA
      ['link', { rel: 'manifest', href: '/manifest.json' }],
      ['link', { rel: 'apple-touch-icon', href: `${logoPath}` }],
    ],
    serviceWorker: true, // 是否开启 PWA
    

    // 主题配置
    themeConfig: { 
        // logo: '/assets/img/logo.png',
        
        // 导航
        nav: [
            { text: '主页', link: '/' },
            { text: '最优化部分', link: `/opt/`}, // ${baseUrl} , target:'_self', rel:'' 
            { text: '机器学习部分', link: '/mldl/' },
            { text: '微分方程部分', link: '/de/' },
            { text: 'matlab与数学建模', link: '/sxjm/' },
            { text: '草稿', link: '/drafts/' },
            { text: '开发说明', link: '/devexp/' },
            { text: '赞助', link: '/sponsor/' },
            // { text: 'ma 源码', link: 'https://github.com/dataer-xy/ma-xy', target:'_blank', rel:'' },
            
            {
                text: '语言',
                ariaLabel: 'Language Menu',
                items: [
                  { text: 'Chinese', link: '/' },
                  { text: 'English', link: '/en/' }
                ]
            }
        ],

        // 侧边栏
        sidebar: {
            '/devexp/': [
              '',     /* /devexp/ */
              'HELPME',
              'LOG',  /* /devexp/one.html */
              'TODO',
              'DEBUG',
            //   'NEWS',
              'NOTES',
            //   'code-style'
            ],

            '/drafts/':[
              '',
              'cs'
            ],
            '/sponsor/':[
              '',
            ],

            '/opt/': require("./nav/opt"),
            '/mldl/': require("./nav/mldl"),
            '/de/': require("./nav/de"),
            '/sxjm/': require("./nav/sxjm"),

        },

        //
        lastUpdated: '上次更新', // string | boolean
        // displayAllHeaders: true, // 默认值：false

        // github 
        repo: 'dataer-xy/ma-xy-website', // 假定是 GitHub. 同时也可以是一个完整的 GitLab URL
        // 自定义仓库链接文字。默认从 `themeConfig.repo` 中自动推断为
        // "GitHub"/"GitLab"/"Bitbucket" 其中之一，或是 "Source"。
        repoLabel: 'ma源码',

        // docsRepo: 'vuejs/vuepress', // 假如你的文档仓库和项目本身不在一个仓库：
        // docsDir: 'docs', // 假如文档不是放在仓库的根目录下：
        // docsBranch: 'master', // 假如文档放在一个特定的分支下：
        
        editLinks: true, // 默认是 false, 设置为 true 来启用
        
        editLinkText: '在 GitHub 上编辑此页', // 默认为 "Edit this page"

        // 页面滚动 1.2.0+
        smoothScroll: true

    
    },
}
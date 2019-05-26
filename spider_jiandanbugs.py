"""debug和错误保存代码，非功能。使用selenium包获取html内容，使用BeautifulSoup解析网页"""

import os
import requests
from selenium import webdriver
from bs4 import BeautifulSoup


class GetJandan(object):
    def __init__(self, path, page=10):
        self.start_url = 'http://jandan.net/ooxx'
        self.url = ""
        self.save_path = path
        self.page = page

    def get_html(self):
        # browser = webdriver.PhantomJS()
        # browser.get(url)
        # print("get", url)
        # return browser.page_source
        html = """
        <!DOCTYPE html><html dir="ltr" lang="zh"><head>
            <!-- BEGIN html head -->
        <title>
        随手拍 - 分享经典一刻
        </title>
                <meta name="referrer" content="never">    <meta name="keywords" content="随手拍,身边的趣图,手机摄影,经典一刻">
            <meta name="description" content="大家手机相册里应该有不少有趣的图片，欢迎发到这里，分享你的经典一刻。">
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="renderer" content="webkit">
            <meta http-equiv="Window-target" content="_top">
            <meta name="baidu-site-verification" content="9wC0PEtTmEqSNlOk">
            <meta http-equiv="mobile-agent" content="format=html5; url=//i.jandan.net/ooxx">
                            <meta name="robots" content="index,follow">
                <link rel="stylesheet" href="//cdn.jandan.net/static/min/688b385b41838ddf972a16fb5756e5e3OeDnSTO7.01100002.css" type="text/css" media="screen">
                <link rel="apple-touch-icon" href="//cdn.jandan.net/static/img/appicon.png">
            <link rel="shortcut icon" href="//cdn.jandan.net/static/img/favicon.ico">
        <link rel="canonical" href="http://jandan.net/ooxx">    <script src="http://www.googletagservices.com/activeview/js/current/osd.js?cb=%2Fr20100101"></script><script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js"></script><script type="text/javascript" async="" src="https://dup.baidustatic.com/dup/ui/painter/dynamicFloat.js"></script><script type="text/javascript" async="" src="http://b3.jandan.net/auto_ds?ns=t&amp;vde=ammiVw3Vv8Vv8cWgZWgVTg_mVv8hhqq&amp;zcs=xtuYY_yX2yxW0xXZtY--Xztuxw0212uW&amp;zkb=uwzzq0v1&amp;ndw=3NMHTCLHGI&amp;nsc=t&amp;mom=NM8U1&amp;kbs=v&amp;nks=u&amp;ohzc=uuuttv,uu2tt1,uuttuu&amp;zc=vu1tquxu&amp;kxd=u&amp;zsc=UuqUu&amp;nbs=t&amp;nm=x&amp;zmc=xttqwtt&amp;zcc=21xqxvt1&amp;nml=TTTXWbZnTngbhgTYWeeXWYdT&amp;dzb=uyy1022xuw2yt&amp;p6=3llxg"></script><script src="http://push.zhanzhang.baidu.com/push.js"></script><script type="text/javascript" async="" src="http://cpro.baidustatic.com/cpro/ui/cm.js"></script><script src="http://pagead2.googlesyndication.com/pagead/js/r20190522/r20190131/show_ads_impl.js" id="google_shimpl"></script><script src="http://pagead2.googlesyndication.com/pub-config/r20160913/ca-pub-5673546663729848.js"></script><script type="text/javascript" async="" src="http://a3.jandan.net/keimow.js"></script><script>if (window != top)top.location.href = window.location.href;</script>
            <!--[if lt IE 9]>
            <script src="//cdn.jandan.net/static/jquery/1.11.1/jquery.min.js"></script>
            <![endif]-->
            <!--[if gte IE 9]><!-->
            <script src="//cdn.jandan.net/static/jquery/2.0.3/jquery.min.js"></script>
            <!--<![endif]-->
            <script src="//cdn.jandan.net/static/js/velocity-1.5.0.min.js"></script>
            <script src="//cdn.jandan.net/static/js/jquery.lazyload.1.9.5.js"></script>
            <script>
                var $JANDAN = {
                    GO_API: false,
                    IS_MOBILE : false,
                    COOKIE_HASH : '01b0531fab6a989460dd1b231010b496',
                    SITE_URL : 'http://jandan.net',
                    API_URL : '//api.jandan.net'
                };
                if (/(Android|iPhone|Windows Phone)/i.test(navigator.userAgent)) {
                    window.location = '//i.jandan.net' + window.location.pathname + window.location.hash;
                }
            </script>
            <!--
            <script src="//cdn.jandan.net/static/min/5daa5dc030f28ff4408ddad5af5b8182.50034911.js"></script>
            -->        <script src="//cdn.jandan.net/static/min/1a5d330246b7aa117cf0439a2688bba45Hg5Yu1f.05100001.js"></script>
            <script>
                eval(function(p,a,c,k,e,r){e=function(c){return c.toString(a)};if(!''.replace(/^/,String)){while(c--)r[e(c)]=k[c]||e(c);k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('(g(){1 d=["j","a","0","d","a","0",".","0","e","f"];1 3=7 8(d.2(\'\')+\'$\');4(!3.9(b.c)){1 a=5.6.h;4(a==\'/\'){a=\'\'}5.6.i=\'k://\'+d.2(\'\')+\'/\'+a}})($l);',22,22,'n|var|join|r|if|window|location|new|RegExp|test||document|domain|||t|function|pathname|href||http|JANDAN'.split('|'),0,{}));
            </script>
        
        <link rel="preload" href="https://adservice.google.com/adsid/integrator.js?domain=jandan.net"><script type="text/javascript" src="https://adservice.google.com/adsid/integrator.js?domain=jandan.net"></script><link rel="preload" href="http://pagead2.googlesyndication.com/pagead/js/r20190522/r20190131/show_ads_impl.js"></head>
        <!-- END html head -->
        <body style="">
        <!-- BEGIN wrapper -->
        
        <div id="wrapper">
        
            <!-- BEGIN header -->
            <div id="header">
                <div class="logo">
                    <h1><a href="/" onclick="ga('send', 'pageview','/header/logo');">煎蛋</a></h1>
                </div>
                <div class="break"></div>
                <div class="nav">
                    <ul class="nav-items">
                        <li class="nav-item f"><a href="/" onfocus="blur()" onclick="ga('send', 'pageview','/header/index');" class="nav-link">首页</a></li>
                        <li class="nav-item x">
                            <a href="javascript:;" class="nav-link">专题</a>
                            <div class="sub-items">
                                <table class="tag-cloud">
                                    <thead>
                                    <tr>
                                        <th>科学</th>
                                        <th>技术</th>
                                        <th>极客</th>
                                        <th>脑洞</th>
                                        <th>故事</th>
                                        <th>人类</th>
                                        <th>折腾</th>
                                    </tr>
                                    </thead>
                                    <tbody>
                                    <tr>
                                        <td><a href="/tag/走进科学" onfocus="blur()">走进科学</a></td>
                                        <td><a href="/tag/tech" onfocus="blur()">TECH</a></td>
                                        <td><a href="/tag/GEEK" onfocus="blur()">GEEK</a></td>
                                        <td><a href="/tag/DIY" onfocus="blur()">DIY</a></td>
                                        <td><a href="/tag/冷新闻" onfocus="blur()">冷新闻</a></td>
                                        <td><a href="/tag/女性" onfocus="blur()">女性</a></td>
                                        <td><a href="/tag/减肥" onfocus="blur()">减肥</a></td>
                                    </tr>
                                    <tr>
                                        <td><a href="/tag/无厘头研究" onfocus="blur()">无厘头研究</a></td>
                                        <td><a href="/tag/人工智能" onfocus="blur()">人工智能</a></td>
                                        <td><a href="/tag/MEME" onfocus="blur()">MEME</a></td>
                                        <td><a href="/tag/艺术" onfocus="blur()">艺术</a></td>
                                        <td><a href="/tag/爷有钱" onfocus="blur()">爷有钱</a></td>
                                        <td><a href="/tag/熊孩子" onfocus="blur()">熊孩子</a></td>
                                        <td><a href="/tag/整形" onfocus="blur()">整形</a></td>
        
                                    </tr>
                                    <tr>
                                        <td><a href="/tag/天文" onfocus="blur()">天文</a></td>
                                        <td><a href="/tag/无人机" onfocus="blur()">无人机</a></td>
                                        <td><a href="/tag/quora" onfocus="blur()">QUORA</a></td>
                                        <td><a href="/tag/设计" onfocus="blur()">设计</a></td>
                                        <td><a href="/tag/致富信息" onfocus="blur()">致富信息</a></td>
                                        <td><a href="/tag/大丈夫" onfocus="blur()">大丈夫</a></td>
                                        <td><a href="/tag/旅游" onfocus="blur()">旅游</a></td>
                                    </tr>
                                    <tr>
                                        <td><a href="/tag/nasa" onfocus="blur()">NASA</a></td>
                                        <td><a href="/tag/3D打印" onfocus="blur()">3D打印</a></td>
                                        <td><a href="/tag/小学堂" onfocus="blur()">小学堂</a></td>
                                        <td><a href="/tag/广告" onfocus="blur()">广告</a></td>
                                        <td><a href="/tag/安全警示" onfocus="blur()">安全警示</a></td>
                                        <td><a href="/tag/笨贼" onfocus="blur()">笨贼</a></td>
                                        <td><a href="/tag/健康" onfocus="blur()">健康</a></td>
                                    </tr>
                                    <tr>
                                        <td><a href="/tag/高科技" onfocus="blur()">高科技</a></td>
                                        <td><a href="/tag/数码产品" onfocus="blur()">数码产品</a></td>
                                        <td><a href="/tag/创意产品" onfocus="blur()">创意产品</a></td>
                                        <td><a href="/tag/建筑" onfocus="blur()">建筑</a></td>
                                        <td><a href="/tag/国内观光" onfocus="blur()">国内观光</a></td>
                                        <td><a href="/tag/真的猛士" onfocus="blur()">真的猛士</a></td>
                                        <td><a href="/tag/教育" onfocus="blur()">教育</a></td>
        
                                    </tr>
                                    <tr>
                                        <td><a href="/tag/环保" onfocus="blur()">环保</a></td>
                                        <td><a href="/tag/虚拟现实" onfocus="blur()">虚拟现实</a></td>
                                        <td><a href="/tag/大吐槽" onfocus="blur()">大吐槽</a></td>
                                        <td><a href="/tag/摄影" onfocus="blur()">摄影</a></td>
                                        <td><a href="/tag/史海钩沉" onfocus="blur()">史海钩沉</a></td>
                                        <td><a href="/tag/正能量" onfocus="blur()">正能量</a></td>
                                        <td><a href="/tag/心理学" onfocus="blur()">心理学</a></td>
                                    </tr>
                                    </tbody>
                                </table>
        
        
                            </div>
                        </li>
                        <li class="nav-item"><a class="nav-link" href="/qa" onfocus="blur()" onclick="ga('send', 'pageview','/header/qa');">问答</a></li>
                        <li class="nav-item"><a class="nav-link" href="/treehole" onfocus="blur()" onclick="ga('send', 'pageview','/header/treehole');">树洞</a></li>
                        <li class="nav-item"><a class="nav-link" href="/ooxx" onfocus="blur()" onclick="ga('send', 'pageview','/header/ooxx');">随手拍</a></li>
                        <li class="nav-item"><a class="nav-link" href="/zoo" onfocus="blur()" onclick="ga('send', 'pageview','/header/zoo');">动物园</a></li>
                        <li class="nav-item"><a class="nav-link" href="/pic" onfocus="blur()" onclick="ga('send', 'pageview','/header/pic');">无聊图</a></li>
                        <li class="nav-item"><a class="nav-link" href="/top" onfocus="blur()" onclick="ga('send', 'pageview','/header/top');">热榜</a></li>
                        <li class="nav-item" style="float:right;"><a class="nav-link" style="color:#666" href="/pond" onfocus="blur()" onclick="ga('send', 'pageview','/header/pond');">鱼塘</a></li>
                        <li class="nav-item" style="float:right;"><a class="nav-link" style="color:#666" href="/zhoubian" onfocus="blur()" onclick="ga('send', 'pageview','/header/zhoubian');">周边</a></li>
        
                    </ul>
                    <div class="break"></div>
                </div>
            </div>
            <!-- END header -->
        
            <!-- BEGIN body -->
            <div id="body">
            <!-- BEGIN content -->
            <div id="content">
                            <h1 class="title">随手拍</h1>
                    <!-- begin post -->
                    <div class="post f">
                        <p>大家手机相册里应该有不少有趣的图片，欢迎发到这里，分享你的经典一刻。</p>
        <p><small><strong>发图方法</strong><br>
        上传到<a href="//photo.weibo.com/photos/upload">微博相册</a>；右键复制图片地址，在<a href="#respond">评论框</a>粘帖图片地址；等待更新。<br>
        请勿发布AV截图/裸体/露点图/偷拍、带有网址/商标/二维码等水印、涉嫌隐私或转载他人的未授权图片。<br>
        </small></p>
        <hr>
                        <style>
            .switch {
                display: inline-block;
                padding: 0 5px;
                border: 1px solid #444;
                cursor: pointer;
                line-height: 14px;
                text-align: center;
                color: #aaa;
                font-size: 10px;
                vertical-align: middle;
            }
            .switch-current {
                background-color: #333;
                color: #fff;
        
            }
        
        </style>
        <p>
            GIF图点击加载: <span class="switch switch-current" id="gif-click-load-on">ON</span><span class="switch" id="gif-click-load-off">OFF</span>&nbsp;&nbsp;
            NSFW图自动隐藏: <span class="switch switch-current" id="nsfw-click-load-on">ON</span><span class="switch" id="nsfw-click-load-off">OFF</span>&nbsp;&nbsp;
            隐藏不受欢迎图片: <span class="switch switch-current" id="bad-click-load-on">ON</span><span class="switch" id="bad-click-load-off">OFF</span>
        </p>			</div>
                    <!-- end post -->
                    <!-- begin comments -->
                    <div id="comments">
        
            <div style="clear:both;"></div>
        
            <h3 class="title" id="comments"><span class="plusone"><a href="#respond" title="来一发">+1</a></span></h3>
        
        
            <span class="break"></span>
            <div class="comments">
                                <div class="cp-pagenavi">
                                                                    <span class="current-comment-page">[25]</span>
                                                                    <a href="//jandan.net/ooxx/page-24#comments">
                            24                </a>
                                                                    <a href="//jandan.net/ooxx/page-23#comments">
                            23                </a>
                                                            <a title="Older Comments" href="//jandan.net/ooxx/page-24#comments" class="previous-comment-page">下一页</a>
                            </div>
                    </div>
        
        
            <ol class="commentlist" style="list-style-type: none;">
        
        
                    <li id="comment-4258748">
                        <div>
                            <div class="row">
                                <div class="author"><strong title="防伪码：5bfef5f2efa2c4fbcd46f18093efb7a3a6a252fb" class="">AOI</strong>                            <br>
                                    <small><a href="#footer" title="@回复" onclick="document.getElementById('comment').value += '@&lt;a href=&quot;//jandan.net/ooxx/page-25#comment-4258748&quot;&gt;AOI&lt;/a&gt;: '">@1 hour ago</a></small>
                                </div>
                                <div class="text"><span class="righttext"><a href="/t/4258748">4258748</a></span><p>安卓客戶端沒法一次透多張圖？<br>
        <a href="//ws4.sinaimg.cn/large/abac4104ly1g3dxrn2ybmj20rr1kwk8q.jpg" target="_blank" class="view_img_link" referrerpolicy="no-referrer">[查看原图]</a><br><img src="//ws4.sinaimg.cn/mw600/abac4104ly1g3dxrn2ybmj20rr1kwk8q.jpg" referrerpolicy="no-referrer" style="max-width: 480px; max-height: 750px;"></p>
                                </div>
                                <div class="jandan-vote">
                                    <span class="comment-report-c">
                                        <a title="举报" href="javascript:;" class="comment-report" data-id="4258748">[举报]</a>
                                    </span>
                                    <span class="tucao-like-container">
                                    <a title="圈圈/支持" href="javascript:;" class="comment-like like" data-id="4258748" data-type="pos">OO</a> [<span>7</span>]
                                    </span>
                                    <span class="tucao-unlike-container">
                                    <a title="叉叉/反对" href="javascript:;" class="comment-unlike unlike" data-id="4258748" data-type="neg">XX</a> [<span>1</span>]
        
                                    <a href="javascript:;" class="tucao-btn" data-id="4258748"> 吐槽 [0] </a>
                                    </span>
                                </div>
                            </div>
                        </div>
                    </li>
        
        
        
        
                    <li id="comment-4258747">
                        <div>
                            <div class="row">
                                <div class="author"><strong title="防伪码：5bfef5f2efa2c4fbcd46f18093efb7a3a6a252fb" class="">AOI</strong>                            <br>
                                    <small><a href="#footer" title="@回复" onclick="document.getElementById('comment').value += '@&lt;a href=&quot;//jandan.net/ooxx/page-25#comment-4258747&quot;&gt;AOI&lt;/a&gt;: '">@1 hour ago</a></small>
                                </div>
                                <div class="text"><span class="righttext"><a href="/t/4258747">4258747</a></span><p><a href="//wx2.sinaimg.cn/large/abac4104ly1g3dxr45dc5j20uk0s9n6n.jpg" target="_blank" class="view_img_link" referrerpolicy="no-referrer">[查看原图]</a><br><img src="//wx2.sinaimg.cn/mw600/abac4104ly1g3dxr45dc5j20uk0s9n6n.jpg" referrerpolicy="no-referrer" style="max-width: 480px; max-height: 750px;"></p>
                                </div>
                                <div class="jandan-vote">
                                    <span class="comment-report-c">
                                        <a title="举报" href="javascript:;" class="comment-report" data-id="4258747">[举报]</a>
                                    </span>
                                    <span class="tucao-like-container">
                                    <a title="圈圈/支持" href="javascript:;" class="comment-like like" data-id="4258747" data-type="pos">OO</a> [<span>6</span>]
                                    </span>
                                    <span class="tucao-unlike-container">
                                    <a title="叉叉/反对" href="javascript:;" class="comment-unlike unlike" data-id="4258747" data-type="neg">XX</a> [<span>2</span>]
        
                                    <a href="javascript:;" class="tucao-btn" data-id="4258747"> 吐槽 [1] </a>
                                    </span>
                                </div>
                            </div>
                        </div>
                    </li>
        
        
        
        
                    <li id="comment-4258730">
                        <div>
                            <div class="row">
                                <div class="author"><strong title="防伪码：0a1b5ea5e18bf18fb3b8b16c3a0bc2ddc47e75e0" class="">naqu</strong>                            <br>
                                    <small><a href="#footer" title="@回复" onclick="document.getElementById('comment').value += '@&lt;a href=&quot;//jandan.net/ooxx/page-25#comment-4258730&quot;&gt;naqu&lt;/a&gt;: '">@2 hours ago</a></small>
                                </div>
                                <div class="text"><span class="righttext"><a href="/t/4258730">4258730</a></span><p><a href="//wx1.sinaimg.cn/large/007JBZrwly1g3dtjknbrjj327m0u01iq.jpg" target="_blank" class="view_img_link" referrerpolicy="no-referrer">[查看原图]</a><br><img src="//wx1.sinaimg.cn/mw600/007JBZrwly1g3dtjknbrjj327m0u01iq.jpg" referrerpolicy="no-referrer" style="max-width: 480px; max-height: 750px;"></p>
                                </div>
                                <div class="jandan-vote">
                                    <span class="comment-report-c">
                                        <a title="举报" href="javascript:;" class="comment-report" data-id="4258730">[举报]</a>
                                    </span>
                                    <span class="tucao-like-container">
                                    <a title="圈圈/支持" href="javascript:;" class="comment-like like" data-id="4258730" data-type="pos">OO</a> [<span>10</span>]
                                    </span>
                                    <span class="tucao-unlike-container">
                                    <a title="叉叉/反对" href="javascript:;" class="comment-unlike unlike" data-id="4258730" data-type="neg">XX</a> [<span>2</span>]
        
                                    <a href="javascript:;" class="tucao-btn" data-id="4258730"> 吐槽 [1] </a>
                                    </span>
                                </div>
                            </div>
                        </div>
                    </li>
        
        
                                            <span class="break"></span><li class="row">
        <div style="padding-left:120px;padding-top:10px;padding-bottom:15px;width:336px;">
        <!-- 336-tuwen -->
        <div id="_9ui1hlunpvr" style=""><iframe width="336" frameborder="0" height="280" scrolling="no" src="http://pos.baidu.com/s?hei=280&amp;wid=336&amp;di=u529095&amp;ltu=http%3A%2F%2Fjandan.net%2Fooxx&amp;psi=401cce5b954a74bd0cffb6014379891a&amp;drs=3&amp;tcn=1558799414&amp;ari=2&amp;tpr=1558799413950&amp;ps=2180x141&amp;pis=-1x-1&amp;pss=984x4208&amp;exps=111000,119008,110011&amp;pcs=400x300&amp;cec=UTF-8&amp;ccd=32&amp;psr=1366x768&amp;dis=0&amp;cdo=-1&amp;cja=false&amp;cce=true&amp;dtm=HTML_POST&amp;dri=0&amp;cfv=0&amp;cpl=0&amp;dai=1&amp;ant=0&amp;ti=%E9%9A%8F%E6%89%8B%E6%8B%8D%20-%20%E5%88%86%E4%BA%AB%E7%BB%8F%E5%85%B8%E4%B8%80%E5%88%BB&amp;par=1366x728&amp;tlm=1558770613&amp;col=zh-CN&amp;dc=3&amp;chi=1&amp;cmi=0"></iframe></div><script type="text/javascript" src="//a3.jandan.net/site/api/zxm78u.js?kfcunl=nc"></script></div>
                                </li>            
        
                    <li id="comment-4258706">
                        <div>
                            <div class="row">
                                <div class="author"><strong title="防伪码：a877eb037420d93fc801b08c183540cec5748b24" class="">勾心斗鸡儿</strong>                            <br>
                                    <small><a href="#footer" title="@回复" onclick="document.getElementById('comment').value += '@&lt;a href=&quot;//jandan.net/ooxx/page-25#comment-4258706&quot;&gt;勾心斗鸡儿&lt;/a&gt;: '">@3 hours ago</a></small>
                                </div>
                                <div class="text"><span class="righttext"><a href="/t/4258706">4258706</a></span><p>山上的杏快熟了<br>
        <a href="//ws4.sinaimg.cn/large/765a3737ly1g3dvkr3559j21400u0wwo.jpg" target="_blank" class="view_img_link" referrerpolicy="no-referrer">[查看原图]</a><br><img src="//ws4.sinaimg.cn/mw600/765a3737ly1g3dvkr3559j21400u0wwo.jpg" referrerpolicy="no-referrer" style="max-width: 480px; max-height: 750px;"></p>
                                </div>
                                <div class="jandan-vote">
                                    <span class="comment-report-c">
                                        <a title="举报" href="javascript:;" class="comment-report" data-id="4258706">[举报]</a>
                                    </span>
                                    <span class="tucao-like-container">
                                    <a title="圈圈/支持" href="javascript:;" class="comment-like like" data-id="4258706" data-type="pos">OO</a> [<span>22</span>]
                                    </span>
                                    <span class="tucao-unlike-container">
                                    <a title="叉叉/反对" href="javascript:;" class="comment-unlike unlike" data-id="4258706" data-type="neg">XX</a> [<span>1</span>]
        
                                    <a href="javascript:;" class="tucao-btn" data-id="4258706"> 吐槽 [3] </a>
                                    </span>
                                </div>
                            </div>
                        </div>
                    </li>
        
        
        
        
                    <li id="comment-4258696">
                        <div>
                            <div class="row">
                                <div class="author"><strong title="防伪码：4cfefc8c9785f7222969431a437272ea51301376" class="">kksk</strong>                            <br>
                                    <small><a href="#footer" title="@回复" onclick="document.getElementById('comment').value += '@&lt;a href=&quot;//jandan.net/ooxx/page-25#comment-4258696&quot;&gt;kksk&lt;/a&gt;: '">@3 hours ago</a></small>
                                </div>
                                <div class="text"><span class="righttext"><a href="/t/4258696">4258696</a></span><p>这黑牌是合资公司车辆来着吧?<br>
        <a href="//wx4.sinaimg.cn/large/9aba64b5gy1g3dv2pi39oj21jk15o1ky.jpg" target="_blank" class="view_img_link" referrerpolicy="no-referrer">[查看原图]</a><br><img src="//wx4.sinaimg.cn/mw600/9aba64b5gy1g3dv2pi39oj21jk15o1ky.jpg" referrerpolicy="no-referrer" style="max-width: 480px; max-height: 750px;"></p>
                                </div>
                                <div class="jandan-vote">
                                    <span class="comment-report-c">
                                        <a title="举报" href="javascript:;" class="comment-report" data-id="4258696">[举报]</a>
                                    </span>
                                    <span class="tucao-like-container">
                                    <a title="圈圈/支持" href="javascript:;" class="comment-like like" data-id="4258696" data-type="pos">OO</a> [<span>8</span>]
                                    </span>
                                    <span class="tucao-unlike-container">
                                    <a title="叉叉/反对" href="javascript:;" class="comment-unlike unlike" data-id="4258696" data-type="neg">XX</a> [<span>12</span>]
        
                                    <a href="javascript:;" class="tucao-btn" data-id="4258696"> 吐槽 [8] </a>
                                    </span>
                                </div>
                            </div>
                        </div>
                    </li>
        
        
        
        
                    <li id="comment-4258670">
                        <div>
                            <div class="row">
                                <div class="author"><strong title="防伪码：925c6ef1dcf388f85cf7f78f2501f43f24ef7ef2" class="orange-name">游客</strong>                            <br>
                                    <small><a href="#footer" title="@回复" onclick="document.getElementById('comment').value += '@&lt;a href=&quot;//jandan.net/ooxx/page-25#comment-4258670&quot;&gt;游客&lt;/a&gt;: '">@3 hours ago</a></small>
                                </div>
                                <div class="text"><span class="righttext"><a href="/t/4258670">4258670</a></span><p style="position: relative;"><a href="//wx2.sinaimg.cn/large/6a84d8d8ly1g3dueo0um5g20a00ht1kz.gif" target="_blank" class="view_img_link" referrerpolicy="no-referrer">[查看原图]</a><br><img src="//wx2.sinaimg.cn/thumb180/6a84d8d8ly1g3dueo0um5g20a00ht1kz.gif" org_src="//wx2.sinaimg.cn/mw1024/6a84d8d8ly1g3dueo0um5g20a00ht1kz.gif" onload="add_img_loading_mask(this, load_sina_gif);" referrerpolicy="no-referrer" style="max-width: 480px; max-height: 750px;"><div class="gif-mask" style="top:22px;left:0px;width:180px;height:180px;line-height:180px;">PLAY</div></p>
                                </div>
                                <div class="jandan-vote">
                                    <span class="comment-report-c">
                                        <a title="举报" href="javascript:;" class="comment-report" data-id="4258670">[举报]</a>
                                    </span>
                                    <span class="tucao-like-container">
                                    <a title="圈圈/支持" href="javascript:;" class="comment-like like" data-id="4258670" data-type="pos">OO</a> [<span>16</span>]
                                    </span>
                                    <span class="tucao-unlike-container">
                                    <a title="叉叉/反对" href="javascript:;" class="comment-unlike unlike" data-id="4258670" data-type="neg">XX</a> [<span>5</span>]
        
                                    <a href="javascript:;" class="tucao-btn" data-id="4258670"> 吐槽 [2] </a>
                                    </span>
                                </div>
                            </div>
                        </div>
                    </li>
        
        
        
        
                    <li id="comment-4258660">
                        <div>
                            <div class="row">
                                <div class="author"><strong title="防伪码：16690c05acd6fdc05fb981881f5801142bb8d3b4" class="orange-name">小宝</strong>                            <br>
                                    <small><a href="#footer" title="@回复" onclick="document.getElementById('comment').value += '@&lt;a href=&quot;//jandan.net/ooxx/page-25#comment-4258660&quot;&gt;小宝&lt;/a&gt;: '">@3 hours ago</a></small>
                                </div>
                                <div class="text"><span class="righttext"><a href="/t/4258660">4258660</a></span><p><a href="//ws4.sinaimg.cn/large/00745YaMgy1g3dtxfaxiqj312l1bgb29.jpg" target="_blank" class="view_img_link" referrerpolicy="no-referrer">[查看原图]</a><br><img src="//ws4.sinaimg.cn/mw600/00745YaMgy1g3dtxfaxiqj312l1bgb29.jpg" referrerpolicy="no-referrer" style="max-width: 480px; max-height: 750px;"></p>
                                </div>
                                <div class="jandan-vote">
                                    <span class="comment-report-c">
                                        <a title="举报" href="javascript:;" class="comment-report" data-id="4258660">[举报]</a>
                                    </span>
                                    <span class="tucao-like-container">
                                    <a title="圈圈/支持" href="javascript:;" class="comment-like like" data-id="4258660" data-type="pos">OO</a> [<span>8</span>]
                                    </span>
                                    <span class="tucao-unlike-container">
                                    <a title="叉叉/反对" href="javascript:;" class="comment-unlike unlike" data-id="4258660" data-type="neg">XX</a> [<span>2</span>]
        
                                    <a href="javascript:;" class="tucao-btn" data-id="4258660"> 吐槽 [1] </a>
                                    </span>
                                </div>
                            </div>
                        </div>
                    </li>
        
        
        
        
            </ol>
            <div class="comments">
                        <div class="cp-pagenavi">
                                                                    <span class="current-comment-page">[25]</span>
                                                                    <a href="//jandan.net/ooxx/page-24#comments">
                            24                </a>
                                                                    <a href="//jandan.net/ooxx/page-23#comments">
                            23                </a>
                                                            <a title="Older Comments" href="//jandan.net/ooxx/page-24#comments" class="previous-comment-page">下一页</a>
                            </div>
                    </div>
        
        
            <span class="break"></span>
            <div class="comments">
        
        
                <h3>
                    <p id="respond">发表评论</p>
                </h3>
            </div>
        
        
        
                <form method="post" id="commentform">
        
        
                        <div class="hide-input">
                            <p><label for="author">称呼: </label><input type="text" name="author" id="author" value="" title="常用的网络 ID，必填项" size="22" tabindex="1"></p>
        
                            <p><label for="email">邮箱: </label><input type="text" name="email" id="email" value="" title="真实 Email 地址，必填项" size="22" tabindex="2"></p>
                        </div>
        
        
                    <p><textarea name="comment" id="comment" rows="10" tabindex="4" onkeydown="if(event.ctrlKey&amp;&amp;event.keyCode==13){document.getElementById('submit').click();return false};"></textarea><div id="loading" class="loading" style="display: none;"></div><div id="error" style="display: none;">#</div>
                    </p>
        
                    <p><input name="submit" id="submit" type="submit" tabindex="5" value="点击发布 / Ctrl+Enter">
        
                        <input type="hidden" name="comment_post_ID" id="comment_post_ID" value="21183">
                        <br></p>
        
                </form>
        
        
        </div>
                    <!-- end comments -->
                    <div id="tucao-gg">
            <div style="padding:20px 0 10px 125px;border-top:1px solid #EEE;border-bottom:1px solid #EEE;"><div style="width:336px;">
            <font color="#AAA">[ 广告 ]</font><br>
            <!-- 336 adx -->
            <script type="text/javascript"><!--
        google_ad_client = "ca-pub-5673546663729848";
        /* 煎蛋网-首页-336x280 */
        google_ad_slot = "1965170595/jandannet-home-336x280";
        google_ad_width = 336;
        google_ad_height = 280;
        //-->
        </script>
        <script type="text/javascript" src="//pagead2.googlesyndication.com/pagead/show_ads.js">
        </script><ins id="aswift_0_expand" style="display:inline-table;border:none;height:280px;margin:0;padding:0;position:relative;visibility:visible;width:336px;background-color:transparent;" data-ad-slot="1965170595/jandannet-home-336x280"><ins id="aswift_0_anchor" style="display:block;border:none;height:280px;margin:0;padding:0;position:relative;visibility:visible;width:336px;background-color:transparent;"><iframe width="336" height="280" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" onload="var i=this.id,s=window.google_iframe_oncopy,H=s&amp;&amp;s.handlers,h=H&amp;&amp;H[i],w=this.contentWindow,d;try{d=w.document}catch(e){}if(h&amp;&amp;d&amp;&amp;(!d.body||!d.body.firstChild)){if(h.call){setTimeout(h,0)}else if(h.match){try{h=s.upd(h,i)}catch(e){}w.location.replace(h)}}" id="aswift_0" name="aswift_0" style="left:0;position:absolute;top:0;border:0px;width:336px;height:280px;"></iframe></ins></ins>    </div></div>
        </div>
        <script>
            (function($) {
                var prev = $('<span id="nav_prev"><a href="javascript:;" title="上一页">&#8250;</a></span>');
                var next = $('<span id="nav_next"><a href="javascript:;" title="下一页">&#8249;</a></span>');
        
                $('#body').append(prev).append(next);
                $().ready(function() {
                    var prev_link = $('.next-comment-page');
                    if (prev_link.length > 0) {
                        next.show();
                        next.find('a').attr('href', prev_link.attr('href'));
                    } else {
                        next.hide();
                    }
        
                    var next_link = $('.previous-comment-page');
                    if (next_link.length > 0) {
                        prev.show();
                        prev.find('a').attr('href', next_link.attr('href'));
                    } else {
                        prev.hide();
                    }
                });
            })($);
        </script>
                    <script>
            var gif_click_load = getCookie('gif-click-load');
            var bad_click_load = getCookie('bad-click-load');
            var nsfw_click_load = getCookie('nsfw-click-load');
            var gif_on = (gif_click_load == 'on' || gif_click_load == null) ? true : false;
            var nsfw_on = (nsfw_click_load == 'on' || nsfw_click_load == null) ? true : false;
            var bad_on = (bad_click_load == 'on' || bad_click_load == null) ? true : false;
        
        
            $('.switch').removeClass('switch-current');
            var btn_id = 'gif-click-load-off';
            if (gif_on) {
                btn_id = 'gif-click-load-on';
            }
            $('#'+btn_id).addClass('switch-current');
        
            btn_id = 'nsfw-click-load-off';
            if (nsfw_on) {
                btn_id = 'nsfw-click-load-on';
            }
            $('#'+btn_id).addClass('switch-current');
        
        
            btn_id = 'bad-click-load-off';
            if (bad_on) {
                btn_id = 'bad-click-load-on';
            }
            $('#'+btn_id).addClass('switch-current');
        
        
        
            $('#gif-click-load-on').click(function() {
        
                if ($(this).hasClass('switch-current'))
                    return;
                setCookie('gif-click-load', 'on', 30);
                $('#gif-click-load-off').removeClass('switch-current');
                $(this).addClass('switch-current');
                location.reload();
            });
        
            $('#gif-click-load-off').click(function() {
                if ($(this).hasClass('switch-current'))
                    return;
                setCookie('gif-click-load', 'off', 30);
                $('#gif-click-load-on').removeClass('switch-current');
                $(this).addClass('switch-current');
                location.reload();
            });
        
            $('#nsfw-click-load-on').click(function() {
                if ($(this).hasClass('switch-current'))
                    return;
                setCookie('nsfw-click-load', 'on', 30);
                $('#nsfw-click-load-off').removeClass('switch-current');
                $(this).addClass('switch-current');
                location.reload();
            });
        
            $('#nsfw-click-load-off').click(function() {
                if ($(this).hasClass('switch-current'))
                    return;
                setCookie('nsfw-click-load', 'off', 30);
                $('#nsfw-click-load-on').removeClass('switch-current');
                $(this).addClass('switch-current');
                location.reload();
            });
        
            $('#bad-click-load-on').click(function() {
                if ($(this).hasClass('switch-current'))
                    return;
                setCookie('bad-click-load', 'on', 30);
                $('#bad-click-load-off').removeClass('switch-current');
                $(this).addClass('switch-current');
                location.reload();
            });
        
            $('#bad-click-load-off').click(function() {
                if ($(this).hasClass('switch-current'))
                    return;
                setCookie('bad-click-load', 'off', 30);
                $('#bad-click-load-on').removeClass('switch-current');
                $(this).addClass('switch-current');
                location.reload();
            });
            $(".commentlist li").each(function () {
                var e = $(this);
                var is_bad = false;
                if (bad_on) {
                    var oo = parseInt(e.find('.comment-like').next('span').text());
                    var xx = parseInt(e.find('.comment-unlike').next('span').text());
                    // oo xx 总和超过50个，且xx占多数
                    if ( (oo + xx) >= 50 && (oo / xx) < 0.618 ) {
                        is_bad = true;
                        var r = e.find("p").not('.bad_content');
                        r.hide();
                        e.find('.righttext').after('<p class="bad_content" style="color:#ddd">因不受欢迎已被超载鸡自动隐藏.  <a href="javascript:;" class="view_bad">[手贱一回]</a></p>');
                        e.find(".view_bad").click(function () {
                            if (this.innerHTML == '[手贱一回]' || this.innerHTML == '[再手贱一回]') {
                                r.show();
                                if (this.innerHTML == '[手贱一回]') {
                                    r.find('.gif-mask').remove();
                                    r.find('img').each(function() {
                                        var org_src = this.getAttribute('org_src');
                                        if (org_src)
                                            this.src = org_src;
                                    });
                                }
                                this.innerHTML = '[真不该手贱]';
                            } else {
                                r.hide();
                                this.innerHTML = '[再手贱一回]';
                            }
                        });
                    }
                }
        
                if ( ! is_bad && nsfw_on) {
                    var p = e.find("p").not('.bad_content');
                    if (p.length == 0) // ad line
                        return;
                    var content = p.html();
                    if (content.indexOf('NSFW') > -1) {
                        p.hide();
                        e.find('.righttext').after('<p class="nsfw_content" style="color:#ff6600">此图被标记为<b>NSFW</b>被超载鸡自动隐藏.  <a href="javascript:;" class="view_nsfw">[旁边没人]</a></p>');
                        e.find(".view_nsfw").click(function () {
                            if (this.innerHTML == '[旁边没人]' || this.innerHTML == '[旁边还是没人]') {
                                p.show();
                                p.find('.gif-mask').remove();
                                if (this.innerHTML == '[旁边没人]') {
                                    p.find('img').each(function() {
                                        var org_src = this.getAttribute('org_src');
                                        if (org_src)
                                            this.src = org_src;
                                    });
                                }
                                this.innerHTML = '[看完了，擦键盘]';
                            } else {
                                p.hide();
                                this.innerHTML = '[旁边还是没人]';
                            }
                        });
                    }
                }
        
            });
        </script>			<script>
            $('.commentlist li p img').each(function (imgIndex) {
                var max_width = $(this).parent().parent().width();
                $(this).css('max-width', max_width);
                $(this).css('max-height', '750px').click(function () {
                    var $this = $(this);
                    if ($this.css('max-height') == 'none') {
                        var max_width = $(this).parent().parent().width();
                        $this.css('max-width', max_width);
                        $this.css('max-height', '750px');
                    } else {
                        if ($this.parent().hasClass('acv_comment'))
                            $this.css('max-width', 'none');
                        $this.css('max-height', 'none');
                    }
                    $("html,body").animate(
                        {
                            scrollTop: $this.offset().top - 40
                        },
                        325
                    );
                });
            });
        </script>
                    <script>
            $("img.lazy").each(function () {
                $(this).lazyload({
                    effect: "fadeIn"
                });
            });
        </script>            <script>
            $().ready(function () {
                $comments = $('#comments-title');
                $cancel = $('#cancel-comment-reply-link');
                cancel_text = $cancel.text();
                $submit = $('#commentform #submit');
                $submit.attr('disabled', false);
                $('#comment').after('<div id="loading"class="loading"></div><div id="error">#</div>');
                $('#loading').hide();
                $('#error').hide();
                function nl2br(str) {
                    var breakTag = '<br>';
                    return (str + '').replace(/([^>\r\n]?)(\r\n|\n\r|\r|\n)/g, '$1' + breakTag + '$2');
                }
                $('#commentform').submit(function () {
                    $('#loading').slideDown();
                    $submit.attr('disabled', false);
                    $.ajax({
                        url: '/jandan-comment.php',
                        data: $(this).serialize(),
                        type: $(this).attr('method'),
                        error: function (request) {
                            $('#loading').slideUp();
                            var errorhtml = request.responseText;
                            errorhtml = errorhtml.replace(/WordPress &rsaquo; Error/i, "");
                            $('#error').slideDown().html('<p style="color:red;"> ' + errorhtml + '</p> ');
                            setTimeout(function () {
                                $submit.attr('disabled', false).fadeTo('slow', 1);
                                $('#error').slideUp();
                            }, 5000);
                        },
                        success: function (comment_id) {
                            $('#loading').hide();
        
                            var new_row = [];
                            new_row.push('<li id="comment-#id#" style="display:none;">');
                            new_row.push('<div>');
                            new_row.push('<div class="row">');
                            new_row.push('<div class="author"><strong>'+ $('#author').val() +'</strong>');
                            new_row.push('<br>');
                            new_row.push('<small>');
                            new_row.push('<a href="javascript:;" title="@1 min ago" >@1 min ago</a>');
                            new_row.push('</small>');
                            new_row.push('</div>');
                            new_row.push('<div class="text"><p>'+ nl2br($('#comment').val()) +'</p>');
                            new_row.push('<div class="vote" id="vote-#id#">');
                            new_row.push('<span id="acv_stat_"></span>');
                            new_row.push('<a title="圈圈/支持" class="acvclick acv4" id="vote4-#id#" href="javascript:acv_vote(#id#,1);">oo</a> [<span id="cos_support-#id#">0</span>]');
                            new_row.push('<a title="叉叉/反对" class="acvclick acva" id="votea-#id#" href="javascript:acv_vote(#id#,0);">xx</a> [<span id="cos_unsupport-#id#">0</span>]</div>');
                            new_row.push('</div>');
                            new_row.push('</div>');
                            new_row.push('<span class="break"></span></div>');
                            new_row.push('</li>');
        
                            var new_row_html = new_row.join("\n").replace(/#id#/g, comment_id);
                            $('.commentlist').append(new_row_html);
        
                            $('textarea').each(function () {
                                this.value = ''
                            });
        
                            $('#comment-' + comment_id).fadeIn();
                            $body = (window.opera) ? (document.compatMode == "CSS1Compat" ? $('html') : $('body')) : $('html,body');
                            $body.animate({
                                scrollTop: $('#comment-' + comment_id).offset().top - 200
                            }, 900);
                        }
                    });
                    return false
                });
        
                $('textarea').keypress(function (e) {
                    if (e.ctrlKey && e.which == 13 || e.which == 10) {
                        $(this).parent().submit()
                    }
                });
        
                // 显示＠信息
                $('.commentlist li p a').each(function () {
                    var $this = $(this);
                    if ($this.attr('href').match(/^#comment-/)) {
                        $this.addClass('atreply').hover(function (e) {
                            $($this.attr('href')).clone().hide().insertAfter($this.parents('li')).attr('id', '').addClass('tip').fadeIn(200)
                        }, function () {
                            $('.tip').fadeOut(400, function () {
                                $(this).remove()
                            })
                        })
                    }
                });
        
                var comment_author = getCookie('comment_author_'+ $JANDAN.COOKIE_HASH);
                var comment_email = getCookie('comment_author_email_'+ $JANDAN.COOKIE_HASH);
                if (comment_author) {
                    var author = htmlEscape(decodeURIComponent(comment_author));
                    $('#commentform #author').val(author);
                    var edit = $('<a href="javascript:;">EDIT</a>').click(function() {
                        $('.hide-input').toggle();
                    });
                    $('#respond').html(author + ', 想说点什么? &nbsp;&nbsp;').append(edit);
                    $('.hide-input').hide();
                }
                if (comment_email) {
                    $('#commentform #email').val(decodeURIComponent(comment_email));
                }
            });
        </script>		
            </div><span id="nav_prev"><a href="//jandan.net/ooxx/page-24#comments" title="上一页">›</a></span><span id="nav_next" style="display: none;"><a href="javascript:;" title="下一页">‹</a></span>
            <!-- END content -->
        
        <!-- BEGIN sidebar -->
        <div id="sidebar">
        
               <form action="https://www.so.com/s" target="_blank" id="cse-search-box">
           <input type="text" autocomplete="off" name="q" id="s" value="" placeholder="搜索">
                <button type="submit" id="so360_submit">Search</button>
                <input type="hidden" name="ie" value="utf8">
                <input type="hidden" name="src" value="zz_jandan.net">
                <input type="hidden" name="site" value="jandan.net">
                <input type="hidden" name="rg" value="1">
            </form>
        
        <!--1- top banner -->
                    <!-- ad middle -->
                <ul><!-- 300-adx -->
                    <script type="text/javascript"><!--
        google_ad_client = "ca-pub-5673546663729848";
        /* 煎蛋网-全站侧栏-300x250 */
        google_ad_slot = "1965170595/jandannet-sidebar-300x250";
        google_ad_width = 300;
        google_ad_height = 250;
        //-->
        </script>
        <script type="text/javascript" src="//pagead2.googlesyndication.com/pagead/show_ads.js">
        </script><ins id="aswift_1_expand" style="display:inline-table;border:none;height:250px;margin:0;padding:0;position:relative;visibility:visible;width:300px;background-color:transparent;" data-ad-slot="1965170595/jandannet-sidebar-300x250"><ins id="aswift_1_anchor" style="display:block;border:none;height:250px;margin:0;padding:0;position:relative;visibility:visible;width:300px;background-color:transparent;"><iframe width="300" height="250" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" onload="var i=this.id,s=window.google_iframe_oncopy,H=s&amp;&amp;s.handlers,h=H&amp;&amp;H[i],w=this.contentWindow,d;try{d=w.document}catch(e){}if(h&amp;&amp;d&amp;&amp;(!d.body||!d.body.firstChild)){if(h.call){setTimeout(h,0)}else if(h.match){try{h=s.upd(h,i)}catch(e){}w.location.replace(h)}}" id="aswift_1" name="aswift_1" style="left:0;position:absolute;top:0;border:0px;width:300px;height:250px;"></iframe></ins></ins>        </ul>
        
        <!-- 2- direct banner -->
        <ul>
        <a href="//api.jandan.net/money.php?redirect_id=172" target="_blank" rel="external nofollow"><img src="//cdn.jandan.net/static/ss/recreate-games.gif" border="0" height="75" width="300"></a><span class="dot" data-id="172"></span><!-- recreate games -->
        
        </ul>
        
        <!-- 公告 -->
        <ul>
        <strong>网站公告</strong><br>
        1/ 蛋T补货： [<a href="https://item.taobao.com/item.htm?id=590677279605" target="_blank"><strong>唔想返工</strong></a>] [<a href="https://item.taobao.com/item.htm?id=593509459360" target="_blank"><strong>返工兽DIO!</strong></a>] <br>
        2/ 目前评论和吐槽全部人工审核<br>
        3/ 如有违规内容请直接站内举报，或邮件联系 sein@jandan.com 
        </ul>
        <!-- 3-middle  content -->
        
        
        <!-- 5-last banner -->
        
                        <!-- other stick -->
                 <div id="box">
                    <div id="float" class="box">
                        <ul><!-- 300-baidu -->
                            <div id="_hex7osy41oo" style="width: 300px; height: 250px; display: inline-block;"><iframe id="iframeu608784_0" name="iframeu608784_0" src="http://pos.baidu.com/lccm?conwid=300&amp;conhei=250&amp;rdid=3147009&amp;dc=3&amp;exps=110011&amp;psi=401cce5b954a74bd0cffb6014379891a&amp;di=u608784&amp;dri=0&amp;dis=0&amp;dai=2&amp;ps=1166x661&amp;enu=encoding&amp;dcb=___adblockplus&amp;dtm=HTML_POST&amp;dvi=0.0&amp;dci=-1&amp;dpt=none&amp;tsr=0&amp;tpr=1558799414014&amp;ti=%E9%9A%8F%E6%89%8B%E6%8B%8D%20-%20%E5%88%86%E4%BA%AB%E7%BB%8F%E5%85%B8%E4%B8%80%E5%88%BB&amp;ari=2&amp;dbv=0&amp;drs=3&amp;pcs=400x300&amp;pss=984x4493&amp;cfv=0&amp;cpl=0&amp;chi=1&amp;cce=true&amp;cec=UTF-8&amp;tlm=1558770614&amp;rw=320&amp;ltu=http%3A%2F%2Fjandan.net%2Fooxx&amp;ecd=1&amp;uc=1366x728&amp;pis=-1x-1&amp;sr=1366x768&amp;tcn=1558799414&amp;qn=1d33bbf008114b69&amp;tt=1558799413990.29.30.132" width="300" height="250" align="center,center" vspace="0" hspace="0" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" style="border:0;vertical-align:bottom;margin:0;width:300px;height:250px" allowtransparency="true"></iframe></div><script type="text/javascript" src="//a3.jandan.net/common/js/openjs/ml8rwn.js?niho=kjke"></script>                </ul>
                        <ul><!-- 300-adx-->
                            <script type="text/javascript"><!--
        google_ad_client = "ca-pub-5673546663729848";
        /* 煎蛋网-全站侧栏-300x250 */
        google_ad_slot = "1965170595/jandannet-sidebar-300x250";
        google_ad_width = 300;
        google_ad_height = 250;
        //-->
        </script>
        <script type="text/javascript" src="//pagead2.googlesyndication.com/pagead/show_ads.js">
        </script><ins id="aswift_2_expand" style="display:inline-table;border:none;height:250px;margin:0;padding:0;position:relative;visibility:visible;width:300px;background-color:transparent;" data-ad-slot="1965170595/jandannet-sidebar-300x250"><ins id="aswift_2_anchor" style="display:block;border:none;height:250px;margin:0;padding:0;position:relative;visibility:visible;width:300px;background-color:transparent;"><iframe width="300" height="250" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" onload="var i=this.id,s=window.google_iframe_oncopy,H=s&amp;&amp;s.handlers,h=H&amp;&amp;H[i],w=this.contentWindow,d;try{d=w.document}catch(e){}if(h&amp;&amp;d&amp;&amp;(!d.body||!d.body.firstChild)){if(h.call){setTimeout(h,0)}else if(h.match){try{h=s.upd(h,i)}catch(e){}w.location.replace(h)}}" id="aswift_2" name="aswift_2" style="left:0;position:absolute;top:0;border:0px;width:300px;height:250px;"></iframe></ins></ins>                </ul>
                    </div>
                </div>
        
        
        
            <!-- hot-tabs JS -->
            <script>
            (function($) {
                function add_show_more() {
                    var $this = $(this);
                    var pHeight = 0;
                    $this.find('p').each(function () {
                        pHeight += $(this).height();
                    });
                    if (pHeight > $this.height()) {
                        var show_more = $this.find('.show_more');
                        if (show_more.length == 0) {
                            $this.append('<div class="show_more"> &DownTeeArrow;  展开</div>')
                        }
                    }
                }
        
                $('.hot-tabs li').click(function () {
                    var tab = this.id.split('-')[1];
                    var parent = $(this).parent();
                    parent.find('li').removeClass('current');
                    parent.parent().find('.hot-list-item').removeClass('hot-list-item-current');
                    $(this).addClass('current');
                    var list_tab = $('#list-' + tab);
                    list_tab.addClass('hot-list-item-current');
                    list_tab.find('.acv_comment').each(add_show_more);
                    list_tab.find('.gif-mask').each(function () {
                        var $this = $(this);
                        if ($this.height() > 0) {
                            return;
                        }
                        $this.parent().css('position', 'relative');
                        var img = $this.prev();
                        var position = img.position();
                        $this.css({
                            'height': img.height(),
                            'width': img.width(),
                            'line-height': img.height() + 'px',
                            'left': position.left,
                            'top': position.top
                        });
                    });
                });
                $(window).load(function () {
                    $('.acv_comment').click(function () {
                        var $this = $(this);
                        var show_more = $this.find('.show_more');
                        if (show_more.length == 0) {
                            return;
                        }
                        if (!$this.hasClass('acv_comment_full_size')) {
                            $this.addClass('acv_comment_full_size');
                            show_more.html(' &UpTeeArrow; 收起');
                        } else {
                            $this.removeClass('acv_comment_full_size');
                            show_more.html(' &DownTeeArrow; 展开');
                        }
                    }).each(add_show_more);
                });
            })($);
        </script>
            <!-- END sidebar -->
        
            <div class="break"></div>
        </div>
        <!-- END body -->
        <!-- BEGIN footer -->
        </div>
        <a id="nav_top" style="cursor:pointer;" title="回到页头"><span>▲</span></a>
        <div id="footer">
                <a href="http://www.beian.miit.gov.cn/" target="_blank" rel="external nofollow">鄂ICP备11008023号-1</a> ·  <a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=42018502002747" target="_blank" rel="external nofollow">鄂公网安备42018502002747号</a> ·  投稿及反馈：TG@jandan.com
        </div>
        <!-- END footer -->
        <!-- BEGIN JS -->
        <script>
        (function(){
            var bp = document.createElement('script');
             bp.src = 'http://push.zhanzhang.baidu.com/push.js'; 
             var s = document.getElementsByTagName("script")[0];
            s.parentNode.insertBefore(bp, s);
        })();
        </script>
        
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async="" src="https://www.googletagmanager.com/gtag/js?id=UA-462921-3"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());
        
          gtag('config', 'UA-462921-3');
        </script>
        
        
        <!-- END JS -->
        
        </div>
        <!-- END wrapper -->
        
        
        <iframe id="google_osd_static_frame_9896039753220" name="google_osd_static_frame" style="display: none; width: 0px; height: 0px;"></iframe></body><iframe id="google_esf" name="google_esf" src="http://googleads.g.doubleclick.net/pagead/html/r20190522/r20190131/zrt_lookup.html#" data-ad-client="ca-pub-5673546663729848" style="display: none;"></iframe></html>
        """
        return html

    def get_1stpage(self):
        "打印首页用来测试选择器，获取页码数，所以直接使用selenium包手写元素获取代码"

        # target = browser.find_element_by_xpath('//span[@class="current-comment-page"]')
        # first_page = target.text
        # first_page = eval(first_page)[0]
        # print("first page is %s" % first_page)
        # browser.close()
        # return first_page

        # html = self.get_html()
        # soup = BeautifulSoup(html, 'lxml')
        # target = soup.find_all(name='img', atrrs={"referrerpolicy": "no-referrer"})
        # tagsee = soup.find_all(name='img', attrs={"referrerpolicy": "no-referrer"})
        # print(target)
        # print(tagsee)

        html = self.get_html()
        soup = BeautifulSoup(html, 'lxml')
        tags = soup.find_all(name='img', attrs={"referrerpolicy": "no-referrer"})
        for tag in tags:
            print(tag)
            # url = tags.get('src')
            url = tag.get('src')
            print(url)

        """
        <img referrerpolicy="no-referrer" src="//ws4.sinaimg.cn/mw600/abac4104ly1g3dxrn2ybmj20rr1kwk8q.jpg" style="max-width: 480px; max-height: 750px;"/>
        //ws4.sinaimg.cn/mw600/abac4104ly1g3dxrn2ybmj20rr1kwk8q.jpg
        <img referrerpolicy="no-referrer" src="//wx2.sinaimg.cn/mw600/abac4104ly1g3dxr45dc5j20uk0s9n6n.jpg" style="max-width: 480px; max-height: 750px;"/>
        //wx2.sinaimg.cn/mw600/abac4104ly1g3dxr45dc5j20uk0s9n6n.jpg
        <img referrerpolicy="no-referrer" src="//wx1.sinaimg.cn/mw600/007JBZrwly1g3dtjknbrjj327m0u01iq.jpg" style="max-width: 480px; max-height: 750px;"/>
        //wx1.sinaimg.cn/mw600/007JBZrwly1g3dtjknbrjj327m0u01iq.jpg
        <img referrerpolicy="no-referrer" src="//ws4.sinaimg.cn/mw600/765a3737ly1g3dvkr3559j21400u0wwo.jpg" style="max-width: 480px; max-height: 750px;"/>
        //ws4.sinaimg.cn/mw600/765a3737ly1g3dvkr3559j21400u0wwo.jpg
        <img referrerpolicy="no-referrer" src="//wx4.sinaimg.cn/mw600/9aba64b5gy1g3dv2pi39oj21jk15o1ky.jpg" style="max-width: 480px; max-height: 750px;"/>
        //wx4.sinaimg.cn/mw600/9aba64b5gy1g3dv2pi39oj21jk15o1ky.jpg
        <img onload="add_img_loading_mask(this, load_sina_gif);" org_src="//wx2.sinaimg.cn/mw1024/6a84d8d8ly1g3dueo0um5g20a00ht1kz.gif" referrerpolicy="no-referrer" src="//wx2.sinaimg.cn/thumb180/6a84d8d8ly1g3dueo0um5g20a00ht1kz.gif" style="max-width: 480px; max-height: 750px;"/>
        //wx2.sinaimg.cn/thumb180/6a84d8d8ly1g3dueo0um5g20a00ht1kz.gif
        <img referrerpolicy="no-referrer" src="//ws4.sinaimg.cn/mw600/00745YaMgy1g3dtxfaxiqj312l1bgb29.jpg" style="max-width: 480px; max-height: 750px;"/>
        //ws4.sinaimg.cn/mw600/00745YaMgy1g3dtxfaxiqj312l1bgb29.jpg
        """


    def search_img_url(self, html):
        url_list = []
        soup = BeautifulSoup(html, 'lxml')
        for img_url_tag in soup.find_all('img'):
            img_urls = img_url_tag.find_all(atrrs={"referrerpolicy": "no-referrer"})
            for each in img_urls:
                img_url = each.img['src']
                print(img_url)
                url_list.append(img_url)
        return url_list

    def visit_page(self, first_page):
        url_list = []
        for i in range(self.page):
            page_num = first_page - i
            url = "http://jandan.net/ooxx/page-" + str(page_num) + "#comments"
            print('start getting page: ', url)
            html = self.get_html()
            list = self.search_img_url(html)
            url_list += list
        return url_list

    def get_img(self, url_list):
        file_num = 0
        for url in url_list:
            file_name = str(file_num) + ".jpg"
            response = requests.get(url)
            picture = response.content
            # self.save(picture,file_name)
            with open(path + file_name, "wb") as f:
                f.write(picture)
            print("get picture %s" % file_name)
            file_num += 1

    def save(self, file, name):
        with open(path + name, "wb") as f:
            f.write(file)
        print("save picture %s" % name)

    def run(self):
        # if not os.path.exists(self.save_path):
        #     os.mkdir(self.save_path)
        # else:
        #     os.chdir(self.save_path)

        first_page = self.get_1stpage()
        # url_list = self.visit_page(first_page)
        # self.get_img(url_list)


if __name__ == '__main__':
    path = "C:/Users/BiaobiaoPeng/Desktop/python/projects/demoHTTP/images-jandan/"
    page = 3
    jandan = GetJandan(path, page)
    jandan.run()


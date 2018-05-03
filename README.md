短链接

主要分为两部分

- 生成短链接
- 短链接跳转

生成短链接

短链接的生成采用了发号的方式，通过向数据库插入新数据，将新数据的ID转换成64位编码。这样算下来，在短链接到达的6位的时候，能够承载的数据为64^6,为600多亿条数据

另外配合redis，将每条新数据都在redis中保存一段时间，这样避免了一些url的重复生成短链接。

另外实现了一些如访问数量限制，自定义title的功能

短链接跳转

通过对获取到的短链接代码进行解码，获取到id，然后从数据库中取到该id对应的链接，并返回302跳转





url接口

- shorturl
- - /shortUrl          
  - - Method : POST
    - Data:{'url':'','title':'','limit'}
    - 参数：url（必填，需要缩短的链接）,limit（访问限制）,title（自定义后缀）
    - 功能：对需要缩短的网址短链接的生成
    - 返回结果：缩短后的链接
  - /checkTitle
  - - Method : POST
    - Data:{'title':''}
    - 参数：title（需要检测的后缀）
    - 功能：检测自定义后缀是否可用
    - 返回结果：ok,error
- shortUrlJump
- - /*
  - - Method : GET
    - 功能：返回对应的地址

部署步骤

shorturl跟shortUrlJump可以在一个机器下面部署，也可以使用两台机器进行部署，因为我的短域名不能在国内备案，所以我的shortUrlJump是部署在了香港的阿里云机器，shorturl是部署在国内的机器上。

不管怎么部署，都要保证能够连接到同一台数据库



需要更改的参数

Converte/settings里面的数据库参数

shorturl/views里面的域名



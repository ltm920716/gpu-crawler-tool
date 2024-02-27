# 爬取云计算厂商GPU资源信息

### List

- [x] [latitude.sh](https://www.latitude.sh/accelerate/pricing)  
- [x] [paperspace](https://docs.paperspace.com/core/compute/machine-types/#gpu-machines) 
- [x] [vultr](https://www.vultr.com/pricing/#cloud-gpu)   
- [x] [ovhcloud](https://us.ovhcloud.com/public-cloud/prices/)
- [x] [vast.ai](https://cloud.vast.ai/)
- [x] [gcore](https://gcore.com/cloud/ai-gpu)
- [x] [lambdalabs](https://lambdalabs.com/service/gpu-cloud)
- [x] [tensordock](https://www.tensordock.com/pricing)
- [x] [fluidstack](https://www.fluidstack.io/pricing)
- [x] [runpod](https://www.runpod.io/gpu-instance/pricing)
- [x] [coreweave](https://www.coreweave.com/gpu-cloud-pricing)
- [x] [datacrunch](https://datacrunch.io/)
- [x] [jarvislabs](https://jarvislabs.ai/pricing/)
- [x] [tensordock](https://www.tensordock.com/pricing)
- [ ] [google](https://cloud.google.com/compute/gpus-pricing?hl=zh-cn)
- [ ] [run.ai](https://www.run.ai/)
- [ ] [Aliyun-ECS](https://ecs-buy.aliyun.com/ecs/)
- [ ] [Baidu]()
- [ ] [Tencent](https://buy.cloud.tencent.com/price/gpu)
- [ ] [Huoshan]()

### ModelItems
```
{
    "name": str = "别名"
    "gpu": str = "型号"
    "scale":  str = "规模"
    "gpu_ram": str = "显存"
    "vcpus": str
    "cpu_info": str
    "ram": str
    "storage": str
    "bandwidth": str
    "type": str = Optional["竞价", "常驻"]
    "regions": List[str] = ["可用地区"]
    "hour_price": str
    "month_price": str
    "year_price": str
    "is_available": bool
    "account": str = "可用数量"
    "os": str = Optional['windows', 'linux']
    "public_network": str    
    "private_network": str
```

### showcase
path: ```'./version1/show_extract/'```  


## pyspider
http://docs.pyspider.org/en/latest/Quickstart/

### Build env
```
# test with python=3.6
$ pip install -U pip 
$ pip install -r requirements_p.txt
```

### Mac 安装debug相关
- python>=3.6  
https://blog.csdn.net/q384264619/article/details/127248256
- pycurl  
  https://cscheng.info/2018/01/26/installing-pycurl-on-macos-high-sierra.html
- other  
  https://www.jianshu.com/p/deb496604b46?u_atoken=14f79dff-430f-459f-ab7f-e2b21220c5db
- [webui area small](https://github.com/binux/pyspider/issues/740#issuecomment-418808718)
- phantomjs is not enabled
  ```
  $ brew install phantomjs
  $ which phantomjs 
  $ spctl --add --label "PhantomJS" /opt/homebrew/bin/phantomjs
  $ brew reinstall phantomjs
  $ phantomjs --version
  ```
### Run
```
$ cd version1
$ pyspider -c config.json all
# edit and run on http://localhost:5001
``` 

### database
todo https://cloud.tencent.com/developer/article/1809106



## scrapy 
https://docs.scrapy.org/en/latest/  

### Build env
```
# test with python=3.6
$ pip install -U pip 
$ pip install -r requirements_s.txt
```

### Run
- 创建项目
```
$ scrapy startproject scrapy_version1
```
- 创建爬虫
```
$ cd scrapy_version1 
$ scrapy genspider latitude latitude.sh
# 完成parse()
```
- 运行爬虫
```
$ scrapy crawl latitude
# scrapy crawl latitude -o show_extract/latitude.json
# scrapy crawl latitude -o show_extract/latitude.csv
```
- 多爬虫运行  
todo
https://blog.csdn.net/xc_zhou/article/details/107452111
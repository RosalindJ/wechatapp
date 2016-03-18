Sample app to test the toolbar
==============================

A simple multi file app - to help get you started

1. Install all the requirements from: flask-mongoengine/requirements.txt::

    pip install -r requirements.txt

2. From the root folder run the app eg::

	python ./examples/biggerapp/app.py

3. Point your browser to localhost:4000/



爬虫计划及进度情况

1. 已完成新风系统的电商产品数据的抓取,包括名称,品牌,销量,价格,评价数据等,共计5000个.
2. 正在做数据分析工作,比如品牌数量,品牌销量,品牌的定价情况,客户关键字的提取,将这些提供web展示.
3. 计划抓取历史销售数据,以便能够更详细分析销售的变化情况.
    各大电商对爬虫程序的保护机制,如
        登录限制(文字识别码,图像识别码),
        速度限制, 重要数据的加载会很慢,期间也会让你输入验证码之类.
        次数限制, 连续多次访问也会触发保护机制.

4. 计划能够每个月或者每周提供一份市场分析数据的报告.
#_*_coding:utf-8_*_
import scrapy
import re


class testxpath(scrapy.Spider):
    name = 'spider1111111111111111111'#留作草稿,勿动
    start_urls=['http://sn.newssc.org/system/20170418/002159156.html']#http://sn.newssc.org/system/20170418/002159156.html
    # start_urls=['http://www.w3school.com.cn/example/xmle/books.xml']
    def parse3(self, response):

        def functionget(root1,tag):
            print 'in functionget'
            # print help(root1)
            strnode="\'"+tag+"\'"
            str3='%s'%tag

            # print strnode
            bdoy1='body'
            data_body=root1.xpath('div')
            data_yinhao=root1.xpath(strnode)
            print data_yinhao
            # print data_yinhao
            # data_yinhao2='%s'%tag
            # data_yuanlai=tag
            # data_yinghao22=root1.xpath(data_yinhao2)
            # data_yuanlai2=root1.xpath(data_yuanlai)
            # print data_yinghao22
            # print data_yuanlai2
            for childroot in data_yinhao:
                try:
                    print childroot.root.tag
                    functionget(childroot,childroot.root.tag)
                except Exception as e:
                    print e


            # xpathnext='%s'%(tag)
            # print xpathnext
            # functionresult2 = root1.Selector.xpath('head/child::node()')
            # functionresult= root1.xpath(xpathnext)
            # functionresult3=functionresult.xpath('/child::node()')
            #
            # for childroot in functionresult:
            #     try:
            #         print childroot.root.tag
            #         functionget(childroot,childroot.root.tag)
            #     except Exception as e:
            #         print e


        print 'in parse'
        xpathresult=response.xpath('/html/child::node()')
        print len(xpathresult)
        for i in xpathresult:
            try:
                print i
                print i.root.tag
                functionget(i,i.root.tag)
            except Exception as e:
                print e

    def parse2(self, response):
        i1s= response.xpath('/html/child::node()')
        for i1 in i1s:
            print i1##########################################说名结果是有的
            print i1.root.tag
            print i1.xpath('div')############################说明xpath('body')是有正常的结果的
            # print i1.xpath('')###################(child::node())也是没问题的
            # print len(i1)#就是看看长度
            print type(i1)#就是看看类型
            # for iii in i1:
            #     str1='head/child::node()'#################################循环遍历,selectorlist中的selector对象用什么方法也是没问题的.
            #     i11=iii.xpath(str1)#######################################卸载变量里边,反正学成xpath('head/child::node')上边已经证明了是没有问题的
            # # print i11.xpath('child::node()')
            # print i11
            print "______________qq______"

    def parse4(self,response):
        def childget(father):
            funcChildall=father.xpath('/child::node()')
            print funcChildall
            # if father==funcChildall.pop():
            #     return
            for child1 in funcChildall:
                if father==child1:
                    return
                else:
                    print child1.root.tag
                    childget(child1)

        i1 = response.xpath('/html/child::node()')
        for child in i1:
            print child.xpath('/child::node()')
            childget(child)

    def parse5(self, response):
        i1 = response.xpath('/html/child::node()')
        try:
            for j1 in i1:
                print 'in i1',j1
                print 'in j1',j1.root.tag
                try:
                    i2=j1.xpath('/html/%s/child::node()'%(j1.root.tag))
                    print 'in i2',i2
                except Exception as e:
                    print e
        except Exception as e:
            print e

    def parse(self, response):

        def getchild(fatherfunc,tagfunc,xpathfunc,numfunc):
            thischild=fatherfunc.xpath('%s[%d]/child::node()'%(xpathfunc,numfunc))
            print '%s[%d]/child::node()' % (xpathfunc, numfunc)
            # print fatherfunc.xpath('%s[%d]/text()'%(xpathfunc,numfunc)).extract()#显示对应的文档内容
            num=1
            # tag_decide_num=''
            tag_this_div={}#用一个字典来判断这个子标签div在所在的标签中出现了多少次好用来设置xpath路径
            for j2 in thischild:
                try:

                    tag= j2.root.tag
                    xpath='%s[%d]/%s'%(xpathfunc,numfunc,tag)

                    if tag not in tag_this_div.keys():#如果这个标签没出现过,记录它,num重置;否则,num+1
                        tag_this_div[tag]=1
                        num=1
                    else:
                        tag_this_div[tag]+=1
                        num=tag_this_div[tag]

                    # print xpath
                    # num+=1
                    getchild(j2,tag,xpath,num)
                    # print xpath

                except Exception as e:
                    # print e
                    pass



        i1=response.xpath('/child::node()')
        num=1
        tag_this_div = {}
        for j1 in i1:
            try:
                tag= j1.root.tag
                xpath='/'+tag
                if tag not in tag_this_div.keys():  # 如果这个标签没出现过,记录它,num重置;否则,num+1
                    tag_this_div[tag] = 1
                    num = 1
                else:
                    tag_this_div[tag] += 1
                    num = tag_this_div[tag]
                # num=num
                print xpath
                getchild(fatherfunc=j1,tagfunc=tag,xpathfunc=xpath,numfunc=num)


                num+=1
                # print xpath
            except Exception as e:
                pass

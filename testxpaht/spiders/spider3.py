#_*_coding:utf-8_*_
import scrapy
import re
import pickle
from testxpaht import myPageStucture




class testxpath(scrapy.Spider):
    name = 'spider'
    start_urls=['http://sn.newssc.org/system/20170418/002159156.html']#http://sn.newssc.org/system/20170418/002159156.html
    # start_urls=['http://www.w3school.com.cn/example/xmle/books.xml']
    def parse3(self, response):

        def functionget(root1,tag):
            print 'in functionget'
            # print help(root1)
            strnode="\'"+tag+"\'"
            str3='%s'%tag
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
            print "___________________________________qq_______________________________________"

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
                    #删除:body > div:nth-child(9) > table > tbody > tr > td:nth-child(3) > div > table > tbody > tr:nth-child(1) > td > div > table:nth-child(3) > tbody > tr > td > p > table > tbody > tr:nth-child(1) > td.new14 > a

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
        thisclass=myPageStucture.pageStructure()
        def getchild(fatherfunc,tagfunc,xpathfunc,numfunc,fatherstructure_class):

            thisclass2=myPageStucture.pageStructure()

            thischild=fatherfunc.xpath('%s[%d]/child::node()'%(xpathfunc,numfunc))
            print '%s[%d]/child::node()' % (xpathfunc, numfunc)
            # print ' ----------------------------text--begin-----------------------------------'
            # for icontent in fatherfunc.xpath('%s[%d]/text()' % (xpathfunc, numfunc)).extract():
            #     print icontent
            # print '        -----------------------text--end--------------------'
            num=1
            tag_this_div={}#用一个字典来判断这个子标签div在所在的标签中出现了多少次好用来设置xpath路径
            div_number=1
            for j2 in thischild:
                try:
                    tag= j2.root.tag
                    xpath='%s[%d]/%s'%(xpathfunc,numfunc,tag)
                    if tag not in tag_this_div.keys():#如果这个标签没出现过,记录它,num重置;否则,num+1
                        tag_this_div[tag]=1
                        num=1#后来发现其实不要这个num也是可以没有的，后边直接传入tag_this_div[tag]
                    else:
                        tag_this_div[tag]+=1
                        num=tag_this_div[tag]

                    thisclass2.name=tag
                    thisclass2.content=fatherfunc.xpath('%s[%d]/text()' % (xpathfunc, numfunc)).extract()#传过来就已经是子标签,所以这里处理一下num就行
                    thisclass2.num=num
                    thisclass2.xpath=xpath
                    thisclass.divnum=div_number
                    fatherstructure_class.child[tag+str(num)]=thisclass2#这里的tag貌似没有添加下标，可能会出错。#7-6对头,今天发现了tag没有下表,出错了
                    has_url= fatherfunc.xpath('%s[%d]/@href'%(xpathfunc,numfunc))
                    if has_url:
                        thisclass2.has_url=1


                    div_number+=1#这个div_number代表是的当前子节点下所有的子标签数量，前边的num表示的同一个标签的的出现次数
                    getchild(j2,tag,xpath,num,thisclass2)
                except Exception as e:
                    print e
        i1=response.xpath('/child::node()')
        num=1
        tag_this_div = {}
        div_number=1
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

                #所有信息提取完成

                thisclass.name=tag
                thisclass.content=j1.xpath('/%s/text()'%tag)
                thisclass.xpath=xpath
                thisclass.num=num
                thisclass.divnum=div_number
                #thisclass需要获得5个标签,这里4个,下边在子节点中再获得它所有的child
                print xpath
                getchild(fatherfunc=j1,tagfunc=tag,xpathfunc=xpath,numfunc=num,fatherstructure_class=thisclass)
                div_number+=1
            except Exception as e:
                pass

        print thisclass
        p1=pickle.dumps(thisclass,-1)
        file2='/home/passager/Desktop/xpath/xpath.pkl'
        with open(file2,'w+') as fl:
            fl.write(p1)
        pass

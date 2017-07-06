#_*_coding:utf-8_*_
import re
class pageStructure:
    def __init__(self):
        self.name=None
        self.num=1
        self.xpath=None
        self.content=None#为标签的文本内容,很多时候这个extract之后是一个列表.
        self.TL=0#文本长度
        self.PN=0#标点符号数量
        self.ND=None#这个其实没用,表示两个节点间的相对距离,一个节点没什么用,它针对的是两个节点
        self.TDTN=0#计集合元素在文本中出现的次数(比如一些特殊符号:可用作时间,@可用作邮箱)
        self.TAL=0#文本中字符的长度
        self.TP=None#表示节点的属性,如div,tr,td等,与那么属性重合
        self.NTP=None#表节点与标题之间的关系,在\其之上为'U',在其之下为'D'


        self.child={}#用来表示自己的子节点,每一个子节点都是一个pagestructure
        self.divnum=1#用来表示这个标签在网页父标签中的顺序.可以用来计算ND


    def Init(self):
        self.TAl=len(self.content)
        # content_no_Symbol=self.content.replace(u'，','').replace(u'。','').replace(u'“','').replace(u'-','').replace(u'"')#没有处理中文符号，暂时先这样
        # self.TL=len(content_no_Symbol)

        Re_find_PN=re.compile(r'[\,\.\'\"\;\。——\-\，\”\“\！\《\》\!\<\>\{\}\<\>]')
        PN_list=Re_find_PN.findall(self.content)
        self.PN=len(PN_list),self.content

        content_no_Symbol=Re_find_PN.sub('',self.content)
        self.TL=len(content_no_Symbol)
        self.TAl=len(self.content)
        print content_no_Symbol,len(content_no_Symbol)
        print len(self.content)
        self.TP=self.name+'['+str(self.num)+']'

    def putin(self,pageStructure):
        if pageStructure.name ==None:
            print 'Wrong Type'

        self.child[pageStructure.name]=pageStructure
        return self

if __name__ == '__main__':
    thisclass=pageStructure()
    thisclass.content='你好啊！《某个电影》，这里的文本做测试用“当然这里也是--这里还是”,of course this also be'
    thisclass.name='div'
    thisclass.num=1
    thisclass.Init()
    print thisclass.content

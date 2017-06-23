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
        self.ND=None#这个其实没用,表示两个节点间的相对距离,一个节点没什么用,它针对的是连个节点
        self.TDTN=0#计集合元素在文本中出现的次数(比如一些特殊符号:可用作时间,@可用作邮箱)
        self.TAL=0#文本中字符的长度
        self.TP=None#表示节点的属性,如div,tr,td等,与那么属性重合
        self.NTP=None#表节点与标题之间的关系,在\其之上为'U',在其之下为'D'


        self.child={}#用来表示自己的子节点,每一个子节点都是一个pagestructure
        self.divnum=1#用来表示这个标签在网页父标签中的顺序.可以用来计算ND


    def Init(self):
        self.TAl=len(self.content)
        content_no_Symbol=self.content.replace(u',','').replace(u'.','').replace(u'"','').replace('-','')#没有处理中文符号

        self.PN=len(content_no_Symbol)

    def putin(self,pageStructure):
        if pageStructure.name ==None:
            print 'Wrong Type'

        self.child[pageStructure.name]=pageStructure
        return self

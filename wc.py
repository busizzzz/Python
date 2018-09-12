#coding=utf8
#argparse模块，用于处理命令行参数
import argparse
parser = argparse.ArgumentParser(description="wc.exe")            
parser.add_argument("-c", 
                     dest="Chars",
                     help="count chars")  
parser.add_argument("-w", 
                     dest="Words",
                     help="count words") 
parser.add_argument("-l", 
                     dest="Lines",
                     help="count lines")                                                                                    
args = parser.parse_args() 

i=0#全局变量，用于判断该返回哪个数
def get_Count(args):#用于计算出字符数、单词数和行数
    global i
    if i==1:
        chars=0
        with open(args,'r')as f:
            data = f.read()
            chars = len(data)
        return chars#返回字符数
    if i==2:
        words=0
        with open(args,'r')as f:
            data = f.read()
            words = len(data.split())
        return words#返回单词数
    if i==3:
        lines=0
        with open(args,'r')as f:
            for Lines in f:
                lines+=1
        return lines#返回行数
def main():#用于调用get_Count函数和输出结果
    global i
    if args.Chars:
        i=1
        c=get_Count(args.Chars)
        print('文本的字符数：',c)
    if args.Words:
        i=2
        w=get_Count(args.Words)
        print('文本的词数：',w)
    if args.Lines:
        i=3
        l=get_Count(args.Lines)
        print('文本的行数：',l)
if __name__ == '__main__':
    main()
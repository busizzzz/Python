#coding=utf8
#argparse模块，用于处理命令行参数
import argparse
parser = argparse.ArgumentParser(description="wc.exe")            
parser.add_argument("-c", "--chars",
                     dest="chars",
                     help="count chars")  
parser.add_argument("-w", "--words",
                     dest="words",
                     help="count words") 
parser.add_argument("-l", "--lines",
                     dest="lines",
                     help="count lines")                                                                                    
args = parser.parse_args()   

def get_Count(data):#
    chars = len(data)
    words = len(data.split())
    lines = data.count('\n')
    return lines, words, chars

def count_chars(args):
    chars=0
    with open(args,'r')as f:
        data = f.read()
        for line in f:
            chars=get_Count(args)
    return chars    
        
def count_lines(args):
    lines=0
    with open(args,'r')as f:
        data = f.read()
        for line in f:
            lines=get_Count(args)       
    return lines 

def count_words(args):
    words=0
    with open(args,'r')as f:
        data = f.read()
        for line in f:
            words=get_Count(args)       
    return words 

if args.chars:  
	l=count_chars(args.chars)
	print('字符数：',l)
if args.words:   
	w=count_lines(args.words)
	print('词数：',w)
if args.lines:   
	c=count_words(args.lines)
	print('行数：',c)
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

def get_Count(data):
    chars = len(data)
    words = len(data.split())
    lines = data.count('\n')
    if args.chars:
        return chars
    if args.words:
        return words
    if args.lines:
         return lines

def count_chars(args):
    chars=0
    with open(args,'r')as f:
        data = f.read()
        chars=get_Count(data)
    return chars    
        
def count_lines(args):
    lines=0
    with open(args,'r')as f:
        data = f.read()
        lines=get_Count(data)       
    return lines 

def count_words(args):
    words=0
    with open(args,'r')as f:
        data = f.read()
        words=get_Count(data)       
    return words 

if args.chars:  
	c=count_chars(args.chars)
	print('文本的字符数：',c)
if args.words:   
	w=count_words(args.words)
	print('文本的词数：',w)
if args.lines:   
	l=count_lines(args.lines)
	print('文本的行数：',l)
#coding=utf8
#argparse模块，用于处理命令行参数
import argparse
parser = argparse.ArgumentParser(description="wc.exe")            
parser.add_argument("-c", "--chars",
                     dest="chars",
                     action="store_true",
                     help="count chars")  
parser.add_argument("-w", "--words",
                     dest="words",
                     action="store_true",
                     help="count words") 
parser.add_argument("-l", "--lines",
                     dest="lines",
                     action="store_true",
                     help="count lines")                                                                                    
args = parser.parse_args()   

def get_Count(data):
    chars = len(data)
    words = len(data.split())
    lines = data.count('\n')
    return lines, words, chars

def count_chars(args):
    c=0
    with open(args.chars,'r')as f:
        for line in f:
            c=get_Count(args)
    return c    
        
def count_lines(args):
    l=0
    with open(args.lines,'r')as f:
        for line in f:
            l=get_Count(args)       
    return l 

def count_word(args):
    w=0
    with open(args.lines,'r')as f:
        for line in f:
            w=get_Count(args)       
    return w 


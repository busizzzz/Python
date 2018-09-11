#argparse模块，用于处理命令行参数
import argparse
parser = argparse.ArgumentParser(description="wc.exe")            
parser.add_argument("-c", "--char",
                     dest="chars",
                     action="store_true",
                     default=False,
                     help="count chars")  
parser.add_argument("-w", "--word",
                     dest="words",
                     action="store_true",
                     default=False,
                     help="count words") 
parser.add_argument("-l", "--line",
                     dest="lines",
                     action="store_true",
                     default=False,
                     help="count lines")                                                                                    
args = parser.parse_args()   
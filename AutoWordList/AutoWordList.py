#coding=utf-8
import requests as req
from bs4 import BeautifulSoup
from collections import Counter
from googlesearch import search
import argparse


def google():
    site_list = []
    for j in search(query, tld="co.in", num=sites, stop=sites, pause=2):
        site_list.append(j)
    return site_list
def progressBar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '=', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iterable    - Required  : iterable object (Iterable)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    total = len(iterable)
    # Progress Bar Printing Function
    def printProgressBar (iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Initial Call
    printProgressBar(0)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    # Print New Line on Complete
    print()
# Create the parser
my_parser = argparse.ArgumentParser(prog='AutoWordList.py',
                                    description='Create a targeted wordlist for bruteforcing',
                                    epilog='AutoWordList uses Google to create a "smart" wordlist that can help speed up bruteforcing. The generated list is designed to be used in conjuction with a standard wordlist to create an effective Combinator attack with Hashcat. AutoWordList searches Google for the inputted words, scrapes the top websites that come up, and creates a wordlist using the most common words found on each site.')

# Add the arguments
my_parser.add_argument('-s',
                       metavar='# of sites',
                       dest='sites',
                       help='number of websites to search [10]',
                       action='store',
                       nargs='?',
                       default=10,
                       type=int)
my_parser.add_argument('-d',
                       metavar='search depth',
                       dest='depth',
                       help='number of words to grab per website [4]',
                       action='store',
                       nargs='?',
                       default=4,
                       type=int)
my_parser.add_argument('keyw',
                       metavar='keywords',
                       nargs='*',
                       type=str,
                       help='the words to build the wordlist around')


# Execute the parse_args() method
args = my_parser.parse_args()

query = ' '.join(str(e) for e in args.keyw)
search_depth = args.depth
sites = args.sites
if len(query) != 0:


    print("search term:",query,"\n# of sites:",sites,"\nwords/site:",search_depth)
    common_words = ['said','was','are','&','is','the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us']
    special_characters = ["–","!","\"","@","(",")","#","$","%","^","-"," ","+","?","_","=",",","<",">","/","."," ",":","•","|"]
    out_words = []
    out_word_nodup = []



    site_list = google()
    
    for i in progressBar(site_list, prefix = 'Progress:', suffix = 'Complete', length = 50):

        resp = req.get(i)
        soup = BeautifulSoup(resp.text, 'html.parser')
        # get text
        text = soup.get_text()
        for x in common_words:
            text = text.replace(" "+x+" "," ")
            text = text.replace("."+x+" "," ")
        for x in special_characters:
            text = text.replace(x,"")
            
        
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        # split() returns list of all the words in the string
        split_it = text.split()
          
        # Pass the split_it list to instance of Counter class.
        CounterVar = Counter(split_it)
          
        # most_common() produces k frequently encountered
        # input values and their respective counts.
        most_occur = CounterVar.most_common(search_depth)
    
    #        print(most_occur)
        for p in most_occur:
            cur_word = p
            out_words.append(cur_word[0].lower())
    
         
    out_words = list(dict.fromkeys(out_words))
    #print(out_words)
    for i in out_words:
        if i not in out_word_nodup:
            out_word_nodup.append(i)
            
    out_word_nodup.sort()
    for i in out_word_nodup:
        print(i)
else:
    print("No keyword was entered.") 
            





        

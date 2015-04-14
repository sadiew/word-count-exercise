import string
import sys
from collections import Counter
#from sys import argv

def count_words():
    word_dict = {}
    filename = str(sys.argv[1])
    with open(filename) as source_file:
        for line in source_file:
            for c in string.punctuation:
                if c != "'":
                    line = line.replace(c, '')
            
            line = (line.rstrip().lower().split(' '))
            for word in line:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1

    for word, word_count in word_dict.iteritems():
        print "%s %r" % (word, word_count)

#count_words()

def count_words_by_counter():
    word_list = []
    filename = str(sys.argv[1])
    with open(filename) as source_file:
        for line in source_file:
            for c in string.punctuation:
                if c != "'":
                    line = line.replace(c, '')
            
            line = (line.rstrip().lower().split(' '))
            word_list.extend(line)

    word_counter = Counter(word_list)
        
    for word, word_count in sorted(word_counter.iteritems()):
        print "%s %r" % (word, word_count)


#count_words_by_counter()

def count_words_sort_frequency():
    word_list = []
    filename = str(sys.argv[1])
    with open(filename) as source_file:
        for line in source_file:
            for c in string.punctuation:
                if c != "'":
                    line = line.replace(c, '')
            
            line = (line.rstrip().lower().split(' '))
            word_list.extend(line)

    word_counter = Counter(word_list)

    for word in sorted(word_counter, key=word_counter.get, reverse=True):
        print "%s %r" % (word, word_counter[word])

#count_words_sort_frequency()

def count_words_sort_freq_alpha():
    word_list = []
    filename = str(sys.argv[1])
    with open(filename) as source_file:
        for line in source_file:
            for c in string.punctuation:
                if c != "'":
                    line = line.replace(c, '')
            
            line = (line.rstrip().lower().split(' '))
            word_list.extend(line)

    word_counter = Counter(word_list)

    dict_with_lists = {}
    for count in word_counter.values():
        dict_with_lists[count] = []

    for word in word_counter:
        dict_with_lists[word_counter[word]].append(word)
    
    for frequency in dict_with_lists:
        dict_with_lists[frequency].sort()

    for frequency in reversed(sorted(dict_with_lists)):
        for word in dict_with_lists[frequency]:
            print '%s %r' % (word, frequency)

count_words_sort_freq_alpha()

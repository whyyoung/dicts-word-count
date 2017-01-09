# # put your code here.
# #text_file = open("test.txt")
# #word_count = {}

# #for each_line in text_file:
#     each_line = each_line.rstrip()
#     words = each_line.split(' ')

#     for each_word in words:
#         word_count[each_word] = word_count.get(each_word, 0) + 1

# for word, w_count in word_count.items():
#     print "%s: %d" %(word, w_count)




def build_dictionary(filename):
    text_file = open(filename)
    word_count = {}

    for each_line in text_file:
        #each_line = each_line.strip("\.,%#^*--;:")
        #each_line = each_line.lstrip("\.,%#^*--;:")
        words = each_line.split()

        for each_word in words:
            each_word = each_word.strip("\.,%#^*--;:?!" '"')
            #each_word = each_word.lstrip("\.,%#^*--;:")
            word_count[each_word] = word_count.get(each_word, 0) + 1

    display_word_count(word_count)

def display_word_count(dict1):
    for word, w_count in dict1.iteritems():
        print "%s: %d" %(word, w_count)

build_dictionary("twain.txt")

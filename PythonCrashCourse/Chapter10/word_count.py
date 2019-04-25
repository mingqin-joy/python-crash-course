def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
       # msg = "Sorry, the file " + filename + " does not exist."
       # print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


filename = 'C:/Users/MingqinZhou/Desktop/alice.txt'
count_words(filename)


filename2 = ['C:/Users/MingqinZhou/Desktop/alice.txt', 'C:/Users/MingqinZhou/Desktop/siddhartha.txt',
             'C:/Users/MingqinZhou/Desktop/moby_dick.txt', 'C:/Users/MingqinZhou/Desktop/little_women.txt']
for filename in filename2:
    count_words(filename)

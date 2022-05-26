with open("ex/textfull.txt") as f:
    count_ruby = f.read().count("《");
    print(count_ruby)
    #108
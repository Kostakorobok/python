def count_words(filename):
    try:
        with open(filename, encoding = "utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"File {filename} doesn't exist.")
        pass
    else:
        # count the approximate number of words in the file
        words = contents.split()
        num_words = len(words)
        print(f"There are {num_words} in the document {filename}")

file_name1 = "text_files/alice.txt"
file_name2 = "text_files/siddhartha.txt"
file_name3 = "text_files/moby_dikk.txt"
file_name4 = "text_files/little_women.txt"

file_names = [file_name1, file_name2, file_name3, file_name4]

for i in file_names:
    count_words(i)

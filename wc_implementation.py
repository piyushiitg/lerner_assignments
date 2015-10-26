"""
Word count
 
 Unix systems contain many utility functions. One of the most useful to me (in my writing) is wc, the "word count" program. If you run wc against a text file, it'll count the characters, words, and lines that the file contains.
  
  The challenge for this exercise is to write a version of wc in Python. However, your version of wc will return four different types of information about the files:
   
   Number of characters (including whitespace)
   Number of words (separated by whitespace)
   Number of lines
   Number of unique words
   The program should ask the user for the name of an input file, and then produce output for that file.
>>>>python wc_implementation.py test-file.txt
Number of characters (including whitespace):  165
Number of words (separated by whitespace):  28
Number of lines:  11
number_of_unique_words 20

>>>>python wc_implementation.py t1.txt
Number of characters (including whitespace):  54
Number of words (separated by whitespace):  15
Number of lines:  11
number_of_unique_words 12

"""

def wc_implementation(file_name):
    f = open(file_name, "r")
    lines = f.readlines()
    no_of_char_with_space = 0
    no_of_words = 0
    number_of_lines = len(lines)
    number_of_unique_words = 0
    words = []
    f.close()
    for line in lines:
        no_of_char_with_space = no_of_char_with_space + len(line)
        words.extend(line.split())
        no_of_words = no_of_words + len(line.split())
    print "Number of characters (including whitespace): ", no_of_char_with_space
    print "Number of words (separated by whitespace): ", no_of_words
    print "Number of lines: ", number_of_lines
    print "number_of_unique_words", len(set(words))
 

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
         print "File name is not prsent"
    file_name = sys.argv[1]
    wc_implementation(file_name)

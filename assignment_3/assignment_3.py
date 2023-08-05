""" Assignment 3: File Handling (python)
Write a Python program that reads a text file named "input.txt" and performs the following tasks:
1.	Count the number of lines in the file.
2.	Count the number of words in the file.
3.	Count the number of occurrences of a specific word entered by the user.
4.	Create a new file named "output.txt" and write the contents of "input.txt" in reverse order """

class FileHandlerUtility:
    def __init__(self, file_path) -> None:
        self.file_path = file_path

    # 1. Count the number of lines in the file.
    def cnt_lines(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()

        total_lines = len(lines)
        return {'count_of_lines': total_lines}

    # 2. Count the number of words in the file.
    def cnt_words(self):
        with open(self.file_path, 'r') as file:
            words = file.read()
        words = words.split()
        return {'count_of_words': len(words)}

    # 3. Count the number of occurrences of a specific word entered by the user.
    def cnt_words_occ(self):
        with open(self.file_path, 'r') as file:
            words = file.read()
        file_contents = words.split()    
        """Take user input & search the occu. of the specific word"""
        user_search = input('Please enter the word you want to search: ')
       
        total_word_count = 0
        for word in file_contents:
            if word.lower() == user_search.lower():
                total_word_count +=1
        if total_word_count>0:
            return {'total_word_count': total_word_count}
        return {"The word you searched for doesn't exist"}

    #4. Create a new file named "output.txt" and write the contents of "input.txt" in reverse order
    def read_reverse(self):
        with open(self.file_path, 'r') as file:
            words = file.read()
        reverse_order  = words[::-1]
        
        #creating `output.txt` file and writing th reversed order word.
        with open('output.txt', 'w') as file:
            file.write(reverse_order)
        return {'status': 1, 'message': 'file created and data stored successfully.'}

file_obj = FileHandlerUtility(r'<Your filepath here.>')
print(file_obj.cnt_lines())
print(file_obj.cnt_words())
print(file_obj.cnt_words_occ())
print(file_obj.read_reverse())
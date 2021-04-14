lang_list = ["C", "python", "javascript", 50, "java", "swift", "kotlin", "react", "react-ntaive"]
human_lang = ["Bangladesh", "Arabic", "English", "Mandarin" ,"urdu" , "hindi"]

number_of_elements = len(lang_list) # number of elements in list
lang_list[8] = "mongodb" #change item value
lang_list.insert(2, "threejs") #Insert Items
lang_list[3:4] = ["nodejs", "C+"] #Change a Range of Item Values
lang_list.append("C++") # append use for add new item
lang_list.extend(human_lang) #To append elements from another list to the current list, use the extend() method.
lang_list.remove("java") # remove use for remove items
lang_list.pop() # remove last item
lang_list.pop(0) #Remove Specified Index
# del lang_list # Delete the entire list
#lang_list.clear() # Clear the list content
new_list = lang_list.copy() # Make a copy of a list with the copy() method



print("new list: ", new_list)
print("human language list :", human_lang)
print("language list: ", lang_list)






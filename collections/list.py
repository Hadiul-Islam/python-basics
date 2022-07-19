# Lists are used to store multiple items in a single variable.(in other programming languages, they are called array)

# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets:

# list with 10 emogis
my_list  = ['🎁', '🎂', '🎃', '🎄', '🎅', '🎆', '🎇', '🎈', '🎉', '🎊']
my_team = ['John', 'Jane', 'Jack', 'Jill']
#list with list() constructor 
my_num = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
my_nums = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#access elemsent in list
print(my_list[0])
#length of list
print(len(my_list))
#type of list
print(type(my_team))
#change element in list
my_num[0] = 100
print(my_num)
my_team[1:3] = ['Tom', 'Jerry']
print(my_team)
#insert element in list
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index:
my_team.insert(1, 'Bom')
print(my_team)
#add element in list
my_team.append('Jerry')
print(my_team)
#remove element in list
my_team.remove('Jerry')
print(my_team)
#sort list
my_team.sort()
print(my_team)
#reverse list
my_team.reverse()
print(my_team)
#pop element in list
my_team.pop()
print(my_team)
#clear list
# my_team.clear()
# print(my_team)
#copy list
my_team_copy = my_team.copy()
print(my_team_copy)
#sum of list
print(sum(my_nums))


#loop in list
for i in my_team:
    print(i+' '+str(my_team.index(i)))





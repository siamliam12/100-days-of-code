# # Exercise: Array DataStructure

# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190

# Create a list to store these monthly expenses and using that find out,

#     1. In Feb, how many dollars you spent extra compare to January?
#     2. Find out your total expense in first quarter (first three months) of the year.
#     3. Find out if you spent exactly 2000 dollars in any month
#     4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
#     5. You returned an item that you bought in a month of April and
#     got a refund of 200$. Make a correction to your monthly expense list
#     based on this

expenses = [2200,2350,2600,2130,2190]
print(f"In Feb,you spent extra {expenses[1]-expenses[0]} compare to January?")
expense = 0
for i in range(0,3):
    expense += expenses[i]
print(f"your total expense in first quarter (first three months) of the year is {expense}")
for expense in expenses:
    if expense == 2000:
        print("you spent exactly 2000 dollars in any month")
expenses.append(1980)
print("Expenses at the end of June:",expenses)
expenses[3] = expenses[3] - 200
print("Expenses after 200$ return in April:",expenses)
# [Solution](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/Solution/1_expenses.py)

# 2. You have a list of your favourite marvel super heros.
# ```
# heros=['spider man','thor','hulk','iron man','captain america']
# ```

# Using this find out,

#     1. Length of the list
#     2. Add 'black panther' at the end of this list
#     3. You realize that you need to add 'black panther' after 'hulk',
#        so remove it from the list first and then add it after 'hulk'
#     4. Now you don't like thor and hulk because they get angry easily :)
#        So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#        Do that with one line of code.
#     5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

heros=['spider man','thor','hulk','iron man','captain america']
length = len(heros)
print(length)
heros.append('black panther')
print(heros)
# 3. You realize that you need to add 'black panther' after 'hulk',
# so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3]=['doctor strange']
print(heros)
# 5. Sort the list in alphabetical order
heros.sort()
print(heros)
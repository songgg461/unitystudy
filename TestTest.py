we = {'Kim', 'lee', 'park', 'choi', 'jung', 'kang', 'jo', 'yoon', 'jang', 'lim'}
late = {'yoon', 'park'}
abs = {'jung', 'yoon', 'park', 'lim'}
good = we.difference(late).intersection(we.difference(abs)) 
bad = we.intersection(late).intersection(we.intersection(abs))

print("the whole employee : ", end =''); print(we)
print("late : ", end =''); print(late)
print("absence : ", end =''); print(abs)
print("The list of the employees that get bonus : ", end =''); print(good)
print("The list of the employees that must work overtime : ", end =''); print(bad)

new = input("Enter the new employees : ")
newlist = set(new.split())
total = we.union(newlist)
if newlist.issubset(we) :
 print("the names of the new and existing employees is same.")
 print("The list of entire employees : ", end =''); print(total)
else :
 print("The list of entire employees : ", end =''); print(total)




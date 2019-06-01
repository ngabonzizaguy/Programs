from __future__ import print_function


# i = 1

# def foo():
# 	i = 5
# 	print(i,'in foo()')
# print(i,'global')
# foo()


# #func to take user input and assigns it to the nested func
# def user_input(user_age):
# 	user_age = input('what is your age: ')
	
# 	def triggerer_func(user_func,user_age):
# 	    user_func(user_func(user_age))
        
# 	triggerer_func(user_input,user_age)
	


# def add(x,y):
# 	return x+y
# 	def do_twice(add_func,x,y):
# 		return add_func(add_func(x,y), add_func(x,y))

# 	a = 5
# 	b = 10
	
# 	print(do_twice(add,a,b))



# x = 50

# def func():
# 	global x
# 	print('this function is now using the global x!')
# 	print('Because of global x is:',x)
# 	x = 2
# 	print('Ran func(), change global x to:',x)

# print('Before calling func(), x is:',x)
# func()
# print('value of x (outside of func()) is:',x)


# name = 'this is a global variable'

# def greet():
# 	#enclosing function
# 	name = 'samy'
# 	def hello_there():
# 		print('hello', name)
# 	hello_there()
# greet()
# print(name)



# counts = dict()
# for line in handle:
# 	words = line.split()
# 	for word in words:
# 		counts[word] = counts.get(word, 0) + 1

# bigcount = None
# bigword = None
# for word, count in list(counts.items()):
# 	if bigcount is None or count > bigcount:
# 		bigword = word
# 		bigcount = count

# print(bigword, bigcount)
"""
python functions
def function_name(parameters):
statement(s)"""

#creating a function
#calling a function
#Arguments, Number of Arguments
#Returns, value
#default parameter value

#creating a function
def add():
 a = 10
 b = 20
 c = a + b
 print(c)

#calling a function
add()


#Arguments, Number of Arguments
def add_arg(a,b):
  c = a + b
  print(c)
add_arg(2,6)
add_arg(1000, 5000)


#Returns, value
def add_arg_retu(a,b):
  c = a + b
  return c
result = add_arg_retu(2,4)
print(result)


#default parameter value
def add_arg_retu(a =0, b =1):
  c = a + b
  return c
result = add_arg_retu()
print(result)

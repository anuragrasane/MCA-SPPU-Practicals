#2.1. Write a Python program to understand the data types of Python.
#Numeric Datatype(integer,float,complex number)
#Numeric Datatypes
print("Numeric Datatypes")
x_int=10;
x_float=30.3
x_complex_number=4+3j
print("Value of x_int=",x_int,"Datatype of x_int",type(x_int))
print("Value of x_float=",x_float,"Datatype of x_float",type(x_float))
print("Value of x_complex_number=",x_int,"Datatype of x_complex_number",type(x_complex_number))
#Sequence Datatype: (String,List,Tuple)
#Sequence Datatype
print('Sequence Datatype: (String,List,Tuple)')
var_str='Python Class'
var_list=[10,20,30,'python',30.6,10+4j]
var_tuple=(10,30,50,20.3,11-3j,'Hello')
print('value of var_str =',var_str,'Datatype of var_str',type(var_str))
print('value of var_list =',var_list,'Datatype of var_list',type(var_list))
print('value of var_tuple =',var_tuple,'Datatype of var_tuple',type(var_tuple))
#Dictionary Datatype
print('Dictionary Datatype')
var_dict={1:'python',2:'java',3:'php',4:'C++'}
print('Value of var_dict=',var_dict,'Datatype of var_dict =',type(var_dict))
#Set Datatype
print('Set Datatype')
var_set = set(['Python','For','Python',20,30,40,30+4j,30.6])
print('Value of var_set=',var_set,'Datatype of var_set =',type(var_set))
#Boolean Datatype
print('Boolean Datatype')
var_bool= False
print('Value of var_bool =',var_bool,'Datatype of var_bool =',type(var_bool))

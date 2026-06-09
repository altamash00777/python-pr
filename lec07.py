# comments are part of sorce code which
# do not contribute in execution of program

# /////////////////////////////////////////////////////////////
# langchain
# langgraph
# langflow
# langsmith


# langchain->help in building blocks 

# langgraph->we built connection or workflow

# langflow->tools using which we can connect different agents from another agents
#           such that agent1 output work for agent2 input

# langsmith->use for monitoring and debugging the error

# agentA--------------------agentB
#              error
#              /\
#             /\/
#            /\/
#           /\/
#          /\/
#       langsmith 

# CGI-computer graphics interface-->used in vfx industries
# -----------------------------------
# AGI-artificial general interface->similar to human intelligence ->
# -can learn by itself,can evolve like humans
# -research is ongoing

# core is common 


# print("""this is triple double quotes in python""")
# print('''this is triple single quotes in python''')
# print("this is single code")

# but there is difference in them when we write in multiple line

# for multilines there we not use double quotes
# double and single quotes can only execute single lines
# use \ for multilines

# """ """ ->use triple double quotes to execute multiline comments
# print("""once there was someone for\ 
# you waiting , then you realize it will be a false opinion\
#       """)

# in triple double quotes every enter is newline

# we have three types of string
# ->single quotes
# ->double quotes
# ->triple quotes

# if use same same comnination it will generate error

# print("hello world this is me "Altamash" ")->this shows error
# print('hello its me 'altamash'')->this will also generate error

# print("rohan ")


# interview
# double ke ander double
# triple single ke ander triple single

# doc string -> also called documentation string
# triple quotes real usecase in python real example
# 1-> to write multi line string in python
# 2->to write multi line comment -> but not recommended
# 3->to write docstring in python.(documentation string)


# this triple quotes showing useful info about add function

def add(a,b):
    '''
    this is function addition of two number
    @author altamash
    @param a:first num
    @param b:second num
    
    '''
    return a+b

# print(add(3,4))

print(add.__doc__)
# (add.__doc__)->this will print info inside triple comment
# doc -> document -> documentation string

# IO statements
# use for input and output

# input can be zero but output can never be zero
# computer standard input->keyboard
# output->monitor

# addition of two numbers
# we enter number and thats the value

# 2 power n -> n can be 1,2,3,4,5
# n is number of input
# if n=0 -> 2 power 0 -> 1
# there still output without input





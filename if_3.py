#execute block of statements if compound/multiple conditions satisfies

# I will be having two conditions and I will combine those conditions using logical operators(and, or)

a = 10
b = 15
c = 5
#a>b as well as a>c 

if a>b and a>c:
    print "a is greater"
if b>a and b>c:
    print "b is greater"
if c>a and c>b:
    print "c is greater"

#multiple alternatives
# elif 
if a>b and a>c:
    print "a is greater"
elif b>c:
    print "b is greater"
else:
    print "c is greater"

# it is mandatory to use else always
#find out the largest number among 4 values
#find out the largest number among 4 values if any two values are equal then print "not eligible for finding greater value"
#WAP to assign age to a variable
# if age is below 5 then print kid on the console
# if age is below 13 then print teen on the console
# if age is above 13 then print younger on the console
# if age is above 40 then print experienced on the console
# if age is above 60 then print senior citizen on the console

#WAP to assign age and gender to variables
# if age is greater than 18 as well as gender is male, then print he is eligible to drink
# if age is greater than 21 as well as gender is male, then print he is eligible to drink as well as to get married
# if age is greater than 18 as well as gender is female, then print he is eligible to drink as well as to get married

#WAP to assign age to a variable
# if age is below 13 then print "doesn't know anything about life"
# if age is above 13 then print "enjoying the life"
# if age is above 21 then print "difficulties has been started"
# if age is above 30 then print "habituated to difficulties"
# if age is above 60 then print "sharing his life story"
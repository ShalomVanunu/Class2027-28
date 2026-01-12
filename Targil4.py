Text = """
The division has created a two-speed path out of the pandemic led by
states that have suffered the greatest toll, frustrating the federal
government&#39;s efforts to reopen the entire country to foreign arrivals
for the first time in almost two years.
&quot;We need to move in a pace the Australian public feel very
comfortable with, we need to demonstrate that opening up those
borders is being done safely, and they can feel confident, because I
want us to open confidently,&quot; Prime Minister Scott Morrison said
Friday.
Victoria&#39;s 6.7 million residents can now leave their homes for any
reason, though they&#39;ll need to show proof of full vaccination to enter
public venues. Restaurants can cater for limited numbers of diners
indoors, students are back in schools, and there&#39;s no longer a 9 p.m.
curfew in Melbourne.
"""

list_of_word  =  Text.split(" ")

word = input("enter the word :")
counter = 0


for i in list_of_word:
    if i == word :
        counter +=1

print("the number of word is ",counter)


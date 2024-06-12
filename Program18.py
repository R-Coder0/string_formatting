#How can you format a string with placeholder for a variable value.

#there is multiple way to formate string like using "%" operator , .format method, using f-string

#using % operator
name = "Rishabh"
phone_number =7542003073
print("hey %s" '\n'"How are you ?"  "\n""your number iis %s" %(phone_number,name))

#using format() method
name1 = "Rahul"
phone_number1 =7545587852
print("hey {1}" 
      '\n'"How are you ?"  
      "\n""your number iis {0}" .format(phone_number1,name1))
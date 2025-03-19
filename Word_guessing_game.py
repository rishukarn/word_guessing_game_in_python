# word Guessing Game in python 
import random

User_Name=input('Enter your name: ')
print(f'Good luck ! {User_Name.capitalize()}')

choice_Animal=random.choice(['Lion','Elephant','Tiger','Giraffe','Zebra','Kangaroo','Panda'
                      ,'Dolphin','Wolf','Eagle','Penguin',
                      'Cheetah','Gorilla','Crocodile','Hippopotamus'])


# print(choice_Animal)

check_list=[]

for j in range(len(choice_Animal)):
            check_list.append('-')

chances=15
attempt=0
word_track=''


while chances!=0:
    temp_lst=[]
    for i in range(len(choice_Animal)):
        if check_list[i]=='-':
            temp_lst.append(i)
        print(check_list[i])
    
    
    
    if temp_lst != []:
           guess_word=input('Guess a character:: ')
           for i in temp_lst:
                if choice_Animal.upper()[i]==guess_word.upper() and check_list[i]=='-':
                        check_list[i]=guess_word.upper()
                        word_track+=guess_word
                        attempt+=1
                        break
                
           else:
                word_track+=guess_word
                attempt+=1
                chances -=1 
                  
    else:
        break

    

if chances !=0:
    print(f'You win \nYou Guess the word: {choice_Animal} in {attempt} attempt ')
else:
      print(f'You lose \nYou Guess word is Wrong: {word_track} \nYou have: {chances} attemp left \nRight word is: {choice_Animal} ')
            
    
            
        
      


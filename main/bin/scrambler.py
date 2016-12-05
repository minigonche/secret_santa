#Scrip that generated the permutations of the secret santa
#It simply gets random permutations and checks if th restriccions are satisfied

#Imports Numpy for permutations
import numpy as np
import user_handler as uh

#Loads th users in a dictionary
users_dic = uh.load_users()
#Gets the users_ids in an array
users_array = [i for i in users_dic]

#Loads the restrictions
restrictions = uh.load_restrictions()

invalid = True

while(invalid):

    #Randomizes the array
    users_array = np.random.permutation(users_array)

    #Gets the random integer
    step = np.random.randint(1,len(users_array),1)[0]
    
    secret_friend = {}
    #Rearranges the array
    for i in range(len(users_array)):
        secret_friend[users_array[i]] = users_array[(i + step)%len(users_array)]
    
    invalid = False
    
    for k in restrictions:
        invalid = (secret_friend[k] == restrictions[k])
        if(invalid):
            break
    
    if(invalid):
        print('Invalid Permutation. Trying again...')
    else:
        print('Valid Permutation. Saving...')
    
        
#Export secret_santa   

file_out = open('db/secret_santa.txt', 'w')
begin = False
for k in secret_friend:
    if(not begin):
        begin = True
    else:
        file_out.write('\n')
        
    file_out.write(k + ':' + users_dic[secret_friend[k]])
    

file_out.close()    
        


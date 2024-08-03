import os

CURRENT_DIR=str(input('Please enter Directory Path :'))

print('Current Directory is :', os.getcwd())
print('Directory given as input are :', CURRENT_DIR)

i=1

if os.path.exists(CURRENT_DIR) == True :
    dir_list = os.listdir(CURRENT_DIR) 
    number_of_dir_list =int(len(dir_list))
    print('Number of files in given directory is :', number_of_dir_list)
    print("Files and directories presents are :") 
    for files in dir_list:
        print( i , files)
        i+=1

else :
    print('Please provide a correct Directory Path')
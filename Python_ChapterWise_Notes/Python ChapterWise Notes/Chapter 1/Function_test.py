# Driver function
import os
if __name__ == '__main__':
    for (root,dirs,files) in os.walk('C:\\Users\\sojib.DESKTOP-87FHOSD\\Desktop\\Repo\\Practice_set_1\\', topdown=True):
        print (root)
        print (dirs)
        print (files)
        print ('--------------------------------')
#import modules make sure to install instaloader in your system "pip install instaloader"
import instaloader 
import os

#get your current directory where the script is being run from
path = os.getcwd() 

#load module 
ig = instaloader.Instaloader()

#start user input

#Target ig user name
dp = input("Enter Insta username : ")

#Where to save the folder with the pictures 
directory = input("is this the right path to download the files?(yes, no) \n " + path +"\n" )
if directory == "yes":
    ig.download_profile(dp , profile_pic_only=False)
if directory =="nop":
    save_loc = input("Enter where to save the files : ")
    os.chdir(save_loc)
    ig.download_profile(dp , profile_pic_only=False)
else:
    print("not a valid save path")
    
import os, random

# This Program will choose a Desktop Image at Random to set as your Wallpaper
# The goal is to integrate this program on Runtime to choose an Episode Slide
# From Adventure Time and set it as your background.

# def wallpaper_choice(number):
# 	os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/user/Pictures/wallpapers/X")

host_Folder = os.environ.get('USER')
wall_Num =str(random.randint(1,221)) + ".jpg"
dir_Name = '/home/'+ host_Folder + '/Pictures/at4w/'

folder_Path = dir_Name + wall_Num
print("Wallpaper Changed Successfully")

os.system("gsettings set org.gnome.desktop.background picture-uri file:" + folder_Path)





import os, random

host_Folder = os.environ.get('USER')
wall_Num =str(random.randint(1,221)) + ".jpg"
dir_Name = '/home/'+ host_Folder + '/Pictures/at4w/'

folder_Path = dir_Name + wall_Num
print("Wallpaper Changed Successfully")

os.system("gsettings set org.gnome.desktop.background picture-uri file:" + folder_Path)





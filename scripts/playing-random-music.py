import random, os ,subprocess
music_dir = ''#add your path /home/mbily/music
songs=os.listdir(music_dir)
song = random.randint(0,len(songs)-1)
print(songs[song])
# windows users
#os.startfile(os.path.join(music_dir,song[0]))
# linux users
file_name =os.path.join(music_dir,songs[song])
print(file_name)
subprocess.call(["xdg-open",file_name])
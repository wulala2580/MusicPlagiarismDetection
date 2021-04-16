from Classes import *
import os
data_path = 'D:/DaSanXia/CS222-Music-Plagiarism-master/dataset/'

def Vectorized(k):
    files = os.listdir(data_path)
    file_num = len(files)
    musics = []
    for file in files:
        music = Music(data_path + file)
        musics.append(music)

    for music in musics:
        music.pitch_difference()
        music.Vm = []
        music.Rm = []
        for i in range(len(music.notes_list)):
            if (i == 0):
                music.Rm.append(music.notes_list[i].length)
            else:
                music.Vm.append(music.notes_list[i].pitch)
                music.Rm.append(music.notes_list[i].length)

    
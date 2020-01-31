#os and shutil module
import os, shutil
dict_extension={

    "audio_Extension":(".mp3",".wmz",".wav",".flac",".aa",".vag"),
    "document_extension":(".doc",".pdf",".txt"),
    "videos_Extension":(".mp4",".3gp",".ogg",".avi"),

}


# audio_Extension=(".mp3",".wmz",".wav",".flac",".aa",".vag")
# document_extension=(".doc",".pdf",".txt")
# videos_Extension=(".mp4",".3gp",".ogg",".avi")

enter_path = input("enter the path :-")

def separate_file(folder_path,extension):
    new_file_list = []
    for file_in_folder in os.listdir(folder_path):
        for file_extension  in extension:
            if file_in_folder.endswith(file_extension):
                new_file_list.append(file_in_folder)
    return new_file_list


#print(separate_file(enter_path,audio_Extension))

# for key_extension_type,value_extension_tuple in dict_extension.items():
#     print("all_file")
#     print(separate_file(enter_path,value_extension_tuple))

for key_extension_type,value_extension_tuple in dict_extension.items():
    folder_name = key_extension_type.split("_")[0] + " folder"
    folder_path = os.path.join(enter_path,folder_name)
    os.mkdir(folder_path)
    for files in (separate_file(enter_path,value_extension_tuple)):
        file_path = os.path.join(enter_path,files)
        file_new_path = os.path.join(folder_path,files)
        shutil.move(file_path,file_new_path)

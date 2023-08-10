# %% [markdown]
# ___
# 
# <a href='https://www.udemy.com/user/joseportilla/'><img src='../../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by Pierian Data</em></center>

# %% [markdown]
# # Advanced Modules Exercise Puzzle
# 
# It's time to test your new skills, this puzzle project will combine multiple skills sets, including unzipping files with Python, using os module to automatically search through lots of files.
# 
# ## Your Goal
# 
# This is a puzzle, so we don't want to give you too much guidance and instead have you figure out things on your own.
# 
# There is a .zip file called 'unzip_me_for_instructions.zip', unzip it, open the .txt file with Python, read the instructions and see if you can figure out what you need to do!
# 
# **If you get stuck or don't know where to start, here is a [guide/hints](https://docs.google.com/document/d/1JxydUr4n4fSR0EwwuwT-aHia-yPK6r-oTBuVT2sqheo/edit?usp=sharing)**


# %%

import zipfile, os, send2trash, re


# %%

# zip_obj = zipfile.ZipFile('unzip_me_for_instructions.zip')
# zip_obj.extractall("extracted_content")


# %%

my_path = os.listdir(r".\extracted_content")

# %%

# First just get a feeling for how os.walk works

for folder, sub_folders, files in os.walk("extracted_content"):

    print("Currently looking at the folder: ", folder)
    print('\n')
    print("The subfolders are: ")
    for sub_folder in sub_folders:
        print("\t Subfolder: ", sub_folder)

    for f in files:
        print("\tThe files are: ", f)

    
# %%

# Now search through the files for a phone number with the format ###-###-####
pattern = r"\d{3}-\d{3}-\d{4}"

for folder, sub_folders, files in os.walk("extracted_content"):

    for file in files:
        with open(folder + '\\' + file) as f:
            file_text = f.read()

            match = re.findall(pattern, file_text)
            if match:
                print(match)
                print(folder + '\\' + file)


# %%

# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# 
# ANTsPy is a Python wrapper for the ANTs neuroimage processing library, along with other pythonic tools that make it easy and fun to work with brain images directly in Python.
# 

# First, install ANTsPy. It can be installed from source (takes 30-60min) with the following code:
# 
# ```
# git clone https://github.com/ANTsX/ANTsPy.git
# cd ANTsPy
# python setup.py install
# ```
# 
# It can also be installed very quickly from pre-made wheels (latest release only available for Mac, but a previous release is available for Linux which should be OK): https://github.com/ANTsX/ANTsPy/releases . Download the .whl file then run the following:
# ```
# for python 3.7 version at moment. Create env with python=3.7
# pip install /path/to/file.whl
# ```
# %% [markdown]
# # Alternative installation working for Linux
# ```
# conda create -n antspy python=3.8
# conda activate antspy
# pip install antspyxP
# ```

# %%
import ants
import numpy as np
import glob

# %% [markdown]
# # Image IO
# 
# Reading and writing images is easy. ANTsPy has some included data which we will use


# %%
''' load ref brain'''
reg_img= ants.image_read('test_data/reference-brain.tif')

''' load brain images to register'''
path =r'test_data/'
all_files = glob.glob(path + "/*stack.tif")
print (all_files)

images = []
for filename in all_files:
    img = ants.image_read(filename)
    images.append(img)
images



# %%
img1 = images[0]

print (reg_img)
print(img1)

# %%
reg_img.plot(overlay=img1, title='Before Registration', axis=2, cmap = 'Greys',
overlay_cmap = 'Blues')

# %%
mytx = ants.registration(fixed=reg_img, moving=img1, type_of_transform='SyN')
print(mytx)

#  %%
warped_moving = mytx['warpedmovout']
reg_img.plot(overlay=warped_moving,
           title='After Registration', axis=2, cmap = 'Greys',
overlay_cmap = 'Blues')
# %%
reg_img.plot(axis=2)
mytx['warpedmovout'].plot(axis=2)


# %%
'''perform registration for all files at once'''

images_to_register = images
results= []

for image in images_to_register:
     transf = ants.registration(fixed=reg_img, moving=image , type_of_transform='SyN')
     results.append(transf)

print (results)

# %%

for idx, r in enumerate(images):
    print (images_to_register[idx])
    images_moving = r
    reg_img.plot(overlay=images_moving,
           title='Before Registration', axis=2, cmap = 'Greys',
    overlay_cmap = 'Blues')

# %%
for idx, r in enumerate(results):
    print (images_to_register[idx])
    results_moving = r['warpedmovout']
    reg_img.plot(overlay=results_moving ,
           title='After Registration', axis=2, cmap = 'Greys',
    overlay_cmap = 'Blues')

# %% [markdown]
# Conclusions
# - For one of the brains this registration is not great. 
# - Need to optimize. Maybe first just rotate and then additional transformations
# - It it important to be consistent during data collection

# %%

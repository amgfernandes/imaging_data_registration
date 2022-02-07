# %%
import ants
import numpy as np
import glob


# %%
''' load ref brain'''
reg_img= ants.image_read('Register_test_individuals/tdtom_axons_cells/ref/tdtom1_10x_1024.nii.gz')
print (reg_img)

# %%

''' load brain images to register'''
path =r'Register_test_individuals/tdtom_axons_cells/compressed/'
all_files = glob.glob(path + "*nii.gz")
print (all_files)

images = []
for filename in all_files:
    img = ants.image_read(filename)
    images.append(img)
    img.plot(axis =2, nslices=1)
images


# %%
img1 = images[0]

print (reg_img)
print(img1)

# %%
reg_img.plot(overlay=img1, title='Before Registration', axis=2, cmap = 'Greys_r',
overlay_cmap = 'Blues')


# %%
mytx = ants.registration(fixed=reg_img, moving=img1, type_of_transform='Affine',
outprefix = 'ABC')
print(mytx)

#  %%
warped_moving = mytx['warpedmovout']
reg_img.plot(overlay=warped_moving,
           title='After Registration', axis=2, cmap = 'Greys_r',
overlay_cmap = 'Blues')

# %%
'''test for single file'''

ants.image_write(mytx['warpedmovout'], 'test_A_aligned.tif')


# %%
print(ants.image_mutual_information(reg_img, img1))
print(ants.image_mutual_information (reg_img, warped_moving))
# %%
reg_img.plot(axis=2)
mytx['warpedmovout'].plot(axis=2)


# %%

'''Try first Affine transformation before other'''

first = ants.registration(fixed=reg_img, moving=img1, type_of_transform='SyNCC', initial_transform='Affine')
print(first)

# %%

first_moving = first ['warpedmovout']
reg_img.plot(overlay=first_moving,
           title='After Affine first combined with other', axis=2, cmap = 'Greys',
overlay_cmap = 'Blues', overlay_alpha = 0.9, filename = 'try', nslices= 12)

print(ants.image_mutual_information (reg_img, first_moving))

'''test for single file'''

ants.image_write(first['warpedmovout'], 'test_B_aligned.tif')
# %
# %%
'''perform registration for all files at once'''

images_to_register = images
results= []

for image in images_to_register:
     transf = ants.registration(fixed=reg_img, moving=image , type_of_transform='SyN', initial_transform='Affine')
     results.append(transf)
     image.plot(axis=2, nslices =1)

print (results)

# %%

for idx, r in enumerate(images):
    print (images_to_register[idx])
    images_moving = r
    images_moving.plot(axis=2, nslices=1)
    reg_img.plot(overlay=images_moving,
           title='Before Registration', axis=2, cmap = 'Greys',overlay_cmap = 'Blues')

# %%
for idx, r in enumerate(results):
    print (images_to_register[idx])
    results_moving = r['warpedmovout']
    results_moving.plot(axis=2, nslices=1)
    reg_img.plot(overlay=results_moving ,
           title='After Registration', axis=2, cmap = 'Greys',
    overlay_cmap = 'Blues')

# %%

for idx, s in enumerate(results):
    results_moving = s['warpedmovout']
    print(f'Mutual information for image {idx} : {ants.image_mutual_information (reg_img, results_moving)}')

#%%

ants.image_write(results[0]['warpedmovout'], 'test_1_aligned.tif')
ants.image_write(results[1]['warpedmovout'], 'test_2_aligned.tif')
ants.image_write(results[2]['warpedmovout'], 'test_3_aligned.tif')

# %%

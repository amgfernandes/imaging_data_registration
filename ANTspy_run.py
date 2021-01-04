# %%

import ants
import time
import numpy as np
import os

print ('starting ANTspy')
start_time = time.time()

# %%
outputDirectory = '/home/fernandes/scripts/Python/ANTspy/OutputWithMaskANTsPy/'
if not os.path.isdir( outputDirectory ):
  os.mkdir( outputDirectory )

outputPrefix = outputDirectory + 'antsr'

# %%
ref = ants.image_read('/home/fernandes/scripts/Python/ANTspy/huclyntrfpt.nii.gz', dimension=3) #reference brain
align= ants.image_read('/home/fernandes/scripts/Python/ANTspy/average_reference-01.nii.gz',dimension=3) #brain to align
mask= ants.image_read('/home/fernandes/scripts/Python/ANTspy/huclyntrfpt_mask.nii.gz', dimension=3) #if using mask for only partial alignment
#
# %%
registrationWithMask = ants.registration(
  fixed = ref, moving = align,
  mask = mask,
  type_of_transform = "SyN",
  regIterations = ( 100, 75, 20, 0 ),
  verbose = True, outprefix = outputPrefix)

  # %%
ants.image_write( registrationWithMask['warpedmovout'], outputPrefix + "Warped.nii.gz" )
ants.image_write( registrationWithMask['warpedfixout'], outputPrefix + "InverseWarped.nii.gz" )

#%%
# Plot the fixed and warped moving image
#ants.plot(ref, overlay = registrationWithMask['warpedmovout'], overlay_cmap = "viridis", alpha = 0.9 )

# Plot the moving and warped fixed image
#ants.plot(align, overlay = registrationWithMask['warpedfixout'], overlay_cmap = "viridis", alpha = 0.9 )

#jacobian = ants.create_jacobian_determinant_image(ref, registrationWithMask['fwdtransforms'][0] )
#ants.plot( jacobian )

print("Runtime: {:.2f} minutes".format((time.time()-start_time)/60))

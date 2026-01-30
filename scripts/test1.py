import drjit as dr
import mitsuba as mi
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt

mi.set_variant('llvm_ad_rgb')

scene = mi.load_file('./scenes/cbox.xml', res=128, integrator='prb')
image_ref = mi.render(scene, spp=512)

# Preview the reference image
mi.util.convert_to_bitmap(image_ref)

params = mi.traverse(scene)
print(params)

image_init = mi.render(scene, spp=128)
bitmap = mi.util.convert_to_bitmap(image_init)
plt.imshow(bitmap.convert(mi.Bitmap.PixelFormat.RGB, mi.Struct.Type.UInt8))
plt.savefig('output.png')  # Save to file instead of showing

# keys = ['light.emitter.sampling_weight']
# param_ref = mi.Color3f(params[key])
# params[key] = mi.Color3f(0.01, 0.2, 0.9)
# params.update()
# 
# image_init = mi.render(scene, spp=128)
# mi.util.convert_to_bitmap(image_init)
# 
# opt = mi.ad.Adam(lr=0.05)
# opt[key] = params[key]
# params.update(opt)
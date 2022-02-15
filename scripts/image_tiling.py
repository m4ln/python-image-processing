from PIL import Image
import sys

tile_width = int(sys.argv[2])
tile_height = tile_width    

set_name = "A03"
magnification = "X40"
input_dir = "/home/mr38/sds_hd/sd18a006/Marlen/datasets/MITOS-ATYPIA-14/extract/train/" + set_name + "/frames/" + magnification + "/"
output_dir = input_dir + "_tiles_" + W + "_" + X
assure_path_exists(output_dir)

for filename in os.listdir(input_dir):
    image = Image.open(os.src_path.join(input_dir, filename))
    if image.size[0] % tile_width == 0 and image.size[1] % tile_height ==0 :
        currentx = 0
        currenty = 0
        while currenty < image.size[1]:
            while currentx < image.size[0]:
                print(currentx, ",", currenty)
                tile = image.crop((currentx,currenty,currentx + tile_width,currenty + tile_height))
                tile.save("x" + str(currentx) + "y" + str(currenty) + ".png","PNG")
                currentx += tile_width
            currenty += tile_height
            currentx = 0
    else:
        print("sorry your image does not fit neatly into", tile_width, "*", tile_height, "tiles")

# # input = "/home/mr38/sds_hd/sd18a006/Marlen/python/lena_gray.png"
# # img = Image.open(input)
# img = cv2.imread("/home/mr38/sds_hd/sd18a006/Marlen/histo_256.png") # 512x512
#
# img_shape = img.shape
# tile_size = (32, 32)
# offset = (32, 32)
#
# for i in xrange(int(math.ceil(img_shape[0]/(offset[1] * 1.0)))):
#     for j in xrange(int(math.ceil(img_shape[1]/(offset[0] * 1.0)))):
#         cropped_img = img[offset[1]*i:min(offset[1]*i+tile_size[1], img_shape[0]), offset[0]*j:min(offset[0]*j+tile_size[0], img_shape[1])]
#         # Debugging the tiles
#         cv2.imwrite("debug_" + str(i) + "_" + str(j) + ".png", cropped_img)
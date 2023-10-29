# import colorgram
#
# # Challenge is to print a list contaning tuples of (r,b,g) of all the colour object extracted from the image using colorgram
#
# colors = colorgram.extract('hirst_painting.jpg', 30)
# print(type(colors))
# # print(colors)
# # first_color = colors[0]
# # rgb = first_color.rgb
# # print(rgb)
# # print(first_color.proportion)
#
# # red = rgb[0]
# # red1 = rgb.r
# # print(red)
# # print(red1)
#
# # print(colorgram.Color)
#
# color_list = []
# # for i in range(0, len(colors)):
# for colr in colors:
#     # clr_rgb = colors[colr].rgb
#     r = colr.rgb[0]
#     g = colr.rgb[1]
#     b = colr.rgb[2]
#     clr_tup = (r, g, b)
#     color_list.append(clr_tup)
#
# print(color_list)

colours = [(215, 153, 102), (15, 19, 74), (235, 225, 101), (49, 85, 146), (111, 172, 213), (170, 80, 46), (48, 30, 20), (212, 85, 63), (194, 89, 124), (27, 43, 130), (111, 37, 64), (54, 117, 49), (23, 45, 28), (157, 62, 87), (196, 134, 171), (141, 32, 25), (118, 199, 162), (65, 27, 37), (152, 211, 196), (98, 112, 194), (31, 89, 46), (84, 80, 32), (64, 161, 115), (149, 212, 220), (165, 186, 225), (226, 174, 163)]
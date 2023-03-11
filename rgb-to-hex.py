rgb1 = int(input())
rgb2 = int(input())
rgb3 = int(input())
allrgb = (rgb1,rgb2,rgb3)
hex = []
colors = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,
	10 : "a",
	11 : "b",
	12 : "c",
	13 : "d",
	14 : "e",
	15 : "f"
}
for i in allrgb:
	if i < 10:
		hex.append(("0",i))
	elif i < 16:
		hex.append(("0"+colors[i]))
	elif i >= 16:
		f = colors[i//16]
		s = colors[i%16]
		hex.append((str(f)+str(s)))
print("#"+hex[0]+hex[1]+hex[2]

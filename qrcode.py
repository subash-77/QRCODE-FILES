#Import Library
import qrcode
#Generate QR Code
l=["subash certificate","saravana balaji certificate","kannan certificate"]
for i in range(0,len(l)):
    img=qrcode.make(l[i])
    img.save('%d.png'%i)
print("done")

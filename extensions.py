#Get users input
name=input("File name: ").lower().strip()

#if gif or png or jpey or jpg then print image/type
if ".gif" in name:
    print(" image/gif")

elif ".png" in name:
    print("image/png")

elif ".jpeg"  and ".jpg" in name:
    print("image/jpeg")


#if pdf or zip then print application/type
elif ".pdf" in name:
    print("application/pdf")

elif ".zip" in name:
    print("application/zip")

#if txt print text/plain
elif ".txt" in name:
    print("text/plain")

# others print applicatiaon/octet-stream
else:
    print("application/octet-stream")

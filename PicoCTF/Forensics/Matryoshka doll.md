This was fun. It helped me go through quite a few forensics tools for images. 

This [video](https://www.youtube.com/watch?v=rvpvY8yRTK8&ab_channel=GuyInTheShell) was fairly useful and so was this [blog-post](https://ctfs.github.io/resources/topics/steganography/file-in-image/README.html)

I started with exiftool and zsteg. The only two tools that I could remember. Then I did strings dolls.jpg and found the essence of a file hidden in the image.
The blogpost helped me realize that binwalk was the way forward....

After getting irritated because of the repeated extraction, I decided to go ahead with binwalk -e -M dolls.png to get the flag I wanted.

Victory, bishes!

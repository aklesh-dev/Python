import qrcode as qr 
img = qr.make("https://github.com/aklesh-dev")
img.save('github_aklesh.png')
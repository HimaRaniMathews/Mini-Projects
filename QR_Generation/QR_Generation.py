import qrcode
img=qrcode.make('https://open.spotify.com/track/2ZVMc9iFgQY7ZCxNibnvTW?si=70e9c18bb804484f')
img.save("MeditationMusic.png")
img.show()

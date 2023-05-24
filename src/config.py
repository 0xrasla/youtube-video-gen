import os

class Config:
    def __init__(self):
        pass

    def get(self, key):
        # Get the value for the specified key from the configuration dictionary
        config = {
            "image_apiurl": "https://source.unsplash.com/1080x1080/?nature",
            "quotable_apiurl": "https://api.quotable.io/random",
            "image_width": "1080",
            "image_height": "1080",
            "duration" : 8
        }
        return config[key]

    def loadfont_path(self, type):
        # Load the path of the font based on the specified type
        if type == "main":
            # Return the path of the main font
            return os.path.join("fonts", "Anton-Regular.ttf")
        # Return the path of the default font
        return os.path.join("fonts", "OpenSans-Variable.ttf")

    def loadimage_path(self):
        # Load the path of the image
        return os.path.join(os.getcwd(), "image.png")
    
    def loadmusic_path(self):
        # Load the path of the music file
        return os.path.join(os.getcwd(), "sudari.mp3")

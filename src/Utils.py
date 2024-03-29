from PIL import Image
import moviepy.editor as np
class Utils:
    def isImageBright(self, image : Image):
        return image.getextrema()[0][0] < 0

    # get the quote from the api and make it formatted
    def formatTheString(self, quote: str, author : str) -> str:
        """Format the string."""
        word_per_line = 3
        min_len = 13
        total_len = len(quote.split(" "))
        
        if total_len <= min_len:
            word_per_line = 3

        fresh_sentence = ''
        for i, lenn in enumerate(quote.split()):
            if(i % word_per_line == 0 and len(lenn) <= 30):
                fresh_sentence += '\n'

            fresh_sentence += lenn + ' '

        fresh_sentence += f"\n\n - {author}"

        return [fresh_sentence, total_len]
    
    def resize_func(t, duration):
        if t < 4:
            return 1 + 0.2*t  # Zoom-in.
        elif 4 <= t <= 6:
            return 1 + 0.2*4  # Stay.
        else: # 6 < t
            return 1 + 0.2*(duration-t)

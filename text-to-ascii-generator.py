"""
text to ASCII generator
"""

import os

try:
    import pyfiglet
    from termcolor import colored
    import colorama
    from PIL import Image
    from PIL import ImageDraw
except ImportError as ImpErr:
    raise ImportError("Import couldn't find module, or couldn't find name" +\
                      "in module {}".format(ImpErr))

colorama.init()
__ver__ = "0.1"

class FontGenerator:
    # fonts from pyfiglet
    font_list = [
        "3-d", "3x5", "5lineoblique", "acrobatic", "alligator", "alligator2", "alphabet", "avatar", "banner",
        "banner3-D",
        "banner3", "banner4", "barbwire", "basic", "bell", "big", "bigchief", "binary", "block", "bubble", "bulbhead",
        "calgphy2", "caligraphy", "catwalk", "chunky", "coinstak", "colossal", "computer", "contessa", "contrast",
        "cosmic",
        "cosmike", "cricket", "cursive", "cyberlarge", "cybermedium", "cybersmall", "diamond", "digital", "doh", "doom",
        "dotmatrix",
        "drpepper", "eftichess", "eftifont", "eftipiti", "eftirobot", "eftitalic", "eftiwall", "eftiwater", "epic",
        "fender", "fourtops", "fuzzy", "goofy", "gothic", "graffiti", "hollywood", "invita", "isometric1", "isometric2",
        "isometric3", "isometric4", "italic", "ivrit", "jazmine", "jerusalem", "katakana", "kban", "larry3d", "lcd",
        "lean",
        "letters", "linux", "lockergnome", "madrid", "marquee", "maxfour", "mike", "mini", "mirror", "mnemonic",
        "morse",
        "moscow", "nancyj-fancy", "nancyj-underlined", "nancyj", "nipples", "ntgreek", "o8", "ogre", "pawp", "peaks",
        "pebbles", "pepper", "poison", "puffy", "pyramid", "rectangles", "relief", "relief2", "rev", "roman", "rot13",
        "rounded", "rowancap", "rozzo", "runic", "runyc", "sblood", "script", "serifcap", "shadow", "short", "slant",
        "slide", "slscript", "small", "smisome1", "smkeyboard", "smscript", "smshadow", "smslant", "smtengwar", "speed",
        "stampatello", "standard", "starwars", "stellar", "stop", "straight", "tanja", "tengwar", "term", "thick",
        "thin",
        "threepoint", "ticks", "ticksslant", "tinker-toy", "tombstone", "trek", "tsalagi", "twopoint", "univers",
        "usaflag", "wavy",
        "weird"
    ]

    def __init__(self):
        """
        Program introduction
        """
       
        os.system("cls")
        print(colored(pyfiglet.figlet_format("Text to ASCII generator",
                                             font="slant"), "green"))
        print("Version: " + __ver__ + "\n")
        self.menu()

    def menu(self):
        """
        Set a font
        """
        error = False
        while True:
            if error != False:
                print error
                error = False
            else :
                print(colored("What kind of font do you want? ( q:exit , p:show all fonts )", "white", "on_green"))

            font = raw_input("> ")
            if font == "q":
                return
            if font == "p":
                self.show_all_fonts()
                continue
            if font not in self.font_list:
                error = "Do not have this font type, choose another one.\n"
                error += "All Fonts in: https://github.com/jmluang/text-to-ascii/blob/master/EXAMPLE"
            break

        self.introduction_and_generation(font)

    def introduction_and_generation(self, font):
        """
        Font example.
        It also accepts user's text.
        """

        while True:
            os.system("cls")
            print(pyfiglet.figlet_format("Sample Text", font=font))
            
            print(colored("Input text to convert: ", "white", "on_green"))
            text = raw_input("> ")

            ascii_text = pyfiglet.figlet_format(text, font=font)
            print(ascii_text)

            # Loop until a user type a correct command
            while True:
                print(colored("Save? t/i/b/q (text/image/back/exit)", "white", "on_green"))
                command = raw_input("> ")

                if command in ["b", "t", "i", "q"]:
                    if command == "b":
                        break
                    if command == "q":
                        return
                    name = raw_input("File name: ")
                    if command == "t":
                        file = open(name + ".txt", "w")
                        file.write(ascii_text)
                        file.close()
                    elif command == "i":
                        img = Image.new("RGB", (1, 1), (255, 255, 255))
                        d = ImageDraw.Draw(img)
                        text_width, text_height = d.textsize(ascii_text)
                        img = img.resize((text_width, text_height))
                        d = ImageDraw.Draw(img)
                        d.text((0, 0), ascii_text, (0, 0, 0))
                        img.save(name + ".png")
                    print(colored("Done!", "green"))
                    os.system("pause")
                    return

    def show_all_fonts(self):
        os.system("cls")
        print "-----------------------------------"
        for i,font in enumerate(self.font_list):
            print "%s" % font, 
            if i % 10 == 0:
                print "\n"
        print "\n-----------------------------------"
        return 
    

def main():
    font_generator = FontGenerator()


if __name__ == "__main__":
    main()

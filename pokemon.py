class Pokemon:
    def __init__(self, name):
        self.name = name
        self.spriteColors = {"normal": (0, 0, 0), "shiny": (0, 0, 0)}

    def setName(self, name):
        self.name = name

    def setSpriteColor(self, rgbs, shiny):
        if shiny:
            self.spriteColors["shiny"] = rgbs
            return
        self.spriteColors["normal"] = rgbs

    def setSpriteColors(self, rgbs):
        try:
            normal = rgbs["normal"]

            if isinstance(normal, list):
                normalTuple = ()
                for rgb in normal:
                    normalTuple = (*normalTuple, rgb)
                normal = normalTuple

            self.spriteColors["normal"] = normal

        except TypeError:
            pass

        try:
            shiny = rgbs["shiny"]
            if isinstance(shiny, list):
                shinyTuple = ()
                for rgb in shiny:
                    shinyTuple = (*shinyTuple, rgb)
                shiny = shinyTuple

            self.spriteColors["shiny"] = shiny
        except TypeError:
            pass

    def getName(self):
        return self.name

    def getSpriteColor(self, shiny):
        if shiny:
            return self.spriteColors["shiny"]
        return self.spriteColors["normal"]

    def getSpriteColors(self):
        return self.spriteColors

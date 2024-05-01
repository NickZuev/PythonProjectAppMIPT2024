class LanguageDependentString:
    """Provide language adapting string"""
    language = "english"
    def __init__(self, english, russian):
        self.data = {"english" : english, "russian" : russian}
    
    def __add__(self, another):
        self.data['english'] += another.data['english']
        self.data['russian'] += another.data['russian']
        return self
    
    def __str__(self):
        return self.data[self.__class__.language]
    
    @classmethod
    def set(cls, new_language):
        cls.language = new_language


class StringReference:
    """aka basic std::string&"""
    def __init__(self, string):
        self.string = string
    
    def set(self, string):
        self.string = string
    
    def __str__(self):
        return self.string

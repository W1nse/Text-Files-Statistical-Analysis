from multipledispatch import dispatch


class Analyzer():
    def __init__(self, text):
        self.text = text
        self.char_value_map = {}
        self.value_char_map = {}
    
    def character_freq(self,char:str)->int:
        freq = 0
        for c in self.text:
            if c==char:
                freq+=1
        
        return freq 

    @dispatch(int)
    def pmf(self ,x:int)->float:
        return 0.1
        
    @dispatch(str)
    def pmf(self ,c:str)->float:
        return "qwswq"
    
    @dispatch(int)
    def cdf(self, x:int)->float:
        return 0.1

    @dispatch(str)
    def cdf(self, c:str)->float:
        return 0.1

    def mean(self)->float:
        return 0
    
    def variance(self)->float:
        return 0
    
    def skewness(self)->float:
        return 0
    
    def kurtosis(self)->float:
        return 0

        
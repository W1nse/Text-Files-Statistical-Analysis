from multipledispatch import dispatch
from src.lib import generate_char_rv_dict, generate_rv_char_dict, filter_text

class Analyzer():
    def __init__(self, text):
        self.text = filter_text(text)
        self.char_value_map = generate_char_rv_dict()
        self.value_char_map = generate_rv_char_dict()
        self.frequencies = {i:self.character_freq(self.value_char_map[i]) for i in range(62)}

    
    def get_char_rv(self, char:str)->int:
        return self.char_value_map[char]
    
    def get_rv_char(self, x:int)->str:
        return self.value_char_map[x]

    def get_char_freq(self, char:str)->int:
        return self.frequencies[self.get_char_rv(char)]
    
    def get_rv_freq(self, x:int)->int:
        return self.frequencies[x]

    def get_repleated_characters(self, n:int)->list:
        freq_sorted = sorted(self.frequencies.items(), key=lambda item:item[1], reverse=True)
        return freq_sorted[:n]

    def character_freq(self,char:str)->int:
        freq = 0
        for c in self.text:
            if c==char:
                freq+=1
        
        return freq 
    
    def moment(self, moment_number:int)->float:
        value = 0
        for x_i in range(62):
            value = (x_i**moment_number)*self.pmf(x_i)
        return value        

    def centered_moment(self, moment_number:int)->float:
        value = 0
        for x_i in range(62):
            value = ((x_i-self.mean())**moment_number)*self.pmf(x_i)
        return value   

    @dispatch(int)
    def pmf(self ,x:int)->float:
        return self.character_freq(self.value_char_map[x])/len(self.text)
        
    @dispatch(str)
    def pmf(self ,c:str)->float:
        return self.character_freq(c)/len(self.text)
    
    @dispatch(int)
    def cdf(self, x:int)->float:
        cdf_value = 0
        for x_i in range(int(x)):
            cdf_value += self.pmf(x_i)

        return cdf_value
    

    def mean(self)->float:
        return self.moment(1)
    
    def variance(self)->float:
        return self.moment(2) - self.mean()**2
    
    def standard_deviation(self)->float:
        return self.variance()**0.5

    def skewness(self)->float:
        return self.centered_moment(3)/self.standard_deviation()**3
    
    def kurtosis(self)->float:
        return self.centered_moment(4)/self.standard_deviation()**4

        
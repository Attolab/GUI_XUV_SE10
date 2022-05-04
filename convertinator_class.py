class Convertinator:

    def str2float(string):
        return float(string.replace(',','.'))

    def float2str(number):
        return str(number)

    def isStringElementEmpty(elements):    
        return any([element == '' for element in elements])

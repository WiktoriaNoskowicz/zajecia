class ConfigFileHandler:
    data = {}
    path = ''
    def __init__(self, path):
        self.path = path
        file = open(path, 'r')
        for line in file.readlines():
            #line = line.strip()
            line_items = line.split(':')
            self.data[line_items[0]] = line_items[1].strip()
        print(self.data)
        file.close()

    def __getitem__(self, key): #odczyt val = obj[key]
        return self.data[key]

    def update_file(self): 
        file = open(self.path, 'w')
        for key, value in self.data.items():
            file.write(f'{key}: {value} \n')
        file.close()

    def __setitem__(self, key, value): #zapis obj[key] = val
        self.data[key] = value
        self.update_file()

    def __delitem__(self, key): #del obj[key]
        del self.data[key]
        self.update_file()

def main():
    config = ConfigFileHandler('data.txt')
    k1 = config['klucz1']
    config['klucz1'] = "abcdefg"
    print(k1)
    #del config['klucz2'] usuniecie obiektu zamyka plik

#[] -> operator subskrybcji

#zad 12
#funktor to obiekt ktory mozna wywolac jak funkcje dzieki metodzie call

class RollingAvg:
    def __init__(self,size):
        self.size=size

    def __call__(self,data):
        #data = list(map(lambda value: value+self.size, data))
        result = []
        for i in range(1, len(data)-1):
            result += [(data[i-1] + data[i] + data[i+1])/3]
        return [data[0]] + result + [data[-1]]

def main():
    data = [0,1,3,3,4,15,6,7,81,9]
    data = list(map(RollingAvg(5), [data])) #wtkorzystujemy obiekt jako funkcje
    print(data)


if __name__ == '__main__':
    main()

if __name__ == '__main__':
    main()
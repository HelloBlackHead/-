MaxSize = 100
class SqString:
    def __init__(self):
        self.data = [None]*MaxSize
        self.size = 0

    def StrAssign(self,cstr):
        for i in range(len(cstr)):
            self.data[i] = cstr[i]
        self.size = len(cstr)

    def __getsize(self):
        return self.size

    def __getitem__(self, item):
        if 0 <= item <self.size:
            return self.data[item]

    def __setitem__(self, key, value):
        if 0 <= key < self.size:
            self.data[key] = value

    def DisplayStr(self):
        for i in range(self.size):
            print(self.data[i],end = ' ')
        print()

    def count_s(self):
        for i in range(self.size+1):
            s = self.data[i]
            count = 1
            while self.data[i] and self.data[i+1] is not None:
                if s < self.data[i+1]:
                    s = self.data[i+1]
                    count = 1
                elif s == self.data[i+1]:
                    count += 1
                i += 1
            return '最大字符是{}，出现了{}次。'.format(s, count)

if __name__ == '__main__':
    s = SqString()
    c1 = '27385782'
    s.StrAssign(c1)
    print('顺序串为：')
    s.DisplayStr()

    print('-'*30)
    s.count_s()
    print(s.count_s())





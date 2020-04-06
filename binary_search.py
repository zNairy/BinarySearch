#/usr/bin/python3
#coding: utf-8

__author__ = 'Nairy'
__version__ = ''
__contact__ = '__Nairy__#7181 / https://www.github.com/znairy/'

'''Algorítmo de busca/pesquisa binária (Binary Search)'''

class BinarySearch(object):
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target
        self.left_pointer = 0
        self.right_pointer   = len(self.arr) - 1
        self.result = None

    def search(self):
        while True is not False:
            self.result = int((self.left_pointer + self.right_pointer) / 2)
            if(self.arr[self.result] == self.target):
                print(f'Target {self.target} encontrado na posição {self.result}')
                break
            else:
                if(self.arr[self.result] > self.target):
                    self.right_pointer = self.result
                else:
                    self.left_pointer = self.result
    
    def main(self):
        if(self.target in self.arr):
            if(self.target != self.arr[(len(self.arr)-1)]):
                self.search()
            else:
                print(f'Target {self.target} encontrado na posição {(len(self.arr))-1}')
        else:
            print(f'Erro, a target {self.target} não se encontra no array!')


def main():
    bs = BinarySearch([1,2,3,4,5,6,7,8,9,10], 4) #your array
    bs.main()

if __name__ == '__main__':
    main()
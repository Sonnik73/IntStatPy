
from numpy import exp, array, random, dot
import math
import re
import os
from openpyxl import load_workbook
import io
from pprint import pprint
import sys


"""
pattern = re.compile(r'\w+')

with io.open('Text.txt', encoding='utf-8') as file:
    for line in file:
        
        #lineS = file.readline()
        x = re.sub("^\s+|\n|\r|\s+$", '', line)
        while line:
            print(str(pattern.findall(x)))
"""






TestArray= array([[-4.0,-1.0,-2.0,-2.0,13.0,-4.4,-8.7,0,0,0,-4.0,-0.3,0,-109.0,-126.0], [-4.0,-1.0,-2.0,-2.0,13.0,-4.4,-8.7,0,0,0,-4.0,-0.3,0,-109.0,-126.0]])
"""
with open('Text.txt', 'r') as file:
    lst = file.readlines()
lst = [[float(n) for n in x.split()] for x in lst]
lstout=[]


for i in range(len(lst)):
    #lst[0]=(lst[0])[:-1]
    lstout.append(lst[i][-1])
    del lst[i][-1]
"""







class NeuralNetwork():
    def __init__(self):
        # Запустить генератор случайных чисел, чтобы он генерировал те же числа
        # каждый раз, когда программа запускается.

        random.seed(1)

        # Мы моделируем один нейрон с 3 входными и 1 выходным соединением.
        # Мы присваиваем случайные веса матрице 3 x 1 со значениями в диапазоне от -1 до 1
        # и означает 0.
        self.synaptic_weights = 2 * random.random((14, 1)) - 1

    # Сигмовидная функция, которая описывает S-образную кривую.
    # Мы передаем взвешенную сумму входных данных через эту функцию
    # нормализуйте их между 0 и 1.
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))


    # Производная сигмоидной функции.
    # Это градиент сигмовидной кривой.
    # Это показывает, насколько мы уверены в существующем весе.
    def __sigmoid_derivative(self, x):
        return x * (1 - x)


    # Мы обучаем нейронную сеть в процессе проб и ошибок.
    # Регулировка синаптических весов каждый раз.
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            # Пройдите обучение через нашу нейронную сеть (один нейрон).
            output = self.think(training_set_inputs)

            # Рассчитать ошибку (разница между желаемым выводом
            # и прогнозируемый результат).
            error = training_set_outputs - output


            # Умножьте ошибку на вход и снова на градиент сигмоидной кривой.
            # Это означает, что менее уверенные веса корректируются больше.
            # Это означает, что входные данные, которые равны нулю, не вызывают изменения весов.
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

            
            # Отрегулируйте вес.
            self.synaptic_weights += adjustment


    # Нейронная сеть думает.
    def think(self, inputs):
        
        # Передача входных данных через нашу нейронную сеть (наш единственный нейрон).
        return self.__sigmoid(dot(inputs, self.synaptic_weights))


if __name__ == "__main__":

    # Запуск одной нейронной сети нейронов.

    neural_network = NeuralNetwork()

    print ("Random starting synaptic weights: ")
    print (neural_network.synaptic_weights)


    # Учебный комплект. У нас есть 4 примера, каждый из которых состоит из 3 входных значений
    # и 1 выходное значение.
    #training_set_inputs = array([[0, 0, 1, 1, 1], [1, 1, 1, 1, 0], [1, 0, 1, 1, 1], [0, 1, 1, 1, 1]])
    #training_set_outputs = array([[0, 1, 1, 0]]).T

    with open('Text.txt', 'r') as file:
        lst = file.readlines()
    lst = [[int(n) for n in x.split()] for x in lst]
    lstout=[]
    for i in range(len(lst)):
        lstout.append(lst[i][-1])
        del lst[i][-1]
    print(len(array(lstout)))
    print(lstout)
    print(len(array(lst)))
    pprint(lst)

    training_set_inputs = array(lst)
    training_set_outputs = array([lstout]).T



    # Тренируйте нейронную сеть, используя тренировочный набор.
    # Сделайте это 10000 раз и вносите небольшие корректировки каждый раз.
    neural_network.train(training_set_inputs, training_set_outputs, 10000)

    print ("New synaptic weights after training: ")
    print (neural_network.synaptic_weights)

    # Протестируйте нейронную сеть в новой ситуации.
    print ("Considering new situation [1, 0, 0] -> ?: ")
    print (neural_network.think(array([0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0])))




"""
    with open('Text.txt', 'r') as file:
        lst = file.readlines()
    lst = [[float(n) for n in x.split()] for x in lst]
    lstout=[]
    for i in range(len(lst)):
    #lst[0]=(lst[0])[:-1]
        lstout.append(lst[i][-1])
        del lst[i][-1]
    print(len(lstout))
    print(len(lst))
"""

    
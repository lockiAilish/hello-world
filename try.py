import random

class Perceptron:
    def _init_(self,input_number,step_size=0.1):
        self._ins = input_number #Numero de parametros de entrada

        #Seleccionamos Pesos aleatorios
        self._w=[random.random() for _ in range (input_number)] #variable pesos
        self._eta = step_size #tasa de convergencia
        def predict (self, inputs):
            #producto punto de entrada y pesos
            weighted_average = sum(w*elm for w, elm in zip(self._w,inputs))
            if weighted_average > 0:
                return 1
            return 0
        def train(self,inputs, ex_output):
            output = self.predict(inputs)
            error = ex_output - output #Error es la diferencia entre salida
            #correcta y salida esperada
            if error != 0:
                self._w = [w+self._eta*error*x for w,x in zip (self.w,inputs)]
            return error

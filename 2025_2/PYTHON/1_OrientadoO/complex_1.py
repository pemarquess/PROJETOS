# O Arquivo e o "Molde" (__init__ e __str__)
import math # Vamos precisar para a raiz quadrada depois

class ComplexNumber:
    def __init__(self, real, imag):
        """
        O Construtor: Roda automaticamente quando criamos um novo objeto.
        Aqui definimos os atributos (propriedades) do objeto.
        """
        self.real = real
        self.imag = imag

    def __str__(self):
        """
        A Representação: Define o que aparece quando damos print(objeto).
        Sem isso, o Python mostraria <ComplexNumber object at 0x7f...>
        """
        sign = "+" if self.imag >= 0 else "-"
        # Formata bonitinho: "3 + 4i" ou "3 - 4i"
        # O abs(self.imag) garante que não fique "3 + -4i"
        return f"{self.real} {sign} {abs(self.imag)}i"

# --- Área de Teste Rápido ---
if __name__ == "__main__":
    z1 = ComplexNumber(3, 4)
    z2 = ComplexNumber(1, -2)
    
    print(f"Número 1: {z1}") # Deve imprimir: 3 + 4i
    print(f"Número 2: {z2}") # Deve imprimir: 1 - 2i


import math

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        sign = "+" if self.imag >= 0 else "-"
        return f"{self.real} {sign} {abs(self.imag)}i"

    # --- Métodos Mágicos (Operações) ---
    
    def __add__(self, other):
        # Soma
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return ComplexNumber(new_real, new_imag)

    def __sub__(self, other):
        # Subtração (Cuidado com a indentação aqui!)
        new_real = self.real - other.real
        new_imag = self.imag - other.imag
        return ComplexNumber(new_real, new_imag)

    def __mul__(self, other):
        # Multiplicação
        new_real = (self.real * other.real) - (self.imag * other.imag)
        new_imag = (self.real * other.imag) + (self.imag * other.real)
        return ComplexNumber(new_real, new_imag)

    def __abs__(self):
        # Módulo (Raiz quadrada)
        return math.sqrt(self.real**2 + self.imag**2)

# --- Testes ---
if __name__ == "__main__":
    z1 = ComplexNumber(3, 4)
    z2 = ComplexNumber(1, -2)
    
    print(f"Soma: {z1 + z2}")
    print(f"Subtração: {z1 - z2}")
    print(f"Multiplicação: {z1 * z2}")
    print(f"Módulo de z1: {abs(z1)}")
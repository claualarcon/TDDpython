'''
Created on 27 nov. 2017

@author: ClaudiaEstefania
'''
import unittest
from Juego.JuegoBowling import JuegoBowling

class TestJuego(unittest.TestCase):
    
    def testFrame(self):
        frame1 = JuegoBowling()
        result = frame1.frame(valor1=5, valor2=1)
        self.assertEqual(result, 6, "Falla")
        
        
    def testContador(self):
        contador = JuegoBowling()
        result1 = contador.cuentaFrame()
        self.assertEqual(result1, 9, "Falla")
        
    
    def testFrametodos(self):
        todos = JuegoBowling()
        result2 = todos.cuentaFrame()
        self.assertEqual(result2, 300, "Falla")
    
    
        
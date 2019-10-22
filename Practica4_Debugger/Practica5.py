#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys;


class llista_primers:

    """
    Aquest programa és una llista on s'hi afegiràn els nombres prims. L'usuari introduïrà un número
    i a continuació es mostrarà el nombre de números indicats per l'usuari.


    TEST:

    >>> llista_primers(5).llista
    [2, 3, 5, 7, 11]

    >>> llista_primers(8).llista
    [2, 3, 5, 7, 11, 13, 17, 19]

    >>> llista_primers(12).llista
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    """
    def __init__(self, n):
        """
        Tot seguit, s'incialitzarà la variable "n" i a continuació es crearà una llista en blanc i un buscador anomenat "busca".

        """
        self.n = n
        self.llista = []
        self.busca()

    def busca(self):
        """
        Aquesta serà la funció principal. Començarà en 0, però degut al primer if, sempre que "llista" sigui 0 passarà a ser 2.
        Per tant, sempre que la llista no contingui res, s'afegirà un 2 i sempre que el número actual de la llista sigui més petit que "n", "trobat" serà "False"
        i a continuació es sumarà +1 a l'últim número de la llista. El bucle continuarà sempre i quan "trobat" continui sent "False".
        A continuació,s'executarà un "seguent" % "i". El programa executarà una divisió amb algún dels números de la llista que dongui com a residu 0.
        Quan la llista arriba al número de nombres introduïts per l'usuari "trobat" passarà a ser "true" finalitzant d'aquesta manera el bucle.


        """

        if (len(self.llista) == 0):

            self.llista.append(2)
            self.busca()
        elif (len(self.llista) < self.n):
            trobat = False


            seguent = self.llista[-1]+1
            while not trobat:

                for i in self.llista:
                    if seguent%i == 0:
                        seguent += 1
                        trobat = False
                        break
                    else:
                        trobat = True
            self.llista.append(seguent)
            self.busca()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    #l = llista_primers(int(sys.argv[1]))
    #print l.llista

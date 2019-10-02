class EquacioPrimerGrau:

    def __init__(self,equacio):
        self.seq = equacio
        self.a=" "
        self.b=" "
        self.operador=" "
        self.c= " "

    def calcula(self):

        equ=self.seq.split()
        a=equ[0]
        a=a[:-1]
        b=equ[2]
        operador=equ[1]
        c=equ[4]

        if(operador=="+"):
            resultat=(int(c)-int(b))/int(a)

            if(operador=="-"):
                resultat=(int(c)+int(b))/int(a)

            print("x = "+str(resultat))

equacio = EquacioPrimerGrau("2x + 3 = 7")
print(equacio.seq)
equacio.calcula()

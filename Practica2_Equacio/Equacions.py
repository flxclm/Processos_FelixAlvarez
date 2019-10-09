class EquacioPrimerGrau:

    def __init__(self,equacio):
        self.seq = equacio
        self.a=" "
        self.b=" "
        self.operador=" "
        self.c= " "

    def calcula(self):

        try:
            self.equ=self.seq.split()
            self.a=self.equ[0]
            self.a=self.a[:-1]
            self.b=self.equ[2]
            self.operador=self.equ[1]
            self.c=self.equ[4]
        except:
            return ("l'equacio no segueix el format: " + self.seq)
        try:

            if(self.operador=="+"):
                self.resultat=(float(self.c)-float(self.b))/float(self.a)

            elif(self.operador=="-"):
                self.resultat=(float(self.c)+float(self.b))/float(self.a)
            else:
                self.resultat = "Operador no valid: " +self.operador

            return self.resultat

        except:
            return ("l'equacio conte caracter no calculables: " + self.seq)

equacio = EquacioPrimerGrau("2x + 3 = 7")
#print(equacio.seq)
equacio.calcula()

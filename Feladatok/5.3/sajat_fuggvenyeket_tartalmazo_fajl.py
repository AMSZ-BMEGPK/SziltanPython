import sympy as sp

# Az előző héti anyagban (4.3-4.5) definiált és elmagyarázott függvény külső fájlban tárolva

def print_eigensystem_feszultseg(matrix):
    # Legyen a függvény bemenete a vizsgálandó mátrix
    eig_system= matrix.eigenvects()
    
    # Az eredményt a program nem rendezi alapból a sajátértékek nagysága szerint, így azt nekünk kell megtenni
    # A rendezést a 'tuple'-ök első elemei szerint végezzük
    # Utánanézési lehetőség: lambda függvények, sorted() függvény 
    eig_system.sort(key=lambda x: x[0], reverse=True)
    
    # Végig iterálva az 'eig_system' elemein, kiiratjuk a főfeszültségeket és főirányokat
    n = 1
    for elem in eig_system:
        # Ha egy főfeszültség többszörös multiplicitású, akkor többször kell kiírni!
        for i in range(elem[1]): # Az 'elem[1]' értéke a multiplicitást mutatja meg.
                                 # 'range(elem[1])' : csinál egy 'range' objektumot, amin a 'for' ciklus végig
                                 # tud futni. Pontosan annyiszor fut le így a ciklus, amekkora számot adunk a
                                 # 'range' függvény argumentumaként, jelen esetben ez 'elem[1]', azaz a multiplicitás
            sajatertek = elem[0].evalf(5)
            # Normáljuk a sajátvektorokat, hogy egység hosszúságúak legyenek
            sajatvektor = (elem[2][i].normalized()).evalf(5) # '.norm()': a vektor hosszát adja vissza
            # Az 'n' változóval sorszámozzuk az egyes értékeket
            print(str(n)+'. Főfeszültség: '+str(sajatertek.evalf(5))+' MPa')
            print(str(n)+'. Főirány: ')
            display(sajatvektor)
            n += 1 # sorszám léptetése

def print_eigensystem_alakvaltozas(matrix):
    # Legyen a függvény bemenete a vizsgálandó mátrix
    eig_system= matrix.eigenvects()
    
    # Az eredményt a program nem rendezi alapból a sajátértékek nagysága szerint, így azt nekünk kell megtenni
    # A rendezést a 'tuple'-ök első elemei szerint végezzük
    # Utánanézési lehetőség: lambda függvények, sorted() függvény 
    eig_system.sort(key=lambda x: x[0], reverse=True)
    
    # Végig iterálva az 'eig_system' elemein, kiiratjuk a főfeszültségeket és főirányokat
    n = 1
    for elem in eig_system:
        # Ha egy főfeszültség többszörös multiplicitású, akkor többször kell kiírni!
        for i in range(elem[1]): # Az 'elem[1]' értéke a multiplicitást mutatja meg.
                                 # 'range(elem[1])' : csinál egy 'range' objektumot, amin a 'for' ciklus végig
                                 # tud futni. Pontosan annyiszor fut le így a ciklus, amekkora számot adunk a
                                 # 'range' függvény argumentumaként, jelen esetben ez 'elem[1]', azaz a multiplicitás
            sajatertek = elem[0].evalf(5)
            # Normáljuk a sajátvektorokat, hogy egység hosszúságúak legyenek
            sajatvektor = (elem[2][i].normalized()).evalf(5) # '.norm()': a vektor hosszát adja vissza
            # Az 'n' változóval sorszámozzuk az egyes értékeket
            print(str(n)+'. Főnyúlás: '+str(sajatertek.evalf(5)))
            print(str(n)+'. Főirány: ')
            display(sajatvektor)
            n += 1 # sorszám léptetése
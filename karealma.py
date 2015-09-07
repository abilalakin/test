# test
def kareAl(sayi):
    kare=sayi**2
    return kare

girilen = input('Karesi alınacak sayıyı giriniz:')
#Tam sayı girilmeyebilir bu nedenle float yapılmalı.
girilenDeger=float(girilen)
k=kareAl(girilenDeger)
print ('Girdiğiniz sayının karesi:' , k)


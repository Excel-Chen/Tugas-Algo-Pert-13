import os
satuan = ["","satu","dua","tiga","empat","lima","enam","tujuh","delapan","sembilan"]
def terbilang (n) :
    if n%1>0 :
        # adanya . sebagai koma
        str_n = str(n)
        cari_koma = str_n.find(".")
        belakang_koma = str_n[cari_koma+1:]
        depan_koma = str_n[:cari_koma]
        angka_belakang_koma = int(belakang_koma)
        angka_depan_koma = int(depan_koma)

        return terbilang(angka_depan_koma)+" koma "+terbilang(angka_belakang_koma)

    elif n<10 :
        #satuan
        return satuan[int(n)]
    elif n < 20 :
        #belasan
        if n == 10: return " sepuluh "
        if n == 11 : return " sebelas "
        else : return terbilang(n%10) + ' belas ' #dua belas - sembilan belas

    elif n < 100 : # puluhan
        return terbilang(n//10) + " puluh " +  terbilang(n%10)
    
    elif n < 1000 : # ratusan
        if n // 100 == 1 : return " seratus "  + terbilang(n%100)
        else : return terbilang(n//100) + " ratus " +  terbilang(n%100)

    elif n < 1_000_000 : # ribuan
        if n // 1000 == 1 : return " seribu" + terbilang(n%1000)
        else : return terbilang(n//1000) + " ribu " +  terbilang(n%1000)
  
    elif n < 1_000_000_000 : # jutaan
        return terbilang(n//1_000_000)+" juta "+terbilang(n%1_000_000)

    elif n < 1_000_000_000_000: # milliaran
        return terbilang(n//1_000_000_000)+" miliar"+terbilang(n%1_000_000_000)

    elif n < 1_000_000_000_000_000: # triliunan
        return terbilang(n//1_000_000_000_000)+" triliun "+terbilang(n%1_000_000_000_000)
    

while True:
    os.system('cls')
    try :
        n = float(input("Masukkan sebuah bilangan : "))
    except :
        print('Err : Wrong input')
    else :
        print(f"{n if n%1>0 else int(n)} -> {terbilang(n)}")

    while True :
        repe = input('Ulang ? [y] / [n]').lower()
        if repe in 'yn':
            break
    if repe in 'n':
        break
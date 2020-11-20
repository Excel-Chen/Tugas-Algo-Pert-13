import os
satuan = ["","one","two","three","four","five","six","seven","eight","nine"]
def terbilang (n) :
    if n%1>0 :
        # adanya . sebagai koma
        str_n = str(n)
        cari_koma = str_n.find(".")
        belakang_koma = str_n[cari_koma+1:]
        depan_koma = str_n[:cari_koma]
        angka_belakang_koma = int(belakang_koma)
        angka_depan_koma = int(depan_koma)

        return terbilang(angka_depan_koma)+" point "+terbilang(angka_belakang_koma)

    elif n<10 :
        #satuan
        return satuan[int(n)]
    elif n < 20 :
        #belasan
        if n == 10: return " ten "
        elif n == 11 : return " eleven "
        elif n == 12 : return " twelve "
        elif n == 13 : return " thirteen "
        elif n == 14 : return " fourteen "
        elif n == 15 : return " fifteen "
        else : return terbilang(n%10) + 'teen ' #dua belas - sembilan belas

    elif n < 100 : # puluhan
        if n // 10 == 2 : return " twenty " + terbilang(n%10)
        elif n // 10 == 3 : return " thirty " + terbilang(n%10)
        elif n // 10 == 4 : return " forty " + terbilang(n%10)
        elif n // 10 == 3 : return " fifty " + terbilang(n%10)
        return terbilang(n//10) + "ty " +  terbilang(n%10)
    
    elif n < 1000 : # ratusan:
        return terbilang(n//100) + " hundred " +  terbilang(n%100)

    elif n < 1_000_000 : # ribuan
        return terbilang(n//1000) + " thousand " +  terbilang(n%1000)
  
    elif n < 1_000_000_000 : # jutaan
        return terbilang(n//1_000_000)+" million "+terbilang(n%1_000_000)

    elif n < 1_000_000_000_000: # milliaran
        return terbilang(n//1_000_000_000)+" billion "+terbilang(n%1_000_000_000)

    elif n < 1_000_000_000_000_000: # triliunan
        return terbilang(n//1_000_000_000_000)+" trilion "+terbilang(n%1_000_000_000_000)
    

while True:
    os.system('cls')
    try :
        n = float(input("Input a number : "))
    except :
        print('Err : Wrong input')
    else :
        print(f"{n if n%1>0 else int(n)} -> {terbilang(n)}")

    while True :
        repe = input('Repeat ? [y] / [n]').lower()
        if repe in 'yn':
            break
    if repe in 'n':
        break
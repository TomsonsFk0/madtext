def sasveicinaties(vards,vards2,vards3,vards4,vards5):
    pass
madTex1, madTex2, madTex3, madTex4, madTex5 = ["","","","",""] , ["","","","",""] , ["","","","",""] , ["","","","",""] , ["","","","",""]
print(type(madTex4))

def pirmaisspeletajs():
    madTex1[0] = input("KĀDS? ")
    madTex2[1] = input ("KAS? ")
    madTex3[2] = input ("KUR? ")
    madTex4[3] = input ("KO DARĪJA? ")
    madTex5[4] = input ("KAS SANĀCA? ")


def otraisspeletajs():
    madTex2[0] = input("KĀDS? ")
    madTex1[1] = input ("KAS? ")
    madTex5[2] = input ("KUR? ")
    madTex4[3] = input ("KO DARĪJA? ")
    madTex3[4] = input ("KAS SANĀCA? ")

def tresaisspeletajs():
    madTex3[0] = input("Kāds?")
    madTex2[1] = input("Kas?")
    madTex1[2] = input("Kur?")
    madTex5[3] = input("Ko darīja?")
    madTex4[4] =input("Kas sanāca?")
def ceturtaisspeletajs():
    madTex4[0] = input("Kāds?")
    madTex3[1] = input("Kas?")
    madTex2[2] = input("Kur?")
    madTex1[3] = input("Ko darīja?")
    madTex5[4] = input("Kas sanāca?")

def piektiasspeletajs():
    madTex5[0] = input("Kāds?")
    madTex4[1] = input("Kas?")
    madTex3[2] = input("Kur?")
    madTex2[3] = input("Ko darīja?")
    madTex1[4] = input("Kas sanāca?")

if __name__ == '__main__':
    print("Labdien,šajā spēlē kad atbildes uz jautājumiem tiek uzrakstītas uz lapiņām. Katrs spēlētājs atbild uz jautājumu, aizloka lapiņu un padot tālāk nākamajam spēlētājam līdz ir atbildēts uz visiem jautājumiem. Spēles beigās tiek nolasīti teikumi, kas izveidojušies spēles rezultātā.")
    speletajs1 = input("Kā sauc pirmo spēlētaju?")
    print(speletajs1 + " ,Atblidi uz jautājumiem!")
    pirmaisspeletajs()
    print(madTex1)
    
    speletajs2 = input("Kā sauc otro spēlētāju?")
    print(speletajs2 + " ,Atblidi uz jautājumiem!")
    otraisspeletajs()
    print(madTex1)

    speletajs3 = input("Kā sauc treso spēlētāju?")
    print(speletajs3 + " ,Atblidi uz jautājumiem!")
    tresaisspeletajs()
    print(madTex1)

    speletajs4 = input("Kā sauc ceturto spēlētāju?")
    print(speletajs4 + " ,Atblidi uz jautājumiem!")
    ceturtaisspeletajs()
    print(madTex1)

    speletajs5 = input("Kā sauc piekto spēlētāju?")
    print(speletajs5 + " ,Atblidi uz jautājumiem!")
    piektiasspeletajs()
    print(madTex1)

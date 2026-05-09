class Phones():
        Screen=1
        Buttons=4
        Charging_Port=True
        Shape="Rectangle"
        Can_Swim=False

        def Ring_Tone(self):
                print("Airtel Phonk")

        def Picture(self):
                print("Click!")

Iphone=Phones()
Samsung=Phones()
Redmi=Phones()
OnePlus=Phones()
Nokia=Phones()

print(Iphone.Can_Swim)
print(Nokia.Shape)

OnePlus.Picture()
Redmi.Ring_Tone()
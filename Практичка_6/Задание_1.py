temp = (float(input("здравствуйте, напишите пожалуйста вашу температуру: ")))
pulse = int(input("теперь пульс: "))
pressure = int(input("ну и давление: "))

if temp >= 36.0 and temp <=37.0 or pressure >= 110 and pressure <= 130 or pulse >= 60 and pulse <= 100:
    print("У вас всё в норме!")

elif temp > 37.0 and temp < 36.0 or pressure < 110 and pressure > 130 or pulse < 60 and pulse > 100:
    print("У вас легкое недомогание")

else:
    print("Вам требуется врач!")
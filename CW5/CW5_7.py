class Temperature:
    def __init__(self, value, unit="C"):
        self.value = value
        self.unit = unit

    def convert_C(self):
        if self.unit == "C":
            return self.value
        elif self.unit == "F":
            return (32 - self.value) * 5 / 9

    def Convert_F(self):
        if self.unit == "F":
            return self.value
        elif self.unit == "C":
            return (self.value * 9 / 5) + 32


temp1 = Temperature(72, "C")
print("convert F: ", temp1.Convert_F())

temp2 = Temperature(180, "F")
print("convert C: ", temp2.convert_C())

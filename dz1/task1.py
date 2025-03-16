class Auto:
    def __init__(self,model,year,proizvoditel,color,price):
        self.model = model
        self.__year = year
        self.proizvoditel = proizvoditel
        self.engine = input("Введите объем двигателя: ")
        self.color = color
        self.__price = price

    def get_year(self):
        return self.__year

    def get_price(self):
        return self.__price

    def set_color(self):
        color = input("Введите цвет: ")
        self.__color = color
    
    def get_color(self):
        return self.__color

auto = Auto("Tesla", "2015", "Mask", "white", "100000")
print(auto.model, auto.proizvoditel, auto.engine)

auto.set_color()
print(auto.get_year(), auto.get_color(), auto.get_price())

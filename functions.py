import math
from datetime import datetime, timedelta


class StockManager:
    def __init__(self):
        self.initial_stock = 2200
        self.anual_demand = 50000
        self.order_cost = 10
        self.posession_cost = 0.7
        self.delivery_time = 7
        self.security_stock = 1000
        self.daily_demand = self.anual_demand/365

        self.date = datetime.today()

        self.material_to_number = {
            'Tecido': 0,
            'Algodao': 1,
            'Fio': 2,
            'Poliester': 3
        }

        self.number_to_material = {
            0: 'Tecido',
            1: 'Algodao',
            2: 'Fio',
            3: 'Poliester'
        }

        self.clothing_sizes_material = {
            'Tshirt': {
                'Tecido': 1,
                'Algodao': 0.8,
                'Fio': 0.4,
                'Poliester': 1.3,
            },
            'Calcoes': {
                'Tecido': 0.8,
                'Algodao': 0.7,
                'Fio': 0.4,
                'Poliester': 1.4,
            },
            'Camisola': {
                'Tecido': 0.5,
                'Algodao': 0.35,
                'Fio': 0.5,
                'Poliester': 1.15,
            },
            'Calcas': {
                'Tecido': 1.2,
                'Algodao': 0.95,
                'Fio': 0.35,
                'Poliester': 1.5,
            },
        }


        self.tipos_dict = {
            0: 'Tshirt',
            1: 'Calcoes',
            2: 'Camisola',
            3: 'Calcas'
        }

        self.tamanhos_dict = {
            0: 'XS',
            1: 'S',
            2: 'M',
            3: 'L',
            4: 'XL'
        }

        self.sizes_to_ratio = {
            0: 0.5,
            1: 0.75,
            2: 1,
            3: 1.5,
            4: 2,
        }
    

        self.stock_levels = {
            'Tecido': 2200,
            'Algodao': 2200,
            'Fio': 2200,
            'Poliester': 2200,
        }

    def get_stock(self, material):
        return self.stock_levels[self.number_to_material[material]]

    def nextday(self):
        self.date = self.date + timedelta(days=1)

    def order_point(self, material):
        if material not in self.material_to_number:
            return "Material desconhecido."
        
        orderPoint = round((self.daily_demand * self.delivery_time) + self.security_stock)
        return orderPoint
    
    def enconomic_order_quantity(self):
        return round(math.sqrt((2*self.anual_demand*self.order_cost)/self.posession_cost))
    
    
    def manage_order(self, order):

        for encomenda in order:
            item = encomenda['type']
            quantity = encomenda['qty']
            size = encomenda['size']
            flagcontinue = True
            quantityPerMaterial = dict()
            # agora tenho de mexer no meu inventário e chamar aquela porra toda 
            # ver também cada material para cada peça
            for key, value in self.clothing_sizes_material[self.tipos_dict[item]].items(): # vou ver cada material para cada peça
                material = key
                quantityPerItem = value * self.sizes_to_ratio[size]
                quantityPerMaterial[key] = round(quantityPerItem * quantity, 2)
                if(quantityPerMaterial[key] > self.stock_levels[material]):
                    print("NOT ENOUGH MATERIAL")
                    print('DENYING ORDER')
                    flagcontinue = False
                    
            if not flagcontinue:
               self.nextday()
               continue

            for key in quantityPerMaterial:
                print(f"{key}: {quantityPerMaterial[key]}")

                self.stock_levels[key] -= quantityPerMaterial[key]

                print(f"A quantidade de {material} que iremos necessitar para clothing item {self.tipos_dict[item]} será de {quantityPerMaterial}")


                if(self.stock_levels[material] <= self.order_point(material)):
                    # vou ter de chamar a cena do tomy  
                    pass
            
            self.nextday()


manager = StockManager()
print(manager.manage_order([{'type': 3, 'qty': 2, 'size': 4}]))

import math
import encomenda as enc
from datetime import date, timedelta



class StockManager:
    def __init__(self):
        self.initial_stock = 2200
        self.anual_demand = 50000
        self.order_cost = 10 # diferenciar com isto
        self.posession_cost = 0.7 # diferenciar com isto
        self.delivery_time = 7
        self.security_stock = 1000
        self.daily_demand = self.anual_demand/365

        self.date = date.today()

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


    def nextday(self):
        self.date = self.date + timedelta(days=1)

    def order_point(self, material):
        if material not in self.material_to_number:
            return "Material desconhecido."
        
        orderPoint = round(((self.daily_demand * self.delivery_time) + self.security_stock), 2)
        return orderPoint
    
    def economic_order_quantity(self):
        return round(math.sqrt((2*self.anual_demand*self.order_cost)/self.posession_cost), 2)
    
    def get_stock_levels(self):
        for key, value in self.stock_levels.items():
                print(f"Para o material {key} temos {value} m2")
    
    
    def manage_order(self, order):

        for encomenda in order:
            print('Sabendo que temos estes materiais')
            self.get_stock_levels()

            item = encomenda['type']
            quantity = encomenda['qty']
            size = encomenda['size']
            flagcontinue = True
            quantityPerMaterial = dict()
            
            for key, value in self.clothing_sizes_material[self.tipos_dict[item]].items(): # vou ver cada material para cada peça
                material = key
                quantityPerItem = value * self.sizes_to_ratio[size]
                quantityPerMaterial[key] = round(quantityPerItem * quantity, 2)


                if(quantityPerMaterial[key] > self.stock_levels[material]): # se fôssemos ficar com material negativo
                    print(f'nao há {material} suficiente ')
                    flagcontinue = False
                    break
                    
            if not flagcontinue:
               print("NOT ENOUGH MATERIAL")
               print('DENYING ORDER')
               self.nextday()
               continue

            materialsForOrder = list()

            for material in quantityPerMaterial:
                print(f"{material}: {quantityPerMaterial[material]}")

                self.stock_levels[material] -= quantityPerMaterial[material]

                print(f"A quantidade de {material} que iremos necessitar para clothing item {self.tipos_dict[item]} será de {quantityPerMaterial[material]}")


                if(self.stock_levels[material] <= self.order_point(material)): # temos de fazer order
                    order = {
                        'product': material,
                        'qty': self.economic_order_quantity()
                    }

                    materialsForOrder.append(order)

                    
            enc.create_order(materialsForOrder, self.date)
            
            
            self.nextday()


manager = StockManager()
manager.manage_order([{'type': 3, 'qty': 2000, 'size': 4}, {'type': 1, 'qty': 200, 'size': 2}])

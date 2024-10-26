class StockManager:
    def __init__(self):
        self.initial_stock = 2200
        self.anual_demand = 50000
        self.order_cost = 10
        self.posession_cost = 0.7
        self.delivery_time = 7
        self.security_stock = 1000

        self.material_to_number = {
            'Tecido': 0,
            'Algodao': 1,
            'Fio': 2,
            'Poliester': 3
        }

        self.clothing_sizes_price = {
            'Tshirt': {
                self.material_to_number['Tecido']: 1,
                self.material_to_number['Algodao']: 0.8,
                self.material_to_number['Fio']: 0.4,
                self.material_to_number['Poliester']: 1.3,
            },
            'Camisola': {
                self.material_to_number['Tecido']: 0.8,
                self.material_to_number['Algodao']: 0.7,
                self.material_to_number['Fio']: 0.4,
                self.material_to_number['Poliester']: 1.4,
            },
            'Calcoes': {
                self.material_to_number['Tecido']: 0.5,
                self.material_to_number['Algodao']: 0.35,
                self.material_to_number['Fio']: 0.5,
                self.material_to_number['Poliester']: 1.15,
            },
            'Calcas': {
                self.material_to_number['Tecido']: 1.2,
                self.material_to_number['Algodao']: 0.95,
                self.material_to_number['Fio']: 0.35,
                self.material_to_number['Poliester']: 1.5,
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

    def order_point(self, material):
        if material not in self.material_to_number:
            return "Material desconhecido."
        
        material_num = self.material_to_number[material]
        return f"Ponto de encomenda calculado para o material {material_num}"

manager = StockManager()
print(manager.order_point('Tecido'))

class Flowers:

    def __init__(self, title, colour, how_fresh, stem_length, cost):   # how_fresh - это сколько цветок простоит
        self.title = title
        self.colour = colour
        self.how_fresh = how_fresh
        self.stem_length = stem_length
        self.cost = cost


class Roses(Flowers):

    def __init__(self, title, colour, how_fresh, stem_length, cost, is_smell, is_thorn):
        super().__init__(title, colour, how_fresh, stem_length, cost)
        self.is_smell = is_smell
        self.is_thorn = is_thorn


class Сhamomiles(Flowers):
    def __init__(self, title, colour, how_fresh, stem_length, cost, how_petal):
        super().__init__(title, colour, how_fresh, stem_length, cost)
        self.how_petal = how_petal


class Lilies(Flowers):
    def __init__(self, title, colour, how_fresh, stem_length, cost, how_bud, variety):
        super().__init__(title, colour, how_fresh, stem_length, cost)
        self.how_bud = how_bud
        self.variety = variety


class Bouquet:

    def __init__(self, name):
        self.name = name
        self.list_of_flowers = []

    def add_flowers(self, flower):
        self.list_of_flowers.append(flower)

    def bouquet_cost(self):
        return f'Cтоимость {self.name}: {sum(flower.cost for flower in self.list_of_flowers)}'

    def days_of_live(self):
        return (f'{self.name} простоит '
                f'{round(sum(flower.how_fresh for flower in self.list_of_flowers) / len(self.list_of_flowers))} дней')

    def __str__(self):
        return f'{self.name} имеет: ' + ', '.join(f'{flower.title} {flower.colour}' for flower in self.list_of_flowers)

    def sort_fresh(self):
        self.list_of_flowers.sort(key=lambda flower: flower.how_fresh)

    def sort_cost(self):
        self.list_of_flowers.sort(key=lambda flower: flower.cost)

    def sort_stem(self):
        self.list_of_flowers.sort(key=lambda flower: flower.stem_length)

    def search_by_price(self, cost):
        for flower in self.list_of_flowers:
            if flower.cost == cost:
                print(f'{flower.title} {flower.colour}')


rose_1 = Roses('роза', 'красная', 5, 20, 130, True, True)
rose_2 = Roses('роза', 'розовая', 3, 15, 150, False, True)
rose_3 = Roses('роза', 'белая', 6, 22, 250, True, True)
chamomile_1 = Сhamomiles('ромашка', 'белая', 10, 18, 150, 20)
chamomile_2 = Сhamomiles('ромашка', 'белая', 12, 18, 170, 25)
chamomile_3 = Сhamomiles('ромашка', 'белая', 9, 17, 130, 18)
lily_1 = Lilies('лилия', 'белая', 9, 30, 300, 3, 'восточная')
lily_2 = Lilies('лилия', 'розовая', 12, 35, 350, 3, 'азиатская')
lily_3 = Lilies('лилия', 'белая', 14, 33, 330, 4, 'восточная')

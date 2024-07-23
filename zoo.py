"""
Classi:

1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.
2. Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: name, species, age,
 height, width, preferred_habitat, health che è uguale a round(100 * (1 / age), 3).
3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. I recinti possono 
contenere uno o più animali. I recinti possono hanno gli attributi area, temperature e habitat.
4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo.
 I guardiani dello zoo hanno un nome, un cognome, e un id. Essi possono nutrire gli animali, 
pulire i recinti e svolgere altri compiti nel nostro zoo virtuale.

Funzionalità:
1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): consente al guardiano dello zoo
 di aggiungere un nuovo animale allo zoo. L'animale deve essere collocato in un recinto adeguato 
in base alle esigenze del suo habitat e se c'è ancora spazio nel recinto, ovvero se l'area del recinto
 è ancora sufficiente per ospitare questo animale.

2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo di
 rimuovere un animale dallo zoo. L'animale deve essere allontanato dal suo recinto. 
Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.

3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano
 dello zoo di nutrire tutti gli animali dello zoo. Ogni volta che un animale viene nutrito, 
la sua salute incrementa di 1% rispetto alla sua salute corrente, ma le dimensioni dell'animale 
(height e width) vengono incrementate del 2%. Perciò, l'animale si può nutrire soltanto se il recinto
 ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.

4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello 
zoo di pulire tutti i recinti dello zoo. Questo metodo restituisce un valore di tipo 
float che indica il tempo che il guardiano impiega per pulire il recinto. Il tempo di pulizia è il 
rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0,
 restituire l'area occupata.

5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello 
zoo, sui recinti dello zoo che contengono animali. 

E.s.: Se abbiamo un guardiano chiamato Lorenzo Maggi con matricola 1234, e un recinto Fence
(area=100, temperature=25, habitat=Continentale) con due animali
 Animal(name=Scoiattolo, species=Blabla, age=25, ...), Animal(name=Lupo, species=Lupus, age=14,...)
   ci si aspetta di avere una rappresentazione testuale dello zoo             
   print(f"Non c'è abbastanza spazio nel recinto per nutrire l'animale {animal.name}.")0, temperature=25,
     habitat=Continent)

with animals:

Animal(name=Scoiattolo, species=Blabla, age=25)

Animal(name=Lupo, species=Lupus, age=14)
#########################

Fra un recinto e l'altro mettete 30 volte il carattere #.
"""

class Zoo:
    def __init__(self, fence=None, zoo_keeper=None):
        if fence is None:
            fence = []
        else:
            self.fences = fence

        if zoo_keeper is None:
            zoo_keeper = []
        else:
            self.zoo_keepers = zoo_keeper

    def add_animal(self, animal, fence):
        if fence.area >= animal.width and fence.has_space():
            fence.add_animal(animal)
        else:
            print(f"Non c'è abbastanza spazio nel recinto per aggiungere l'animale {animal.name}.")

    def remove_animal(self, animal, fence):
        fence.remove_animal(animal)

    def feed(self):
        for fence in self.fences:
            fence.feed_animals()

    def clean(self):
        total_cleaning_time = 0.0
        for fence in self.fences:
            cleaning_time = fence.clean()
            total_cleaning_time += cleaning_time
        return total_cleaning_time

    def describe_zoo(self):
        print("Guardiani dello zoo:")
        for zoo_keeper in self.zoo_keepers:
            print(f"Nome: {zoo_keeper.name}, Cognome: {zoo_keeper.surname}, ID: {zoo_keeper.id}")
        print("Recinti dello zoo:")
        for fence in self.fences:
            print(f"Recinto - Area: {fence.area}, Temperatura: {fence.temperature}, Habitat: {fence.habitat}")
            print("Animali nel recinto:")
            for animal in fence.animals:
                print(f"Nome: {animal.name}, Specie: {animal.species}, Età: {animal.age}")
            print("#" * 30)

class Animal:
    def __init__(self, name:str, species:str, age:int, height:float, width:float, preferred_habitat:str
                 , health:float):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = (round(100 * (1 / age), 3))

class Fence:
    def __init__(self, area, temperature, habitat):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []

    def has_space(self):
        total_width = sum(animal.width for animal in self.animals)
        return total_width < self.area

    def add_animal(self, animal):
        if self.has_space():
            self.animals.append(animal)
        else:
            print(f"Non c'è abbastanza spazio nel recinto per aggiungere l'animale {animal.name}.")

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def feed_animals(self):
        for animal in self.animals:
            if self.has_space():
                animal.health += 1
                animal.height += 2
            else:
                print(f"Non c'è abbastanza spazio nel recinto per nutrire l'animale {animal.name}.")

    def clean(self):
        occupied_area = sum(animal.width for animal in self.animals)
        remaining_area = self.area - occupied_area
        if remaining_area == 0:
            return occupied_area
        else:
            return occupied_area / remaining_area

class ZooKeeper:
    def __init__(self, name:str, surname:str, id:int):
        self.name = name
        self.surname = surname
        self.id = id




continent_fence = Fence(100, 25, 'Continentale')
lorenzo = ZooKeeper('Marin', 'Dodi', '1234')
zoo = Zoo(fence=[continent_fence], zoo_keeper=[lorenzo])
zoo.fences.append(continent_fence)
scoiattolo = Animal('Scoiattolo', 'Blabla', 25, 0.5, 0.3, 'Continentale', round(100 * (1 / 25), 3))
lupo = Animal('Lupo', 'Lupus', 14, 1.5, 0.8, 'Continentale', round(100 * (1 / 14), 3))
continent_fence.animals.extend([scoiattolo, lupo])

# Visualizza informazioni sullo zoo
if __name__ == "__main__":
    zoo.describe_zoo()
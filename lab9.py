class Tomato:
    states = {"отсутствует", "цветение", "зеленый", "красный"}

    def __init__(self, index):
        self._index = index
        self._state = next(iter(self.states))

    def grow(self):
        current_index = list(self.states).index(self._state)
        if current_index < len(self.states) - 1:
            self._state = list(self.states)[current_index + 1]

    def is_ripe(self):
        return self._state == "красный"


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(index) for index in range(1, num_tomatoes + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print(f"{self.name} собрал урожай!")
            self._plant.give_away_all()
        else:
            print("Подождите, пока все плоды созреют!")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:")
        print("- Помидоры проходят через несколько стадий созревания: от отсутствия до красного.")
        print("- Садовник может ухаживать за растением, заставлять его расти и собирать урожай.")


# Тесты
if __name__ == "__main__":
    Gardener.knowledge_base()

    bush = TomatoBush(5)
    gardener = Gardener("Иван", bush)

    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()

    gardener.harvest()
    gardener.work()
    gardener.harvest()

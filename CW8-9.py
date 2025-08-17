from abc import ABC, abstractmethod


class BodyPart(ABC):
    @abstractmethod
    def function(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}: {self.function()}"


class Brain(BodyPart):
    def function(self):
        return "Body's control center"


class Heart(BodyPart):
    def function(self):
        return "he heart's primary function is to act as a pump, circulating blood throughout the body."


class Lung(BodyPart):
    def function(self):
        return "The breathing apparatus works without problems."


class Spine(BodyPart):
    def function(self):
        return "The skeleton is excellent."


class NerveFibers(BodyPart):
    def function(self):
        return "There is a connection between the brain and the body's organs."


class Eye(BodyPart):
    def function(self):
        return "The visual system is working properly."


class Liver(BodyPart):
    def function(self):
        return "Blood purification is done properly."


class HumanBody:
    def __init__(self):
        self.part_of_body = []

    def call_function(self, part):
        # if isinstance(part, BodyPart):
        self.part_of_body.append(part)
        # else:
        #     raise ValueError("This body part is not in my dictionary.")

    def show_function(self):
        for part in self.part_of_body:
            print(part)


brain = Brain()
heart = Heart()
lung = Lung()
spin = Spine()
nerve_fibers = NerveFibers()
eye = Eye()
liver = Liver()

human = HumanBody()
human.call_function(brain)
human.call_function(heart)
human.call_function(lung)
human.call_function(nerve_fibers)
human.call_function(eye)
print('----List of parts & How it works----')

human.show_function()

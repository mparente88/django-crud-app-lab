from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class Oc:
    def __init__(self, name, age, likes, dislikes, description):
        self.name = name
        self.age = age
        self.likes = likes
        self.dislikes = dislikes
        self.description = description

ocs = [
    Oc('Claude', '18', 'Sauteed Jerky', 'Blue Cheese', 'Claude is a playable character and one of the main protagonists in Fire Emblem: Three Houses.'),
    Oc('Hilda', '19', 'Saghert and Cream', 'Training Weight', 'Hilda possesses a minor Crest of Goneril and is 18 at the start of the game.'),
    Oc('Petra', '15', 'Exotic Feathers', 'Fried Crayfish', 'Petra hails from Brigid, a vassal state of the Adrestian Empire.'),
]

def oc_index(request):
    return render(request, 'ocs/index.html', {'ocs': ocs})
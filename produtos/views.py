from django.shortcuts import render

def listagem_produtos(request):
    context = {
        'produtos': [
            {'Nome': 'Uva', 'Preco': 1}, 
            {'Nome': 'Melancia', 'Preco': 2},
            {'Nome': 'Banana', 'Preco': 3}
            ]
    }
    return render(request, 'templates/listagem_produtos.html',context)
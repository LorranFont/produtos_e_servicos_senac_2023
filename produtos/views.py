from django.shortcuts import render

def listagem_produtos(request):
    produtos_dos_vendedores = [{

        'vendedor': {'nome': 'Lorran'},
        'produtos': [
            {'nome': 'Uva', 'preco': 1}, 
            {'nome': 'Melancia', 'preco': 2},
            {'nome': 'Banana', 'preco': 3},
            ]
    },
    {
        'vendedor': {'nome': 'Jefferson'},
        'produtos': [
            {'nome': 'Goiaba', 'preco': 3}, 
            
            ]
    }]
    context = {'produtos_dos_vendedores': produtos_dos_vendedores}
    return render(request, 'templates/listagem_produtos.html',context)
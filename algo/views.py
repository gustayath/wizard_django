from django.shortcuts import render, redirect
from .models import Inscricao


def view_dados_pessoais(request):
    if request.method == "POST":
        request.session['Inscricao'] = {
            'nome': request.POST.get('nome'),
            'email': request.POST.get('email'),
            'celular': request.POST.get('celular'),
            'data_nascimento': request.POST.get('data_nascimento'),
        }

        print("Sessão Atual:", request.session.get('Inscricao'))

        return redirect('planos')

    return render(request, 'template_1/index.html')


def view_escolha_plano(request):
    if request.method == "POST":
        inscricao = request.session.get('Inscricao', {})

        inscricao['plano'] = request.POST.get('plano')

        request.session['Inscricao'] = inscricao

        print("Sessão Atual:", request.session.get('Inscricao'))

        return redirect('finalizar_plano')

    return render(request, 'template_2/index.html')


def view_finalizar_plano(request):
    inscricao = request.session.get('Inscricao')

    if not inscricao:
        return redirect('dados_pessoais')

    if request.method == "POST":

        Inscricao.objects.create(
            nome=inscricao.get('nome'),
            email=inscricao.get('email'),
            celular=inscricao.get('celular'),
            data_nascimento=inscricao.get('data_nascimento'),
            plano=inscricao.get('plano'),
            finalizado=True
        )

        print("Inscrição salva no banco:", inscricao)

        # Limpa a sessão depois de salvar no banco
        request.session.flush()

        return render(
            request,
            'template_3/index.html',
            {
                'finalizado': True
            }
        )

    return render(
        request,
        'template_3/index.html',
        {
            'inscricao': inscricao
        }
    )
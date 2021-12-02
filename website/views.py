from django.shortcuts import render
from . import scripts

def home(request):
	if request.method == "POST":
		valorselecao = request.POST['valorselecao']
		areatexto = request.POST['areatexto']

		if valorselecao == '1':
			resultado = scripts.shuffler(areatexto)
		elif valorselecao == '2':
			resultado = scripts.enthalpy(areatexto)
		elif valorselecao == '3':
			resultado = scripts.entropy(areatexto)
		elif valorselecao == '4':
			resultado = scripts.stability(areatexto)
		elif valorselecao == '5':
			resultado = scripts.stacking(areatexto)

		return render(request, 'resultados.html', {'resultado':resultado})
	else:
		return render(request,'home.html',{})


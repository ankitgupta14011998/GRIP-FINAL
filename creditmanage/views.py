from django.shortcuts import render,get_object_or_404
from .models import people,transaction
from django.utils import timezone

def index(request):
	return render(request, 'creditmanage/home.html',{
		'user': []
		})

def users(request):
	return render(request, 'creditmanage/home.html',{
		'user': people.objects.all()
		})

def profile(request,pk):
	name=people.objects.get(pk=pk)
	if(request.method=='POST'):
		cred=int(request.POST["credit"])
		tran=people.objects.get(pk=int(request.POST["trans"]))
		name.credit = name.credit - cred
		tran.credit = tran.credit + cred
		e = transaction(Sender=name,Receiver=tran,Credit_Amount=cred,Date=timezone.now(),Senderbalance=name.credit,Receiverbalance=tran.credit)
		e.save()
		name.save()
		tran.save()
		return render(request, 'creditmanage/profile.html',{
			'name': name,
			'people':people.objects.all(),
			'message': "Transaction Successfull!"
			})
	else:
		return render(request, 'creditmanage/profile.html',{
			'name': people.objects.get(pk=pk),
			'people':people.objects.all()
			})

def viewtransactions(request):
	return render(request, 'creditmanage/transactions.html',{
		'lists': transaction.objects.all().order_by('-Date')
		})

def viewpassbook(request,pk):
	entry=[]
	name=people.objects.get(pk=int(pk))
	lists=transaction.objects.all().order_by('-Date')
	for list in lists:
		if list.Sender == name or list.Receiver == name:
			entry.append(list)
	return render(request, 'creditmanage/viewpassbook.html',{
		'name': name,
		'entries': entry
		})

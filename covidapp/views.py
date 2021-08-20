from django.shortcuts import render

import requests
import json
url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "6d3c9e4c3bmsh16a41ada072baa8p182dafjsncdf82bdab138",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

def helloworldview(request):
	n_results=int(response['results'])
	country=[]
	for i in range(0,n_results):
		country.append(response['response'][i]['country'])

	if request.method=='POST':
		selectedCountry= request.POST['selectedcountry']
		# print(selectedCountry)
		for x in range(0,n_results):
			data=response['response'][x]
			if selectedCountry==data['country']:
				# print(data['cases'])
				cases=data['cases']
				new=cases['new']
				active=cases['active']
				critical=cases['critical']
				recovered=cases['recovered']
				total=cases['total']
				deaths=int(total)-int(active)-int(recovered)
		context={'selectedcountry':selectedCountry, 'country':country, 'new':new, 'active':active, 'critical':critical, 'recovered':recovered, 'total':total, 'deaths':deaths}
		return render(request,'helloworld.html',context)

	
	
	context={'country' : country}
	return render(request,'helloworld.html',context)


import re
import whois
from django.db.models import Count
from django.shortcuts import render, redirect
from .models import *
import requests
from django.views.generic import *

def whois_info(request):
    if request.method == 'POST':
        domain_name = request.POST.get('domain_name')
        if not domain_name:
            return render(request, 'whois/whois_check.html', {'error_message': 'Please enter a domain name or URL'})

        # Validate domain name or URL
        if not re.match(r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$',
                        domain_name) and not re.match(
                r'^https?://[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.[a-zA-Z]{2,}', domain_name):
            return render(request, 'whois/whois_check.html', {'error_message': 'Please enter a valid domain name or URL'})

        # Extract domain name from URL
        if re.match(r'^https?://[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.[a-zA-Z]{2,}', domain_name):
            domain_name = \
            re.findall(r'^https?://([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.[a-zA-Z]{2,})', domain_name)[0]

        # Check if the domain already exists in the database
        existing_domain = SearchTerm.objects.filter(keywords=domain_name).first()
        if existing_domain:
            # If it does, update the search count
            existing_domain.count += 1
            existing_domain.save()
        else:
            # If it doesn't, create a new domain with a search count of 1
            new_domain = SearchTerm(keywords=domain_name, count=1)
            new_domain.save()
        try:
            w = whois.whois(domain_name)
            whois_info = {
                'domain_name': w.domain_name,
                'creation_date': w.creation_date,
                'expiration_date': w.expiration_date,
                'registrar': w.registrar,
                'name_servers': w.name_servers,
                'status': w.status,
                'emails': w.emails,
                'updated_date': w.updated_date,
                'name': w.name,
                'org': w.org,
                'address': w.address,
                'city': w.city,
                'state': w.state,
                'zipcode': w.zipcode,
                'country': w.country
            }
            context = {
                'whois_info': whois_info
            }
            return render(request, 'whois/result.html', context)
        except Exception as e:
            return render(request, 'whois/whois_check.html',
                          {'error_message': 'Error retrieving whois information: {}'.format(str(e))})
    else:
        return redirect('/')



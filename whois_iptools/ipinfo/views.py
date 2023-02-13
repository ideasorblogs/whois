from django.shortcuts import render
import re
import requests


def ip_result(request):
    data = {}
    error = None
    ip_address = request.POST.get('ip_address')

    if not ip_address:
        # Get client's IP address
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
        if ip_address:
            ip_address = ip_address.split(',')[0]
        else:
            ip_address = request.META.get('REMOTE_ADDR', '')
    else:
        # Validate user-entered IP address
        ip_address = ip_address.strip()
        pattern = re.compile(
            r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
        if not pattern.match(ip_address):
            error = "Invalid IP address"
            return render(request, 'ipinfo/ipinfo.html', {'error': error})

    if ip_address:
        # Make API request to retrieve IP address details
        response = requests.get(f"https://ipapi.co/{ip_address}/json/")

        if response.status_code == 200:
            response_data = response.json()
            data = {
                'ip_address': response_data.get('ip'),
                'city': response_data.get('city'),
                'region': response_data.get('region_name'),
                'country_code': response_data.get('country_code'),
                'country_name': response_data.get('country_name'),
                'latitude': response_data.get('latitude'),
                'longitude': response_data.get('longitude'),
                'time_zone': response_data.get('time_zone'),
                'currency': response_data.get('currency')
            }
        else:
            error = "Failed to retrieve IP address details"
    else:
        error = "No IP address provided"

    return render(request, 'ipinfo/ipinfo.html', {'data': data, 'error': error})



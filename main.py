import whois

domain = "ideasorblogs.in"
raw = whois.whois(domain).text

parsed = whois.parser.parse(raw)

print(parsed)

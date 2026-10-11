sites = """
https://example.com/home?id=1&user=admin
http://test.org/about?page=3&ref=google
https://mysite.net/contact?lang=en&token=abc123
http://sample.co/products?id=1&page=3
https://website.edu/services?ref=google&lang=en
http://example.com/api/data?token=abc123&user=admin
https://test.org/home?ref=google&id=1
http://mysite.net/contact?page=3&lang=en
https://sample.co/services?token=abc123&user=admin
http://website.edu/about?id=1&ref=google
https://example.com/api/data?user=admin&lang=en
http://test.org/services?page=3&token=abc123
https://mysite.net/home?id=1&ref=google
http://sample.co/contact?user=admin&token=abc123
https://website.edu/products?lang=en&ref=google
"""

sites_list = sites.split("\n")
https_sites = []
http_count = 0
https_count = 0
for site in sites_list:
    if "https" in site:
        https_count +=1
        https_sites.append(site)
    elif ("http") in site:
        http_count += 1



print(f" http : {http_count} , https : {https_count}")
print(https_sites)

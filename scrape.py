import urllib.request
import re
import csv
import ast

# URLS go here #
urls = [  ]

array = []

for url in urls:
    request = urllib.request.urlopen(url)
    page = request.read().decode()

    # fixes a field missing quotes
    pageFixed = page.replace("accordionTitle", "'accordionTitle'")

    # finds all substrings that start "dataLayer.push({" and end "})"
    for r in re.findall(r"dataLayer.push\({(.*?)}\)", pageFixed):
        # ignore any that start with a "&"
        if (r[0] != '&'):
            loneObject = ast.literal_eval('{' + r +'}')
            array.append(loneObject)


fieldNames = ['event', 'site_category', 'property_name', 'property_location', 'form_name', 'accordion_category', 'button_name', 'article_name', 'link_name', 'product_name']

with open('datalayer.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldNames)
    writer.writeheader()
    writer.writerows(array)

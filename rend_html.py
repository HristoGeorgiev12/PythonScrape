from requests_html import HTMLSession
import json
url  = 'https://shop.mango.com/gb/women/skirts-midi/midi-satin-skirt_17042020.html?c=99'

s = HTMLSession()
r = s.get(url)

r.html.render(sleep = 1)

product  = r.html.find('.product-actions')
# product  = r.html.xpath('//*[@id="app"]/main/div/div[3]/div[1]/div[1]/h1', first = True)
name  = r.html.find('.product-name', first = True)
price  = r.html.find('.product-sale', first = True)
color  = r.html.find('.colors-info' , first = True)
sizes_all  = r.html.find('.selector-list span')

sizes = list()
for size in sizes_all:
    sizes.append(size.text)

json_dict = {
  "name": str(name.text),
  "price": float(price.text.replace('£', '')),
  "color": str(color.text),
  "size": list(sizes)
}


print(json_dict)

with open('data.json', 'w') as outfile:
    json.dump(json_dict, outfile, indent=4, sort_keys=True)
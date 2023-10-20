import xml.dom.minidom as minodom

xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

dom = minodom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
currency_data = []

SUM_valute = 0.0

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == "Value":
                currency_data.append(child.firstChild.data)

for i in range(len(currency_data)):
    SUM_valute += float(currency_data[i].replace(',', '.'))

Average_indicatr_value = SUM_valute/float(len(currency_data))

print(SUM_valute)
print(len(currency_data))
print(Average_indicatr_value)




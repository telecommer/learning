import xml.dom.minidom
xmlString = '''<server><pool>http</pool><description>My virtual server test</description><name>http-virtual</name><mask>255.255.255.255</mask><profiles>  <name>http</name><kind>ltm:virtual:profile</kind> </profiles><profiles><name>tcp</name><kind>ltm:virtual:profile</kind> </profiles><ipProtocol>tcp</ipProtocol><sourceAddressTranslation> <type>automap</type><kind>tm:ltm:virtual:virtualstate</kind><destination>1.1.1.3:80</destination></sourceAddressTranslation> </server>'''
dom = xml.dom.minidom.parseString(xmlString)
xml = dom.toprettyxml()
print(xml)
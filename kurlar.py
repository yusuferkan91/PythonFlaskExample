import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json


class Kurlar():
    def __init__(self):
        pass

    def update(self):
        url = "http://www.tcmb.gov.tr/kurlar/today.xml"
        tree = ET.parse(urlopen(url))
        root = tree.getroot()
        dictionary = {}
        Kur_Liste = {}
        for kur in root.findall('Currency'):
            Kod = kur.get('Kod')
            Unit = kur.find('Unit').text
            isim = kur.find('Isim').text
            CurrencyName = kur.find('CurrencyName').text
            ForexBuying = kur.find('ForexBuying').text
            ForexSelling = kur.find('ForexSelling').text
            BanknoteBuying = kur.find('BanknoteBuying').text
            BanknoteSelling = kur.find('BanknoteSelling').text
            CrossRateUSD = kur.find('CrossRateUSD').text
            Kur_Liste[Kod] = isim
            dictionary[Kod] = {
                "Kod": Kod,
                "İsim": isim,
                "Kur_İsmi": CurrencyName,
                "Birim": Unit,
                "Alış": ForexBuying,
                "Satış": ForexSelling,
                "Efektif_alış": BanknoteBuying,
                "Efektif_satış": BanknoteSelling,
                "Birim_USD_Değeri": CrossRateUSD
            }
        return dictionary, Kur_Liste

    def get_json(self):
        data, _ = self.update()
        json_object = json.dumps(data, ensure_ascii=False).encode('utf8')
        return json_object.decode()

    def get_dictionary(self):
        data, _ = self.update()
        return data

    def get_list(self):
        _, kur_list = self.update()
        return kur_list


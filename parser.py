from bs4 import BeautifulSoup

class Parser:
    def __init__(self, content):
        self.soup = BeautifulSoup(content, "html.parser")

    def get_ads(self):
        extracted_ads = []
        ads = self.__get_ads()
        for ad in ads:
            extracted_ads.append({
                'title': self.__get_title(ad),
            })

        return extracted_ads

    def __get_ads(self):
        return self.soup.findAll('li', {'class': '_3DFQ-'})

    def __get_title(self, ad):
        title_section = ad.find('section', {'class': '_2EDA9'})
        title = title_section.find('span').text

        return title
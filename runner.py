# 1)Написать приложение, которое будет проходиться по указанному списку двух
#    и/или более пользователей и собирать данные об их подписчиках и подписках.
# 2) По каждому пользователю, который является подписчиком или на которого
#    подписан исследуемый объект нужно извлечь имя, id, фото (остальные данные по желанию).
#    Фото можно дополнительно скачать.
# 3) Собранные данные необходимо сложить в базу данных.
#     Структуру данных нужно заранее продумать, чтобы:
# 4) Написать запрос к базе, который вернет список подписчиков только указанного пользователя
# 5) Написать запрос к базе, который вернет список профилей, на кого подписан указанный пользователь

from scrapy.crawler import CrawlerProcess                     # Импорт класса для создания процесса
from scrapy.settings import Settings                          # Импорт класса для настроек

from instaparser import settings                              # Настройки
from instaparser.spiders.instagram import InstagramSpider     # Класс паука
from pymongo import MongoClient
from pprint import pprint


client = MongoClient('localhost', 27017)
mongo_base = client.instagram
collection = mongo_base['instagram']

if __name__ == '__main__':
    crawler_settings = Settings()                             # Создание объекта с настройками
    crawler_settings.setmodule(settings)                      # Привязка к настройкам
    process = CrawlerProcess(settings=crawler_settings)       # Создание объекта процесса для работы
    process.crawl(InstagramSpider)                            # Добавление паука
    process.start()                                           # Пуск

for item in collection.find({}):
    pprint(item)
print(f'Всего в базе данных {collection.count_documents({})} записи')
#collection.drop()  # удаление БД для очистки памяти
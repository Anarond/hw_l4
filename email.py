import datetime

# 1. Создайте словарь email
email5 = {
    "subject": "Project collaboration",
    "from": " partner@organization.org ",
    "to": "  lead_dev@icloud.com ",
    "body": "Hello,\nWe are interested in a partnership.\tPlease reply soon.\nRegards,\nTeam",
}

# 2. Добавьте дату отправки: создайте переменную send_date как текущую дату в формате YYYY-MM-DD и запишите её в email["date"].
send_date = datetime.datetime.now().strftime("%Y-%m-%d")
email5["date"] = send_date
print(email5["date"])

# 3. Нормализуйте e-mail адреса отправителя и получателя: приведите к нижнему регистру и уберите пробелы по краям.
# Запишите обратно в email["from"] и email["to"].
email5["from"] = email5["from"].strip().lower()
email5["to"] = email5["to"].strip().lower()
print(email5["from"])
print(email5["to"])

# 4. Извлеките логин и домен отправителя в две переменные login и domain.
login = email5["from"].split("@")[0]
domain = email5["from"].split("@")[1]
print(login)
print(domain)

# 5. Создайте сокращённую версию текста: возьмите первые 10 символов email["body"] и добавьте многоточие "...".
# Сохраните в новый ключ словаря: email["short_body"].
short_body = email5["body"][:10] + "..."
email5["short_body"] = short_body
print(email5["short_body"])

# 6. Списки доменов: создайте список личных доменов
# ['gmail.com','list.ru', 'yahoo.com','outlook.com','hotmail.com','icloud.com','yandex.ru','mail.ru','list.ru','bk.ru','inbox.ru']
# и список корпоративных доменов
# ['company.ru','corporation.com','university.edu','organization.org','company.ru', 'business.net']. с учетом того что там должны быть только уникальные значение
personal_domains = [
    "gmail.com",
    "list.ru",
    "yahoo.com",
    "outlook.com",
    "hotmail.com",
    "icloud.com",
    "yandex.ru",
    "mail.ru",
    "list.ru",
    "bk.ru",
    "inbox.ru",
]
corporate_domains = [
    "company.ru",
    "corporation.com",
    "university.edu",
    "organization.org",
    "company.ru",
    "business.net",
]
print(personal_domains)
print(corporate_domains)

# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений: ни один домен не должен входить в оба списка одновременно.
personal_domains = set(personal_domains)
corporate_domains = set(corporate_domains)
print(personal_domains)
print(corporate_domains)

# 8. Проверьте «корпоративность» отправителя: создайте булеву переменную is_corporate, равную результату проверки вхождения домена отправителя в список корпоративных доменов.
is_corporate = domain in corporate_domains
print(is_corporate)

# 9. Соберите «чистый» текст сообщения без табов и переводов строк: замените "\t" и "\n" на пробел.
# Сохраните в email["clean_body"].
clean_body = email5["body"].replace("\t", " ").replace("\n", " ")
email5["clean_body"] = clean_body
print(email5["clean_body"])

# 10. Сформируйте текст отправленного письма многострочной f-строкой и сохраните в email["sent_text"]:
# Кому: {получатель}, от {отправитель} Тема: {тема письма}, дата {дата} {чистый текст сообщения}
sent_text = (
    f"Кому: {email5['to']}, от {email5['from']}\n"
    f"Тема: {email5['subject']}, дата {email5['date']} {email5['clean_body']}"
)
print(sent_text)

# 11. Рассчитайте количество страниц печати для email["sent_text"], если на 1 страницу помещается 500 символов.
# Сохраните результат в переменную pages. Значение должно быть округленно в большую сторону.
pages = (len(sent_text) + 499) // 500
print(pages)

# 12. Проверьте пустоту темы и тела письма: создайте переменные is_subject_empty, is_body_empty в котором будет хранится что тема письма содержит данные.
is_subject_empty = email5["subject"] == ""
is_body_empty = email5["body"] == ""
print(is_subject_empty)
print(is_body_empty)

# 13. Создайте «маску» e-mail отправителя: первые 2 символа логина + "***@" + домен.
# Запишите в email["masked_from"].
masked_from = login[:2] + "***@" + domain
print(masked_from)

# 14. Удалите из списка личных доменов значения "list.ru" и "bk.ru".
personal_domains.remove("list.ru")
personal_domains.remove("bk.ru")
print(personal_domains)

# В конце файла сделайте print(...) ключевых результатов для быстрой проверки, например:
# print(email) и print(is_corporate, pages, is_subject_empty, is_body_empty)
print(email5)
print(is_corporate, pages, is_subject_empty, is_body_empty)

def domain_name(url):
    # Если в строке есть "//" отбрасываем его и что до него
    if "//" in url:
        url = url.split("//")[1]

    parts = url.split(".")

    for part in parts:

        # 1й элемент либо www либо нужная часть строки
        if part != "www":
            return part

# urls = ["http://github.com/carbonfive/raygun",
#         "http://www.zombie-bites.com",
#         "https://www.cnet.com",
#         "www.xakep.ru",
#         "https://youtube.com"]
#
# for url in urls:
#     print(domain_name(url))


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
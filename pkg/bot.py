import time
import facebook as fb
from pic import image

acess_token = "EAAGiBDIF5b8BAGoa49ipyBkKONdFr8ZBcpkKog9NZCu8hnjcPDGV1lPHW9MwuxLDOeatncCwFNoKGA8ZAJevJ8jceKnYzO12TlsuxUaCmsQYhKZAV8MuBTvK1UXZCQVVuu2ueCHsEDMhqvG4UA6PVo650ZBa6qJJ0KteZBofZARYTLWbk5VLzmvhE2SweiZAIzfI0lAG7FZC3CmYA5eWWlOFiK"

y = fb.GraphAPI(acess_token)
while True:
    image()
    y.put_photo(open("pic.jpg","rb") ,message="Quotes__")
    #uploads a image after an hour
    time.sleep(3600)


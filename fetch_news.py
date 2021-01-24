import requests
NewsAPIKey= "EnterYourAPIKeyHere"
def NewsTechcrunch():
    main_url= "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=" + NewsAPIKey
    open_techcrunch = requests.get(main_url).json() #fetching data in json format
    article = open_techcrunch["articles"] # getting all articles in a string article
    
    NewsResults = [] #empty list which will contain all trending news
    
    for ar in article:
        NewsResults.append(ar["title"])
    for i in range(len(NewsResults)):
        print(i+1, NewsResults[i]) # print all trending news
    
NewsTechcrunch() # call the NewsTechcrunch function

#run now
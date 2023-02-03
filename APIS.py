import requests

#currency
currencyurl="https://free.currconv.com/api/v7/currencies?apiKey=2f227f1d2025329debdf"
reponse=requests.get(currencyurl)
listeall=list(reponse.json()['results'].keys())
def currency(new,old):
    url = "https://free.currconv.com/api/v7/convert?q="+new+"_"+old+"&compact=ultra&apiKey=2f227f1d2025329debdf"
    return requests.get(url).json()[new+'_'+old]




#Location
def location(place,city):
    locurl='https://eu1.locationiq.com/v1/search.php?key=c318b44abac072&q='+str(place)+' '+str(city)+' lebanon&format=json'
    return requests.get(locurl).json()

def staticmap(latlong):
    imgsrc='https://maps.locationiq.com/v2/staticmap?key=c318b44abac072&zoom=14&markers=icon:small-red-cutout'+latlong
    return requests.get(imgsrc)
    


#NEWS
def nynews(date):
    newsurl="https://api.nytimes.com/svc/search/v2/articlesearch.json?q=lebanon&begin_date="+date+"&sort=newest&api-key=e7hCh3j1NkI8ADDTeOptAWdoA8f8bTHG"
    return requests.get(newsurl).json()#['response']['docs']



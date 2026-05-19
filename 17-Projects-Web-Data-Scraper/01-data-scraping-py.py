import requests
from bs4 import BeautifulSoup
import pandas as pd

#Step-1:Fetch webpage content
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
req = requests.get(url)
#print(req)#check xem laptop da ket noi thanh cong voi link url chua

#Step-2 Parse with BeautifulSoup
soup = BeautifulSoup(req.text, "html.parser")

#Step-3 Extracting Data
titles = [item.text.strip()for item in soup.find_all("a", class_="title")]
prices = [item.text.strip()for item in soup.find_all("h4", class_="price float-end card-title pull-right")]
descriptions = [item.text.strip()for item in soup.find_all("p", class_="description card-text")]
roOfReviews = [item.text.strip()for item in soup.find_all("p", class_="review-count float-end")]

#Step-4 Storing Data in Dataframe
# pd = pd.DataFrame({
#     "Title": titles,
#     "Description": descriptions,
#     "Price": prices,
#     "Review": roOfReviews
# })

df = pd.DataFrame({
    "Title": titles,
    "Description": descriptions,
    "Price": prices,
    "Review": roOfReviews
})

df.to_excel("Laptops_data.xlsx", index = False)
print("data has been safe successfully.!")


# %% [markdown]
# ___
# 
# <a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by Pierian Data</em></center>

# %% [markdown]
# # Web Scraping Exercises 
# 
# ## Complete the Tasks Below

# %% [markdown]
# **TASK: Import any libraries you think you'll need to scrape a website.**

# %%
# CODE HERE

import requests, lxml, bs4

# %% [markdown]
# **TASK: Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ and get the HMTL text from the homepage.**

# %%
# CODE HERE

my_page = requests.get("http://quotes.toscrape.com/")

soup = bs4.BeautifulSoup(my_page.text, "lxml")

# %% [markdown]
# **TASK: Get the names of all the authors on the first page.**

# %%
# CODE HERE

# Apply the getText function to all items with the .author class in the html of the webpage
authors_mapping = map(bs4.element.Tag.getText, soup.select(".author"))

# Then cast it into a set to only get the unique values
authors = set(authors_mapping)

# %% [markdown]
# **TASK: Create a list of all the quotes on the first page.**

# %%
#CODE HERE

# %%

quote_info = soup.select(".text")
quotes = []

for quote in quote_info:
    quotes.append(quote.getText())


# %% [markdown]
# **TASK: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top right from the home page (e.g Love,Inspirational,Life, etc...). HINT: Keep in mind there are also tags underneath each quote, try to find a class only present in the top right tags, perhaps check the span.**

# %%

top_tags_info = soup.select("span .tag")

top_tags = list(map(bs4.element.Tag.getText, top_tags_info))

# %%


# %% [markdown]
# **TASK: Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/. Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors on the website. Keep in mind there are many ways to achieve this, also note that you will need to somehow figure out how to check that your loop is on the last page with quotes. For debugging purposes, I will let you know that there are only 10 pages, so the last page is http://quotes.toscrape.com/page/10/, but try to create a loop that is robust enough that it wouldn't matter to know the amount of pages beforehand, perhaps use try/except for this, its up to you!**

# %%

# First find what an empty page looks like so that we can check when we get there.
# The 2nd element of the col-md-8 class says "no quotes found" if the page is empty

# Go to a very high number to make sure it's an empty page
empty_page_req = requests.get("http://quotes.toscrape.com/page/1000/")
empty_soup = bs4.BeautifulSoup(empty_page_req.text, "lxml")

# Store the empty page quote to compare it later
empty_page_quote = empty_soup.select(".col-md-8")[1].getText() 


# %%

# Now actually look for the info

# Initialize a general url without the webpage
url = "http://quotes.toscrape.com/page/"
authors = []

n = 1

# Loop through all pages, will break out manually when finding an empty page
while True:

    # Get the nth page
    req = requests.get(url + str(n) + '/')
    soup = bs4.BeautifulSoup(req.text, "lxml")

    # Check if the page is empty and, in such case, break out of the loop
    if soup.select(".col-md-8")[1].getText() == empty_page_quote:
        break

    # Add the authors of the nth page
    authors.extend(list(map(bs4.element.Tag.getText, soup.select(".author"))))

    # Move to next page
    n += 1

# Cast it into a set to have only unique values
print(set(authors))

# %% [markdown]
# There are lots of other potential solutions that are even more robust and flexible, the main idea is the same though, use a while loop to cycle through potential pages and have a break condition based on the invalid page.



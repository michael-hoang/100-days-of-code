# Create an Automated Amazon Price Tracker
100 Days of Code

## Step 1 - Use BeautifulSoup to Scrape the Product Price
1. Find a product on Amazon that you want to track and get the product URL or just use the one I'm tracking.

https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463

<img src="https://img-c.udemycdn.com/redactor/raw/2020-08-17_11-08-29-1a29e3ccc29320c315fceef87117cc45.png" width="500">

In addition to the URL, when you browser tries to load up a page in Amazon, it also passes a bunch of other information. e.g. Which browser you're using, which computer you have etc.

These additional pieces of information is passed along in the request Headers.

You can see your browser headers by going to this website:

http://myhttpheader.com/

2. Use the requests library to request the HTML page of the Amazon product using the URL you got from 1.

HINT 1: You'll need to pass along some headers in order for the request to return the actual website HTML. At minimum you'll need to give your "User-Agent" and "Accept-Language" values in the request header.

<img src="https://img-c.udemycdn.com/redactor/raw/2020-08-17_11-30-35-4fd7abb7089f536a3754597b52eb3c06.png" width="500">

HINT 2: Remember this is how you pass headers with the requests library:

https://stackoverflow.com/questions/6260457/using-headers-with-the-python-requests-librarys-get-method

HINT 3: Print the output of the get request and make sure the actual HTML of the web page is printed, if not try adding more items from your header from hint1. Sometimes, Amazon might just return the Captcha page.

<img src="https://img-c.udemycdn.com/redactor/raw/2020-08-17_11-17-30-dbfc8264de6a7c2510e60cbd9a0bef49.png" width="1000">

3. Use BeautifulSoup to make soup with the web page HTML you get back. You'll need to use the "lxml" parser instead of the "html.parser" for this to work.



HINT: If you get an error that says "bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: html-parser." Then it means you're not using the right parser, you'll need to import lxml at the top and install the module then use "lxml" instead of "html.parser" when you make soup.



4. Use BeautifulSoup to get hold of the price of the item as a floating point number and print it out.

HINT: You might need to use the split() method: https://www.w3schools.com/python/ref_string_split.asp

<img src="https://img-c.udemycdn.com/redactor/raw/2020-08-17_11-23-51-5d3130b0f744dcfa1c60da4f30290087.png" width="500">
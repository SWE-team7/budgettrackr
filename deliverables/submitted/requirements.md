# Requirements
Group 07 : budgettrackr \
Date : 10/07/2022 \
Members : Braedon Behnke, Akiel Aries, Kyler Conant, Brock Heinz, Brandon Mack

# 1. **Positioning**
## 1.1 **Problem statement**

**The problem of** *[bouncing between websites for the best deal]* \
**affects** *[online shoppers, resellers, high-price item buyers]* \
**the impact of which is** *[Shoppers are spending more on a product than they should’ve]* 

## 1.2 **Product Position Statement**

**For** *[online shoppers]* \
**Who** *[for those wanting the best price]* \
**The (product name)** *[budgettrackr] is a [application allowing the user to compare prices 
of different products]* \
**That** *[allows you to view prices, trends, and other information on products to make the 
best educated decision on a purchase]* \
**Unlike** *[google]* \
**Our product** *[provides visualizations of price trends]* 

## 1.3 **Value proposition and customer segment**

**Value Proposition**
1) what your product is: budgettrackr is a application where you compare prices
1) the target customer: Online Shoppers
3) the value your product provides: Makes better use of time, helps show a product from 
different vendors on one website.
5) why your product is unique: Our product is unique because it takes in multiple websites 
to find the best price for the product searched.

**Consumer Segment:** Online Shoppers who do want to save money and look for the best price.

# 2. **Stakeholders**
- Users: Online shoppers (to shop online / use our program)
- Competitors: Honey (possibly showing other website prices for cheaper / deals), Google 
shop (showing quick and different price results of different websites)
- Developers: CS386 students (Building a product that can compare prices of a product through 
big companies)

# 3. **Functional requirements (features)**
- Able to search for a product.
- Able to see prices of products from said company.
- Sorting products from least to greatest price.
- Able to see a graph of prices.
- Able to see price history for a given product from a graph over the last 30 days.
- Show product images and description.
- Will show prices from a variety of sources.
- Links will go to the proper sites.
- Graph filters such as timeframe and collapsing all to one graph will be usable.
- Viewable on desktop browser.
- Developed using HTML and PyScript.


# 4. **Non-functional requirements**
1) Response Time:
  - We are not certain on the latency associated with certain functionalities such as 
  the web scrubbing utility.
  - Goal: When searching for a product offer a warning of possible latency issues 
  involved with parsing big data but assure a response time of under 15 seconds. 

2) Reliability
  - Goal: For this we will test use of our tool in short term segments and assure 
  uptime of at least 90%+

3) Portability: 
  - We are not sure if this piece of software will run on just any device such as mobile.
  - Goal: To verify our product, our software will be tested on our developers machines 
  ensuring 90% of customers using our tool on desktop a satisfactory experience.  

4) Accuracy:
  - It is hard to judge the accuracy of the data mined with our web scraping utility.
  - Goal: The accuracy of our results will leave 8/10 customers happy with their experience.  

# 5. **MVP**

Our Minimum Viable Product should at least be able to properly incorporate our required 
features for a product category such as our currently planned focus on computer processors. 
Our webpage will show various processors of different brands and prices, and be able to 
display these list prices over the past 30 and 90 day periods from at least 4 different 
sources - namely Amazon, Newegg, Best Buy, and either Walmart or Gamestop with preference 
towards Gamestop. These will all have valid links to the product page. Used markets will 
be avoided, although links to ebay search results will be included on the webpage. In 
addition to price data, pictures from multiple sources will be collected directly from 
the listings (so as to avoid possible google errors) as well as a general description of 
the product in addition to relevant specifications. These will be implemented through HTML 
and PyScript, and utilizing relevant APIs in calculations and data. This website will not 
have a registered domain name for testing, nor will we seek to establish an accessible 
server. Instead we will use a tool which allows hosting a local webpage to test our products 
usage with the APIs. The data should be consistent with Honey price tracking extension and 
show all these webpages at once with prices over the formerly described intervals. The webpage 
should be properly formatted and navigable between off-site and on-site links (related
products, homepage, and categories of which we will have one). The pictures should also 
be fully viewable, and description/specs legible on desktop.

# 6. **Use cases**
## 6.1 **Use case diagram**
![](https://github.com/SWE-team7/budgettrackr/blob/main/imgs/use_case_diagram.png)

## 6.2 **Use case descriptions and interface sketch**
Use Case: Search for product
- **Actor**: Shopper
- **Description**: Shopper will enter the name of a product into a search bar, and choose an item from a list of relevant results.
- **Preconditions**: Web Page must be open.
- **Main Flow**: 
    1) The shopper opens the website at budgettrackr.com
    2) The shopper types in the name of a desired product into the search bar
    3) The shopper submits the search term, bringing up a list of relevant results
    4) The shopper selects the specific product they want by clicking its name
    5) The product’s information is shown, including an expanded description
- **Alternate Flow**:
    1) If shopper cannot find specific product they want they will see the closes option to the product they typed
    2) Then continue as needed
- **Key Scenarios**:
    * Bill needed a quick way to search for a dinner table set on many different websites on one site. 
    Bill visited the budgttrackr website and found many other dinner table sets on many different 
    websites from many different vendors! 
- **Postconditions**: Finding the product

![](https://github.com/SWE-team7/budgettrackr/blob/main/imgs/search.png)

Use Case: View Price Information
- **Actor**: Shopper
- **Description**: The user will be able to view the price information for the given product they search for
- **Preconditions**: Shopper is on the website
- **Main Flow**: 
    1) Shopper uses the search bar to type in the desired product
    2) The website will return products that match 
    3) The use case ends
- **Subflow**:
    1) The user can click on a desired product from the list to view more information and purchase. 
    2) The shopper can also browse the returned list and view products and their descriptions. 
- **Key Scenarios**:
    - Jim, an up and coming event planner, wants to find the best deal on napkins for an upcoming event. 
    Jim can visit the budgettrackr webpage and use the search bar to view matches for his search. Jim 
    can now choose to browse the list and view descriptions or click on each product for more 
    information and to potentially purchase. 
- **Postconditions**: Price information is displayed and the shopper can view any of the listed items. 

![](https://github.com/SWE-team7/budgettrackr/blob/main/imgs/price_info.png)

Use Case: Price Analysis
- **Actor**: Trend Analyst
- **Description**: Trend Analyst wants to compare prices of a product over the last 30 days to 
understand whether this product group may be collectively dropping or rising recently.
- **Preconditions**: The website is already open.
- **Main Flow** : 
    1) Search the product name in the search bar and click search.
    2) Select a product and click Analyze Price button to display price information and graphs
    3) Filter graphs on the right side to overlay onto one graph over the last 30 days.
    4) Follow the line to see if the slope has hit a peak or is climbing to one recently.
    5) The use case ends
- **Alternative Flow**:
    1) If in step 1 of the basic flow, the actor instead searches the overall product category, 
    then they select the product based off of the category from a search menu
    2) The use case resumes at step 2.
- **Key Scenarios**:
    - Scenario 1: Bob, the computer salesperson has heard about a recent surge in the prices 
    of graphics cards. He uses budgettrackr in order to investigate for himself.
      1) Bob searches graphics cards in the search bar.
      2) Bob selects from the most relevant results, choosing a GTX 1060 as it is familiar to him and an older card.
      3) Bob filters the graphs on the right side to show information over the past 30 days and collapses them to one graph.
      4) Bob finds that the lines all trend upwards and have not hit a new peak for this aging card.
- **Postconditions**: Draw conclusions based on empirical evidence.

![](https://github.com/SWE-team7/budgettrackr/blob/main/imgs/price_analysis.png)

Use Case: Compare Prices
- **Actor**: Shopper
- **Description**: The shopper will be able to view prices for a given product from multiple different sources.
- **Preconditions**:
    1) The shopper has the website opened
    2) The shopper is searching for a product which is visible on the website
- **Main Flow**: 
    1) Search the product name in the search bar and press Enter.
    2) Click on the desired product
    3) Click on the Analyze Price button to display price histories and price comparisons
    4) Click on the Show Best Price button to highlight the cheapest product vendor
- **Key Scenarios**:
    - A father, Jesse, wants to get a large number of birthday presents for his son, whose birthday is 
    approaching, but his budget is tight this year due to a recent minor car accident.  Jesse can use 
    the BudgetTrackr website to find where he can get the birthday presents for the lowest price, 
    maximizing his child’s joy on his birthday.
      1) Jesse searches for his product in the website’s search bar.
      2) Jesse selects the product that he believes his child would like most.
      3) Jesse clicks on the “Analyze Price” button, revealing the current prices from all available 
      vendors of the desired product.
      5) Jesse clicks on the “Show Best Price” button to highlight the cheapest product vendor
      6) Jesse finds that one of the vendor graphs has a green outline with the caption “Best Price”, 
      showing which vendor sells the desired product for the lowest cost.
- **Postconditions**: Observing which online vendors are selling products for lower/higher prices.

![](https://github.com/SWE-team7/budgettrackr/blob/main/imgs/price_compare.png)

Use Case: Display Price History
- **Actor**: Shopper
- **Description**: The shopper will be able to select a given vendor selling the product, and 
display a detailed graph of the vendor’s pricing of that product over time.
- **Preconditions**: Web Page must be open.
- **Main Flow**: 
    1) Search the product in the search bar then press enter
    2) Desired product is shown 
    3) Prices trends are displayed
    4) Expand the price graph of a specific vendor
    5) Mouse over a segment of the graph to display the price at that specific point in time
- **Alternative Flow**: N/A
- **Key Scenario**:
  - Karen wanted to see other vendors at the same time with a price history graph with a 
  certain product that she wants to find. Karen used budgettrackr to look up a medkit and see price history 
    1) Karen searches for the product in the site’s search bar
    2) Karen selects the medkit she’s looking for
    3) Karen clicks the Analyze Price button to bring up the vendor information
    4) Karen clicks on the expand button on the corner of a vendor she’s interested in
    5) Karen looks at the expanded graph and mouses over the point in time she wanted to know about
    6) Karen sees the price at the given point in time	
- **Postconditions**: Finding the product prices

![](https://github.com/SWE-team7/budgettrackr/blob/main/imgs/price_history.png)


# 7. **User stories**
1) As an online shopper, I want an easy-to-use tool so that I can get the best prices on the 
things I purchase.
- Priority #6 (moderate priority); about 4 hours

2) As a mother, I want an easy to use product that allows me to quickly look for the best deal 
on back to school items to save time and money. 
- Priority #7 (moderate-high priority); about 4 hours

3) As a college student, I would love a tool that would show me the cheapest price for a product 
with one simple search in a visually appealing format. 
- Priority #4 (moderate priority); about 6 hours

4) As a deal seeker, I want a tool that lets me see the best prices for a product, so that I can 
save money on all of my purchases.
- Priority #7 (moderate-high priority); about 6 hours

5) As a trend analyst, I want a tool that allows me to view the best times to purchase a product 
to maximize the financial justification of my investment. 
- Priority #3 (low-moderate priority); about 8 hours

6) As a shopper, I want to be informed about the cost of a product between multiple vendors so 
that I can spend less on this purchase and more on future purchases.
- Priority #4 (moderate priority); about 4 hours

7) As a PC builder, I want to find the best price on components affected by shortages.
- Priority #8 (high priority); about 4 hours

8) As a chronic gamer, I want to see if a game has sold for less in the past, so that I can see 
how much the publishing company is willing to mark down their product.
- Priority #2 (low-priority); about 1 hour 

9) As a single dad, I want to purchase presents at an all-time low price, so that I can save money 
for Christmas.
- Priority #5 (moderate priority); about 2-5 hours

10) As a McDonald's manager, I want to find the best price on bulk items, so that I can effeciently 
manage this branch.
- Priority #8 (high priority); about 3 hours

11) As the owner of the Krusty Krab, I want to limit my daughter’s purchases by finding her the best 
deals on pearls, so that I can have more money, and my first dollar.
- Priority #6 (moderate priority); about 2 hours

# **8. Issue Tracker**

The user stories should be registered in your GitHub issue tracker. Include here the link 
for your issue tracker and a screenshot of what you did.

URL: [Issues · SWE-team7/budgettrackr (github.com)](https://github.com/SWE-team7/budgettrackr/issues)

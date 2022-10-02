![](Aspose.Words.2dfcf8d4-4087-4a8f-9f9f-da974c5bf25d.001.png)

**CS 386 – Software Engineering**

**Team Project – D.2 Requirements**

**Grading:** 30 points

In this deliverable, you will report the results for the requirements engineering for your product. Structure your deliverable using the following sections.

1. **Positioning**
1. **Problem statement**

Provide a statement to summarize the problem solved by your project according to the following structure (which is based on the OpenUP Vision Template[^1]):



|The problem of|*[bouncing between websites for the best deal]*|
| - | - |
|affects|*[online shoppers, resellers, high-price item buyers]*|
|the impact of which is|*[Shoppers are spending more on a product that they could’ve]*|
Example of a problem statement: “The problem of *inefficient prioritization of homework assignments* affects *college students*; the impact of which is *delivering assignments past due and receiving low grades*.” The problem should read as a problem (must be something bad that makes people spend time or money in an inefficient way.

2. **Product Position Statement**

A product position statement communicates the intent of the application and the importance of the project to all concerned personnel. The product should mitigate the aforementioned problem. Provide a statement according to the following structure:

|For|*[online shoppers]*|
| - | - |
|Who|*[for those wanting the best price]*|
|The (product name)|*[budgettrackr] is a [application allowing the user to compare prices of different products]*|
|That|<p>*[statement of key benefit; that is, the compelling reason to buy]*</p><p>*[this product allows you to view prices, trends, and other information on products to make the best educated decision on a purchase]*</p>|


|Unlike|*[primary competitive alternative] [unlike google]*|
| - | :- |
|Our product|*[provides visualizations of price trends]*|
Example of a product position statement: “For *college students who have many parallel homework assignments*, *MyPrioritizationApp* is a *planning app* that *crowdsources the identification of complexity and time necessary to accomplish assignments, supporting the informed prioritization*; unlike *myHomework Student Planner*, our product *does not rely on the judgment of a student who hasn’t started the homework yet*.” Make sure your product position statement is related to your problem.

3. **Value proposition and customer segment**

Report the value propositions and customer segments of your product. Make sure that your value proposition is coherent with the product position statement and contains the following elements: i) what your product is; ii) the target customer; iii) the value your product provides; and iv) why your product is unique.

Example:

**Value proposition:** *MyPrioritizationApp is a crowdsourced planning app* {(i) what your product is} *that allows college students* {(ii) target costumer} *to make better use of their time* {(iii) the value your product provides}*, prioritizing homework based on more accurate information of required time and complexity of the assignments*{(iv) why your product is unique}*.”*

**Consumer segment:** *College students who have many parallel homework assignments*

*Grading criteria* (3 points, 1 for each section): The content of the subsections should contain all the required elements, follow the provided template, and be consistent with each other. The text should not contain typos or grammar issues.The value for this proposition is considered very valuable in our eyes. As this product will show trends and track prices for a certain product. Not only will this help consumers save money but also see what vendor is at its lowest selling point during this time. Our target customer would be someone who shops online. While partaking in online shopping we can have a website that compares all popular websites to find the cheapest product searched for. The value we provide is ease of use and transparency to seeing how prices are on different websites. This will provide the value of life to relieve the hassle of moving from website to website and making sure you make the right decision to save more money on a certain product. Our product is considered very unique because we believe there is not really a big competitor out there. This is one if it’s kind showing a visualization of a price trend of a certain product with multiple big companies being compared.

**Value proposition and customer segment**

**Value proposition:**

1) what your product is: budgettrackr is a application where you compare prices
1) the target customer: Online Shoppers
3) the value your product provides: Makes better use of time, helps show a product from different vendors on one website.
3) why your product is unique: Our product is unique because it takes in multiple websites to find the best price for the product searched.

**Consumer Segment:** Online Shoppers who do want to save money and look for the best price.

2. **Stakeholders**

Make a list of all stakeholders of the project with a brief description of each one of them, emphasizing any responsibilities with the project. Examples of stakeholders include users, clients, competitors, detractors, developers, etc.

*Grading criteria* (1 point): The stakeholders can’t be too generic or specific. The list should reflect what was described in Section 1.

- Users: Online shoppers (to shop online / use our program)
- Competitors: Honey (possibly showing other website prices for cheaper / deals), Google shop (showing quick and different price results of different websites)
- Developers: CS386 students (Building a product that can compare prices of a product through big companies)
3. **Functional requirements (features)**

Make a numbered list of requirements for your software. Just self-explanatory titles are enough at this point. Remember that requirements should deliver the value proposition and they must be consistent with the interviews you performed for the previous deliverable. You can talk again to your clients to help define the requirements. While writing the requirements, focus on capabilities needed and not on how they should be implemented.

*Grading criteria* (2 points): The list should be comprehensive (remember that you are not expected to implement all the requirements by the end of the course but you should list them). Follow the same pattern to describe all the requirements. The list of requirements should be coherent with the previous sections.

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
4. **Non-functional requirements**

Make a numbered list of non-functional requirements that are important for your software. Explain their importance. Follow the terminology of ISO/IEC 25010:2011. For each non-functional requirement, give an objective goal/measurement in order to provide verifiability for the requirement. You can find more details at the following URL: <https://www.dropbox.com/s/o7jekzuxojc2ywo/ISO-IEC-IEEE-29148.pdf?dl=0>

*Grading criteria* (2 points): Follow the ISO-IEC terminology, explain why they are important, and provide verifiability criteria for each requirement.

1. Availability: It is hard to judge the availability of our service especially taking into account the amount of traffic our product may induce.
1. Response Time: We are not certain on the latency associated with certain functionalities such as the web scrubbing utility.
1. Reliability
1. Portability: We are not sure if this piece of software will run on just any operating system.
1. Accuracy:

It is hard to judge the accuracy of the data mined with our web scraping utility.

5. **MVP**

What will be your MVP? Which features are you going to validate? How?

*Grading criteria* (2 points): Describe what would be considered the Minimal Viable Product and how it will be tested (e.g., via implementation, prototyping, Wizard of Woz, etc.). Make clear what you are going to validate. The MVP should be coherent with the previous sections.

Our Minimum Viable Product should at least be able to properly incorporate our required features for a product category such as our currently planned focus on computer processors. Our webpage will show various processors of different brands and prices, and be able to display these list prices over the past 30 and 90 day periods from at least 4 different sources - namely Amazon, Newegg, Best Buy, and either Walmart or Gamestop with preference towards Gamestop. These will all have valid links to the product page. Used markets will be avoided, although links to ebay search results will be included on the webpage. In addition to price data, pictures from multiple sources will be collected directly from the listings (so as to avoid possible google errors) as well as a general description of the product in addition to relevant specifications. These will be implemented through HTML and PyScript, and utilizing relevant APIs in calculations and data. This website will not have a registered domain name for testing, nor will we seek to establish an accessible server. Instead we will use a tool which allows hosting a local webpage to test our products usage with the APIs. The data should be consistent with Honey price tracking extension and show all these webpages at once with prices over the formerly described intervals. The webpage should be properly formatted and navigable between off-site and on-site links (related products, homepage, and categories of which we will have one). The pictures should also be fully viewable, and description/specs legible on desktop.

6. **Use cases**
1. **Use case diagram**

Include a UML use case diagram for your project. There are many drawing tools that you can use, such as <https://app.diagrams.net/> and <https://creately.com/>

*Grading criteria* (5 points): Follow correctly the UML specification. The actors should be coherent with what was listed in sections 1 and 2. The use case diagram should be coherent with the list of requirements (section 3). The level of granularity of each use case should be adequate. The use cases should be adequately named.

![](Aspose.Words.2dfcf8d4-4087-4a8f-9f9f-da974c5bf25d.002.png)

2. **Use case descriptions and interface sketch**

Present one complete use case description for each member of the group. Therefore, if the group has 4 members, 4 use case descriptions are necessary. As the grading will not be individual, the group is responsible for keeping the quality and consistency of the whole document – avoid just splitting the work. Choose the most important use cases to describe. Follow the template provided by OpenUP to describe the use cases (see also the example): [https://people.cs.clemson.edu/~johnmc/courses/Publish/openup/guidances/templates/reso urces/uc_specification_tpl.dot](https://people.cs.clemson.edu/~johnmc/courses/Publish/openup/guidances/templates/resources/uc_specification_tpl.dot)

After each use case description, add a sketch of the corresponding user interface. This will be a good opportunity to start thinking about usability.

*Grading criteria* (8 points): Follow the template to describe the use cases. Present an interface sketch for each use case. Describe the use case as a dialog between the user and the system. Do not use UI language in the description of the use case.

Use Case: Search for product

Actor: Shopper

Description: Shopper will enter the name of a product into a search bar, and choose an item from a list of relevant results.

Preconditions: Web Page must be open.

Main Flow: Searching

Postconditions: Finding the product

![](Aspose.Words.2dfcf8d4-4087-4a8f-9f9f-da974c5bf25d.003.png)

Use Case: View Price Information

Actor: Shopper

Description: The user will be able to view the price information for the given product they search for

Preconditions: Shopper will search for an item and select one from the list of results Main Flow: Seeing a price

Postconditions: Price information is displayed

![](Aspose.Words.2dfcf8d4-4087-4a8f-9f9f-da974c5bf25d.004.jpeg)

Use Case: Price Analysis

Actor: Trend Analyst

Description: Trend Analyst wants to compare prices of a product over the last 30 days to understand whether this product group may be collectively dropping or rising recently. Preconditions: Product page is open on desired product.

Main Flow: Making graphs filtered for 30 days, collapsing all results to one graph. Postconditions: Observing rising or falling prices.

![](Aspose.Words.2dfcf8d4-4087-4a8f-9f9f-da974c5bf25d.005.png)

Use Case: Compare Prices

Actor: Shopper

Description: The shopper will be able to view prices for a given product from multiple different sources.

Preconditions: Shopper will search for a product and view price information

Main Flow: Seeing multiple prices from different sellers

Postconditions: Observing which sellers are selling products for cheaper/more expensive prices.

![](Aspose.Words.2dfcf8d4-4087-4a8f-9f9f-da974c5bf25d.006.jpeg)

Use Case: See price analysis

Actor: Shopper

Description: Shopper will enter the name of a product into a search bar, and then see a value of the prices showing past prices.

Preconditions: Web Page must be open.

Main Flow: Searching

Postconditions: Finding the product prices

![](Aspose.Words.2dfcf8d4-4087-4a8f-9f9f-da974c5bf25d.007.jpeg)

![](Aspose.Words.2dfcf8d4-4087-4a8f-9f9f-da974c5bf25d.008.jpeg)

7. **User stories**

Write two user stories for each member of the group. They can be related to the same features described in the use cases or to different ones. Adopt the following format: "As a <ROLE>, I want <SOMETHING> so that <GOAL>."

Establish a priority level for each user story and estimate how many hours each one will demand using the planning poker approach.

1. As an online shopper, I want an easy-to-use tool so that I can get the best prices on the things I purchase.
1. As a mother of four, I want a product that allows me to quickly look for the best deal on any given item to save time and money.
1. As a college student, I would love a tool that would show me the cheapest price for a product with one simple search.
1. As a deal seeker, I want a tool that lets me see the best times to shop for a product.
1. As a shopper, I want to be informed about the cost of a product between multiple vendors so I can spend less.
1. As a PC builder, I want to know if the price of an expensive part is trending down so I can make educated economic decisions.
1. As a chronic gamer, I want to know the prices for new and old video games so that I spend the right amount of money on a game.
1. As a single dad, I want a set of legos so my son will like me more, but I’m so I need the best price.
1. As a McDonald's manager, I want new chairs for my restaurant so that customers will be happy in the establishment.
1. As a Teacher, I want to get colored pencils for art so that my students can draw, but I’m a little poor right now!

*Grading criteria* (6 points): Use the provided format. The user stories should be in an adequate level of granularity (not too broad nor too specific). Provide the priority and estimation for each user story.

**8. Issue Tracker**

The user stories should be registered in your GitHub issue tracker. Include here the link for your issue tracker and a screenshot of what you did.

*Grading criteria* (1 point): Provide the URL and screenshot of the issue tracker. The user stories should be registered there.

URL: [Issues · SWE-team7/budgettrackr (github.com)](https://github.com/SWE-team7/budgettrackr/issues)

![](Aspose.Words.2dfcf8d4-4087-4a8f-9f9f-da974c5bf25d.009.png)

**Format**

You can find on BBLearn instructions for the format and submission of the deliverables.

**Example from the previous semester (not necessarily perfect or complete) <https://github.com/ChrisKeefe/DontPanic/blob/master/project_documentation/Requirements.md>**

See also several commented examples from previous years on BB Learn, in which I describe the most common mistakes in the sections above: [https://docs.google.com/document/d/1HLrFTRupUPinqJviA6oOcDzRNZy2n4lSl8Mg7nLIMcQ/ edit?usp=sharing](https://docs.google.com/document/d/1HLrFTRupUPinqJviA6oOcDzRNZy2n4lSl8Mg7nLIMcQ/edit?usp=sharing)

**Additional grading criteria**

Your deliverable should have all the aforementioned sections and follow the instructions. The deliverable must be available on the GitHub repository and written in an md format. All headers should be larger text and bolded to stand out. The deliverable should be updated via pull requests, which should be reviewed and approved by the Quality Assurance person. The document should be written in an appropriate language.

**Acknowledgment:** Parts of this document were adapted from OpenUP Templates

**Feedback![](Aspose.Words.2dfcf8d4-4087-4a8f-9f9f-da974c5bf25d.010.png)**

Didn’t like this assignment? Do you have suggestions? Please, let me know. <https://bit.ly/3vXiBCM>
12

[^1]: http://epf.eclipse.org/wikis/openup/

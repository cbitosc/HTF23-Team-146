# OnlineGrocerySystem

This project is implemented under the domain of web development and online food chains currently popular in markets.

## Technologies Used
1. Django web framework
2. Tokenauthentication for securing API, currently disabled
3. Backend Python programming language
4. frontend in HTML, CSS, JavaScript and bridge it with Jinja templating
5. Database in Sqlite

While deploying:
1. Make sure debug in setting is set to False
2. hide your secret key, better to generate it with environment variables or read it from another file
3. don't forget to mention in Allow_hosts list

## About
This project implements an Online Grocery selling and buying process. Using this a user can either buy groceries or sell them by listing as vendors.
It contains separate login processes for customers and vendors. Vendors have to submit their profile in the website and wait for a confirmation from the 
admins to approve it.
After approval the vendor can create a list or board of what items are available for sale, with their quantities and cost accordingly. They can manage the 
remaining stock of goods and digital invoice of what has been sold so far and to whome.
The customers can select the quantity of desired item to buy and place an order with 1 or more vendors. The information like customer name, delivery address, 
contact number is given to the vendor with the order as well. By default every order is given a status of placed, which is monitored by the vendor and can change
the order status accordingly. This change in order status is reflected in the customers' order history list as well.

The customer also has a digital copy of orders with details and history.

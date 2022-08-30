## Introduction:

Software applications are used in every part of our daily life but there are few areas like show rooms, cloth stores still there is need to use management software for handling billing details, customers information, stock details. In order to full fill this gap we designed boutique management software application for cloth stores. This application will reduce manual work and maintain all details in database. Report generation for every month, week and year is possible with this software.

### Video Demo: 
[![Go To Video](#)](https://drive.google.com/file/d/1KZ89uy86f367tUAIyjWHk3vZDlN50aWR/view?usp=sharing)

## Functionalities of the system:

In a boutique, there are many sections like Designer, New Born Fashion, Luxury, Readymade, Men, Women, Boys, Girls, etc. For each customer an Id is given (to uniquely identify them) to store their purchase and points. After a purchase is made, the customer is asked to fill in their details required to identify their unique ID to store their purchase (products that have been bought) and their price (as points). The price is converted into points and is stored in a relation and these points can be used by the customer to get discounts or any other gifts in their subsequent purchase. If any of purchased product is either damaged or need to be returned, a customer service section is provided where the product purchased can be returned or replaced based on the customers’ wish. While returning the product with the bill of purchase must be returned, so that, it is easier to confirm the purchase in the database. Our overall goal is to make things easier for the manager and employees to access data and information.

## Modules in the system:

_This system includes the following modules:_

- Customer Personal Information
- Add/Remove Customer
- Source Listing
- Searching
- Stocks Details
- Billing Details (Transaction Method Details)
- Order And Delivery Dates
- Product Return and Replacement
- Report Generation

## Benefits of the system:

This project would be very useful for automation of customer measurements and details management and, it will help them to hold the data of the garments, customers, providers with outstanding ease. Further it can also be used for day to day updating of customer information and new Stocks of Design by generating reports.

## Development Platform:

- For Database        -   MySQL
- For User Interface  -   Python

## ER Diagram:

![er](https://raw.githubusercontent.com/Jegadit/BoutiqueManagementSystem/main/ImgRes/ER.png)

This ER(Entity Relationship) Diagram represents  the model of Boutique  Store Management system Entity. The entity-relationship diagram of boutique store Management System shows all the visual instrument of database tablets and the relations between Products, login, customer data, admin, cart, recent orders etc. It used structure data and to define the relationships between structured data groups of boutique Store Management system Functionalities.

When the user tries to login into  the management system, the credentials that he entered is verified with the _UserName_ and _Password_ in the **Employee** table. Once the user is verified, he is given the permissions to add, modify, delete or view records from **Product**, **Customers** and **ReturnOrder** tables depending on his _RoleRank._

## Schema Diagram:

![schema](https://raw.githubusercontent.com/Jegadit/BoutiqueManagementSystem/main/ImgRes/Schema.png)

In this schema design, a uniqueness is identified through the primary keys which are _CustId_, _EmpId_, _UserId_, _ProdId_, _ReturnId_, and _BillId_. These primary keys become foreign keys when they are referred in other relations which are arrowed in the schema diagram

## Extended ER Features:

![EER1](https://raw.githubusercontent.com/Jegadit/BoutiqueManagementSystem/main/ImgRes/EER1.png)

The Entity **Employee** is (disjoint)specialized into 3 types of employees namely: Owner, Full timers and part timers; where the symbol “d” in the superclass entity, represents disjoint meaning that an employee at an instance cannot be both Owners or full times or Part times at the same time. The superclass entity **Employee** has a total participation with its subclass entities meaning that all employee should either be an owner, a full timer or a part timer.

![EER2](https://raw.githubusercontent.com/Jegadit/BoutiqueManagementSystem/main/ImgRes/EER2.png)

The Entity **Products** is (disjoint)specialized into 5 types of Products namely: DesignerSaree, Salwar, churidhar, ReadymadeSherwani, and CoatSuits with ProdId, ProdName, Qty, Gender, Type and amount as commonly inherited attributes; where the symbol “d” in the superclass entity, represents disjoint meaning that an individual product at an instance cannot be another product at the same time. The superclass entity **Products** has a total participation with its subclass entities meaning that all employee should either be a DesignerSaree, Salwar, churidhar, ReadymadeSherwani, or CoatSuits.

## Implementing Extended ER features:

![IEER](https://raw.githubusercontent.com/Jegadit/BoutiqueManagementSystem/main/ImgRes/IEER.png)

## Connectivity and connectors:

Connectivity refers to the connection of middleware or user-interface with the back-end database of the application. Such types of connections are done with the help of a connector( eg: JDBC, ODBC). A database connector is a software that connects an application to any database.

## Why Python?

With Python, one can easily work on prototype development and ad-hoc programming functions. This feature makes Python the ideal language for web development. You can save time, reduce cost, and get an efficient web application with functioning prototypes.

Python's standard database interface is Python DB-API. This interface uses the MySQL dB module for only MySQL. This module is independent of any other database engine, so we need to write Python scripts to access any other database engine.

## Python- MySQL -connector:

To access the MySQL database from Python, you need a database driver. MySQL Connector/Python is a standardized database driver provided by MySQL. Python MySQL Connector is a Python driver that helps to integrate Python and MySQL. This Python MySQL library allows the conversion between Python and MySQL data types. MySQL Connector API is implemented using pure Python and does not require any third-party library.

## Why have I used Python MySQL-connector:

- MySQL Connector/Python is an API implemented using pure Python. It means that you do not need to install any MySQL client library or any Python modules except the standard library.
- MySQL Connector/Python enables Python programs to access MySQL databases, using an API that is compliant with the Python Database API. It is written in pure Python and does not have any dependencies except for the Python Standard Library.
- MySQL Connector/Python allows you to convert the parameter’s value between Python and MySQL data types e.g., Python datetime and MySQL DATETIME.
- MySQL Connector/Python is designed specifically to MySQL. It supports all MySQL extensions such as LIMIT clause.

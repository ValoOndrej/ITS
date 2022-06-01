Login: xvaloo00
Name and Surename" Ondrej Valo
mail: xvaloo00@stud.fit.vutbr.cz
### Introduction
---
This test plan was developed as a school project for the ITS course in the academic year 2019/2020 at the Faculty of Information Technology, VUT. The goal of testing is an instance of the eCommerce platform OpenCart, which is an shopping website. The test plan focuses on the process of pusharching item and confirming it's payment.
### Subject of testing
---
Product purchasing process
### Tested properties
---
The following features will be tested:

Navigation
- Mouse and keyboard control
- Access the elements 
- Button, checkbox, textbox, selectbox behavior
- Required data
- Verification that required data is required

Data type
- Verification that only valid dates can be entered in forms requiring a date, number, etc.

Data integrity
- Verifying that the embedded data has been saved correctly
### Method
---
Tests are designed with behavior driven development method. Testing will be performed automatically using the Selenium tool. A set of several test cases will be run and evaluated automatically.
### Overview of sample test cases
---
F1: Proces of Adding product to shopping cart.
-  S1: Seting Checkboxes for product
-  S2: Seting Textboxes for product.
-  S3: Opening Selectboxes for product.
-  S4: Seting Selectboxes for product.
-  S5: Add product to shopping cart.

F2: Paying for products in shopping cart.
-  S1: Opening shopping cart.
-  S2: moving on page shopping cart.
-  S3: Opennin rollbar.
-  S4: Inserting coupon code.
-  S5: Filling shipping adress.
-  S6: Selecting shipping method.
-  S7: Inserting gift certificate.
-  S8: Continuing to checkout options.
-  S9: Filling checkout options.
-  S10: Filling Billing Details
-  S11: Filling Delivery Details 
-  S12: Filling Delivery Method
-  S13: Filling Payment Method
-  S14: Filling Confirm Order

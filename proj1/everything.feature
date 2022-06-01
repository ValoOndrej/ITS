Feature: Proces of Adding product to shopping cart.
  Scenario Outline: Seting Checkboxes for product
    Given Web browser is at the page of <product>.
      When User click on <checkbox> for difrent <options>.
      Then <option> wil be set to <checkbox>.
  Examples: Electronics
    | product         |
    | Apple Cinema 30 |
  Examples: Options for checkboxes
    | option     | checkbox               |
    | Radio      | Medium (+$24.00)       |
    | Checkbox   | Checkbox 2 (+$24.00)   |


  Scenario Outline: Seting Textboxes for product.
    Given Web browser is at the page of <product>.
      When User whrite to <textbox>.
      Then Text in <textbox> wil change.
  Examples: Electronics
    | product         |
    | Canon EOS 5D    |
    | iPhone          |
    | Apple Cinema 30 |
    | iMac            |
  Examples: Options for textboxes
    | textbox       |
    | Text          |
    | Textarea      |
    | Date          |
    | Time          |
    | Date & Time   |
    | Qty           |


  Scenario Outline: Opening Selectboxes for product.
    Given Web browser is at the page of <product>.
      When User click to <selectboxes>.
      Then Options will apear for <selectboxes>.
  Examples: Electronics
    | product         |
    | Canon EOS 5D    |
    | Apple Cinema 30 |
  Examples: selectboxes to set.
    | selectboxes  |
    | Select       |


  Scenario Outline: Seting Selectboxes for product.
    Given Web browser is at the page of <product>.
      When User click to <options>.
      Then <options> will be set as active.
  Examples: Electronics
    | product         |
    | Canon EOS 5D    |
    | Apple Cinema 30 |
  Examples: Options for selectboxes
    | options  |
    | Red      |
    | Blue     |
    | Green    |
    | Yellow   |


  Scenario Outline: Add product to shopping cart.
    Given Web browser is at the page of <product> whith selected options.
      When User click on button Add to Cart.
      Then <product> will be added to cart.
  Examples: Electronics
    | product         |
    | Canon EOS 5D    |
    | Apple Cinema 30 |



Feature: Paying for products in shopping cart.
  Scenario Outline: Opening shopping cart.
    Given Web browser is at the page of <product> whith selected options.
      When User click on button of shopping cart.
      Then Pop up window with information about shopping cart will apear.
  Examples: Electronics
    | product         |
    | Canon EOS 5D    |
    | iPhone          |
    | Apple Cinema 30 |
    | iMac            |


  Scenario Outline: moving on page shopping cart.
    Given Web browser is at the page of <product> whith pup up of shopping cart.
      When User click on button Wiew Cart on pup up of shopping cart.
      Then User will be redirect to the page Shopping Cart.
  Examples: Electronics
    | product         |
    | Canon EOS 5D    |
    | iPhone          |
    | Apple Cinema 30 |
    | iMac            |


  Scenario Outline: Opennin rollbar.
    Given Web browser is at the page Shopping Cart.
      When User wil click on <option>.
      Then Difrent setting will apreat base on <option>.
  Examples: Options before paying
    | option                    |
    | Use Coupon Code           |
    | Estimate Shipping & Taxes |
    | Use Gift Certificate      |


  Scenario: Inserting coupon code.
    Given Web browser is at the page Shopping Cart, with unrolled rollbar Use Coupon Code.
      When User will insert correct cupon code to textbox and click button Apply Coupon.
      Then Coupon wil be aceptet
      But upon payment will be unusable

  Scenario: Filling shipping adress.
    Given Web browser is at the page Shopping Cart, with unrolled rollbar Estimate Shipping & Taxes.
      When User will fill textboxes with correct parameters and click on button Get Quets.
      Then Pop up window will apear.

  Scenario: Selecting shipping method.
    Given Web browser is at the page Shopping Cart, with pop up window opend.
      When User will choose shipping method and click button Apply Shipping.
      Then Shipping estimate will be applied.

  Scenario: Inserting gift certificate.
    Given Web browser is at the page Shopping Cart, with unrolled rollbar Use Gift Certificate.
      When User will insert correct gift certificate to textbox and click button Apply Gift Certificate.
      Then Gift Certificate wil be acepted
      But upon payment will be unusable

  Scenario: Continuing to checkout options.
    Given Web browser is at the page Shopping Cart, with filed options for Shiping.
      When User will click on button Checkout.
      Then User will be redirect to the page Checkout.

  Scenario Outline: Filling checkout options.
    Given Web browser is at the page Checkout, with unrolled step 1.
      When User will choose <chcekout_option> and click on button continue.
      Then Step 2 will unroll with difrent parameter base on <chcekout_option>.

  Examples: Options for chcekout
    | chcekout_option   |
    | Register Account  |
    | Guest Checkout    |

  Scenario: Filling Billing Details
    Given Web browser is at the page Checkout, with unrolled step 2.
      When User will fill all mandatory texboxes and click button continue.
      Then Step 3 will unroll

  Scenario: Filling Delivery Details 
    Given Web browser is at the page Checkout, with unrolled step 3.
      When User will fill all mandatory texboxes and click button continue.
      Then Step 4 will unroll
    
  Scenario: Filling Delivery Method
    Given Web browser is at the page Checkout, with unrolled step 4.
      When User will choose shipping option and click button continue.
      Then Step 5 will unroll

  Scenario: Filling Payment Method
    Given Web browser is at the page Checkout, with unrolled step 5.
      When User will choose payment method, and agree to the Terms and Conditions and click button continue.
      Then Step 6 will unroll

  Scenario: Filling Confirm Order
    Given Web browser is at the page Checkout, with unrolled step 6.
      When User will confirm information about order and click button continue Order.
      Then User will be redirected to the page of confirmation about placed order.
Feature: Paying for products in shopping cart.
  Scenario: Opening shopping cart.
    Given Web browser is at the page of difrent product.
      When User click on button of shopping cart.
      Then Pop up window with information about shopping cart will apear.

  Scenario: moving on page shopping cart.
    Given Web browser is at the page of difrent product.
      When User click on button Wiew Cart on pup up of shopping cart.
      Then User will be redirect to the page Shopping Cart.

  Scenario: Opennin rollbar.
    Given Web browser is at the page Shopping Cart with somthing in cart.
      When User wil click on option.
      Then Difrent setting will apreat base on option.

  Scenario: Inserting coupon code.
    Given Web browser is at the page Shopping Cart, with unrolled rollbar Use Coupon Code.
      When User will insert correct cupon code to textbox and click button Apply Coupon.
      Then Coupon wil be aceptet

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

  Scenario: Continuing to checkout options.
    Given Web browser is at the page Shopping Cart, with filed options for Shiping.
      When User will click on button Checkout.
      Then User will be redirect to the page Checkout.

  Scenario: Filling checkout options.
    Given Web browser is at the page Checkout, with unrolled step 1.
      When User will choose chcekout_option and click on button continue.
      Then Step 2 will unroll with difrent parameter base on chcekout_option.

  Scenario: Filling Billing Details
    Given Web browser is at the page Checkout, with unrolled step 2.
      When User will fill all mandatory texboxes and click button continue.
      Then Step 3 will unroll

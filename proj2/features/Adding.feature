Feature: Proces of Adding product to shopping cart.
  Scenario: Seting Checkboxes for product
    Given Web browser is at the page of product.
      When User click on checkbox for difrent options.
      Then option wil be set to checkbox.

  Scenario: Seting Textboxes for product.
    Given Web browser is at the page of product.
      When User whrite to textbox.
      Then Text in textbox wil change.

  Scenario: Opening Selectboxes for product.
    Given Web browser is at the page of product.
      When User click to selectboxes.
      Then Options will apear for selectboxes.

  Scenario: Seting Selectboxes for product.
    Given Web browser is at the page of another product.
      When User click to options.
      Then options will be set as active.

  Scenario: Add product to shopping cart.
    Given Web browser is at the page of difrent product.
      When User click on button Add to Cart.
      Then product will be added to cart.

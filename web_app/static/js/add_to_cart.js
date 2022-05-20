$(document).ready(function (){
  function addToCart(productId, quantity) {
    let items = [];
    let quantities = []
    if (localStorage.items && localStorage.quantities) {
        items = localStorage.items.split(',');
        quantities = localStorage.quantities.split(',');

        if (items.includes(productId)) {
            const index = items.indexOf(productId);
            quantities[index] = parseInt(quantities[index]) + quantity;
        } else {
            items.push(productId);
            quantities.push(quantity);
        }
        localStorage.cartTotal = parseInt(localStorage.cartTotal) + quantity;
    } else {
        items = [productId]
        quantities = [quantity];
        localStorage.cartTotal = quantity;
    }
    localStorage.items = items;
    localStorage.quantities = quantities;
  }

  $('.add-to-cart').on('click', function() {
    const productId = this.dataset['id'];
    const quantity = parseInt($('select[name=quantity]').val());

    addToCart(productId, quantity);
    $('span.cart').text(localStorage.cartTotal);
    $('span.cart').css('color', 'red');
  });
});
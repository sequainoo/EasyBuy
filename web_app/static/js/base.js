$(document).ready(function() {
  const cartEl = $('span.cart');
  const cartContainer = $('.cart-container');
  if (localStorage.cartTotal) {
    cartEl.text(localStorage.cartTotal);
  } else {
    cartEl.text('empty');
  }
  cartEl.css('color', 'red');

  // When cart container gets clicked send cart data to
  // /cart on server for cart detailed page
  cartContainer.on('click', function() {
    if (localStorage.items && localStorage.quantities) {
      let items = localStorage.items.split(',');
      let quantities = localStorage.quantities.split(',');
      let queryString = '?';
      let index = 0;

      while (index < items.length - 1) {
        queryString += items[index];
        queryString += '=';
        queryString += quantities[index];
        queryString += '&';
        index += 1;
      }
      queryString += items[index];
      queryString += '=';
      queryString += quantities[index];

      url = '/cart' + queryString;

      window.location = url;
    } else {
      alert('Nothing in cart')
    }
  });
});
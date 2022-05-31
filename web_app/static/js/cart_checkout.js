$(document).ready(function (){
    function clearCart(){
      if (localStorage.items && localStorage.quantities) {
        delete localStorage.items;
        delete localStorage.quantities;
        delete localStorage.cartTotal;
        $('.cart').text('Empty');
      }
    }
    // get cart from localStorage
function getCart(){
    if (localStorage.items && localStorage.quantities){
    let items = localStorage.items.split(',');
    let quantities = localStorage.quantities.split(',');
    let index = 0;
    let cart = {};

    while (index < items.length) {
        cart[items[index]] = parseInt(quantities[index]);
        index += 1;
    }
    console.log('---cart--- in getCart');
    console.log(cart);
    return cart;
    }
    alert('cart is empty');
}
    //   checkout on cart funtion
  $('button.cart-checkout').on('click', function (){
    const email = $('input[name=email]')[0].value;
    const first_name = $('input[name=first_name]')[0].value;
    const last_name = $('input[name=last_name]')[0].value;

    if (email == '') {
      alert('Email is needed');
      return;
    }
    cart = getCart();
    if (!cart){
      return;
    }
    let data = {
      'email': email,
      'first_name': first_name,
      'last_name': last_name
    }
    data.cart = cart;
    data = JSON.stringify(data);
    $.post({
        'url': 'http://localhost/checkout',
        'contentType': 'application/json',
        data
    }).done((data, textStatus) => {
        alert(textStatus)
        window.location = data.url;
    }).fail((xhr, statusCode, error) => {
        alert(JSON.parse(xhr.responseText).error);
    });
  });
//   clear art
$('.cart-clear').on('click', clearCart);
});
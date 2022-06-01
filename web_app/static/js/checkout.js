$(document).ready(function() {
  $('.checkout').on('click', function (){
    const email = $('input[name=email]')[0].value;
    const first_name = $('input[name=first_name]')[0].value;
    const last_name = $('input[name=last_name]')[0].value;
    const quantity = $('select[name=quantity]')[0].value;
    const phone_id = this.dataset['id'];

    if (!email) {
        alert('Email is needed');
        return;
    }
    let cart = {};
    cart[phone_id] = parseInt(quantity);
    let data = {
        'email': email,
        'first_name': first_name,
        'last_name': last_name
    }
    data.cart = cart;
    data = JSON.stringify(data);
    console.log(data)
    $.post({
        'url': 'http://easybuy.digital/checkout',
        'contentType': 'application/json',
        data
    }).done((data, textStatus) => {
        window.location = data.url;
    }).fail((xhr, statusCode, error) => {
        alert(JSON.parse(xhr.responseText).error);
    });
  });
});

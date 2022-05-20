$(document).ready(function () {
  $('a.pay').on('click', function () {
    let order_id = $('#order_id').val();
    let name_on_card = $('#name_on_card').val();
    let card_number = $('#card_number').val();
    let exp_year = $('#exp_year').val();
    let exp_month = $('#exp_month').val();

    let data = {
        order_id,
        details: {
            name_on_card,
            card_number,
            exp_year: parseInt(exp_year),
            exp_month: parseInt(exp_month)
        }
    }
    data = JSON.stringify(data);

    $.post({
      url: 'http://localhost/payment',
      contentType: 'application/json',
      data: data
    }).done((data, textStatus) => {
      paymentPage = document.open('text/html', 'replace');
      paymentPage.write(data);
      paymentPage.close();
    }).fail((xhr, textStatus, error) => {
        const err = JSON.parse(xhr.responseText).error
        $(`<span class="flashed-message">${err}</span>`).prependTo($('.payment'))
    });
  });
});
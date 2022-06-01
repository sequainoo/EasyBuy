$(document).ready(function() {
  $('.btn').on('click', () => {
    const customer_id = $('#customer_id').val();
    const region_id = $('#region_id').val();
    const city_id = $('#city_id').val();
    const town = $('#town').val();
    const phone_number = $('#phone_number').val();

    let data = {customer_id, region_id, city_id, town, phone_number};
    data = JSON.stringify(data)
    console.log(data);
    $.post({
        "url": "http://easybuy.digital:8080/address",
        "contentType": "application/json",
        data
    }).done((data, statusCode) => {
      alert(statusCode);
      if (statusCode < 300) {
        alert('address created successfully proceed with payment');
      } else if (statusCode > 399 && statusCode < 500) {
          errorMsg = JSON.parse(data);
          alert(errorMsg.error);
      } else {
          alert('server error');
      }
    });
  });
});
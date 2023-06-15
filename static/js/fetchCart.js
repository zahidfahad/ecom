function fetchCart(){
    url = '/api/get_cart_details/'

    $.ajax({
        url: url + '?device=' + getCookie('device'),
        type: 'GET',
        success: function(response){
            console.log(response.cart_item_count)
            $('#cart-icon').attr('value', response.cart_item_count)
        }
    })
}
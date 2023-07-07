function addToCart(product_id,action){
    url = '/api/orders/';
    device = getCookie('device');
    backend_data = {"item_id": product_id,"action": action,"device": device};
    var token = $("#csrftoken").val();

    $.ajax({
        url: url,
        type: 'POST',
        headers: { "X-CSRFToken": token },
        data: backend_data,
        success: function(response){
            fetchCart();
        }
    })
}
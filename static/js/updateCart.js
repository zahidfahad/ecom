function updateCart(product_id,action){
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
            console.log(response)
            $('#item_quantity_box' + product_id).html(response.item.quantity);
            $('#item_quantity' + product_id).html(response.item.quantity);
            $('#item_total' + product_id).html(response.item.total);
            $('#total-price').html(response.grand_total);
        }
    })
}
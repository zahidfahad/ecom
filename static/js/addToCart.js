function addToCart(product_id,action){
    url = '/api/orders/';
    backend_data = {"item_id": product_id,"action": action};
    var token = $("#csrftoken").val();

    $.ajax({
        url: url,
        type: 'POST',
        headers: { "X-CSRFToken": token },
        data: backend_data,
        success: function(response){
            console.log(response)
            fetchCart();
        }
    })
}
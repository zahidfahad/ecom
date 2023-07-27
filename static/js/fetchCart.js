function fetchCart(){
    url = '/api/get_cart_details/'

    $.ajax({
        url: url + '?device=' + getCookie('device'),
        type: 'GET',
        success: function(response){
            $('#cart-icon').attr('value', response.cart_item_count);
            $('#total-price').html('BDT ' + response.grand_total);
            $.each(response.order_items, function (key, value) {
                console.log(value)
                $(".shopping_cart").append(
                    `
                    <tr id="cart_item${value.id}">
                        <td><img src=${value.item.cover_image} height="40px" width="40px" /> ${value.item.title}</td>
                        <td id='item_price${value.item.id}'>${value.item.price}</td>
                        <td id='item_quantity${value.item.id}'>${value.quantity}</td>
                        <td id='item_total${value.item.id}'>${value.total}</td>
                        <td>
                            <i class="fa fa-plus" data-action="add" onclick="updateCart(${value.item.id},this.dataset.action)"></i>
                            <span id="item_quantity_box${value.item.id}">${value.quantity}</span>
                            <i class="fa fa-minus" data-action="remove" onclick="updateCart(${value.item.id},this.dataset.action)"></i>
                        <td>
                        <td><i class="fa fa-trash" id="${value.id}"></i></td>
                    </tr>
                    `
                );
            })
        }
    })
    
}
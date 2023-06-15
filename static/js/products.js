function getProducts(){
    url = '/api/products/'
    $.ajax({
        url: url,
        type: 'GET',
        success: function(response){
           $.each(response, function(key, value){
            $('.products').append(
                `
                    <div class="card my-3">
                        <img height="200px" width="200px" src="${value.cover_image}" alt="Denim Jeans" style="width:100%">
                        <h1>${value.title}</h1>
                        <p class="price">$ ${value.price}</p>
                        <p>${value.description}</p>
                        <p><button class="add_to_cart" data-action="add" id="${value.id}" onclick="addToCart(this.id,this.dataset.action)">Add to Cart</button></p>
                    </div>

                `
            )
           })
        }
    })
}
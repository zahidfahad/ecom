function fetchBanners(){
    url = '/api/banners/'

    $.ajax({
        url: url,
        type: 'GET',
        success: function (response){
            count = 1
            $.each(response,function(key,value){
                $('.carousel-inner').append(
                    `
                        <div class="carousel-item ${count == 1 ? 'active': ''}">
                            <img src="${value.image}" class="d-block w-100" alt="...">
                            <div class="carousel-caption d-none d-md-block">
                            <h5>${value.title}</h5>
                            <p>${value.description}</p>
                            </div>
                        </div>

                    `
                )
                count+=1
            })
        }
    })
}
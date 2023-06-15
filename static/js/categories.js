
function fetchCategories(){
    url = '/api/categories/'
    $.ajax({
        url: url,
        method: 'GET',
        success: function(response){
            $.each(response, function (key, value) {
                $(".category_list").append(
                    `<li class='single_category my-2' id=${value.id}> ${value.name} <ul class="sub_category${value.id}"></ul> </li>`
                );
                fetchSubCategories(value.id)
            })
        }
    })
}


function fetchSubCategories(category_id){
    url = '/api/categories/related-sub-categories'
    $.ajax({
        url: url + '?category_id=' + category_id,
        type: 'GET',
        success: function(response){
            $.each(response, function (key, value) {
                $(".sub_category"+category_id).append(
                    `<li id=${value.id}> <a href="#" class="link-secondary">${value.name}</a> </li>`
                );
            })
        }
    })
}
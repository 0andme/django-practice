$(document).ready(function(){
    $('.list-group-item-action').click(function(){
        let product_id=$(this).attr('id')

       
        $.get(`http://127.0.0.1:8000/product/${product_id}/`).then(function (res) {
            $('#detailModalUserName').text(res.username)
            $('#detailModalTitle').text(res.title)
            $('#detailModalContent').html(res.content)
            $('#detailModalPrice').text(`${res.price}원`)
            $('#detailModalLocation').text(res.location)
            $('#detailModalImage').attr('src',res.image)
            $('#detailModal').modal('show')
          })
   
    })
})
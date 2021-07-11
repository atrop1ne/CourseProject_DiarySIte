$(document).ready(function(){
    let form = $('#tag_creation_form');
    form.on('submit', function(e){
        e.preventDefault();
        let serializedData = form.serialize();
        $.ajax({
            url: form.data('url'),
            data: serializedData,
            type: 'post',
            success: function(response){
                $('#tags_container').append('<div class="custom_tag_button"><a href="/notesByTag/' 
                    + response.tag.id + '"><div>' 
                    + response.tag.title + 
                    '</div></a><a href="/deleteTag/'
                    + response.tag.id +
                    '" class="delete_tag_button"></a></div>')
            }
        })
    })
})
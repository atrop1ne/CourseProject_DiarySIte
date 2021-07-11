const openButton = document.querySelector('.burger_menu_button')
        const closeButton = document.querySelector('.burger_menu_close_button')
        const menu = document.querySelector('.menu')

        openButton.addEventListener("click", function(e){
            openButton.classList.toggle('_active');
            menu.classList.toggle('_active');
            document.body.classList.toggle('_lock');
        })

        closeButton.addEventListener("click", function(e){
            openButton.classList.toggle('_active');
            menu.classList.toggle('_active');
            document.body.classList.toggle('_lock');
        })
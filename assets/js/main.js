(function($) {
    'use strict';
    
    /* jQuery MeanMenu */
    $('#mobile-menu-active').meanmenu({
        meanScreenWidth: "991",
        meanMenuContainer: ".mobile-menu-area .mobile-menu",
    });
    
    /* cart */
    $(".icon-cart").on("click", function() {
        $(this).parent().find('.shopping-cart-content').slideToggle('medium');
    })
    
    /*--
	Header Search Toggle
    -----------------------------------*/
    var searchToggle = $('.search-toggle');
    searchToggle.on('click', function(){
        if($(this).hasClass('open')){
           $(this).removeClass('open');
           $(this).siblings('.search-content').removeClass('open');
        }else{
           $(this).addClass('open');
           $(this).siblings('.search-content').addClass('open');
        }
    })
    
//------------------------------------------

document.addEventListener('DOMContentLoaded', function() {
    // Событие input для поля ввода
    document.getElementById('SSearch').addEventListener('input', function() {
        // Получаем значение поля ввода
        var query = this.value.trim(); // Используем trim() для удаления лишних пробелов
        
        // Выполняем поиск (здесь может быть AJAX запрос к серверу)
        searchGames(query);
    });
    
    function searchGames(query) {
        // Здесь вы можете отправить AJAX запрос на сервер для выполнения поиска
        // Например, вы можете использовать fetch или XMLHttpRequest
        // После получения результатов, обновите ваш интерфейс с помощью полученных данных
        console.log('Выполняется поиск игр по запросу: ' + query);
        
        // Ваш код для обновления результатов поиска
    }
});









//------------------------------------------ПОИСК ИГР------------------------------------------
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('SSearch');
    searchInput.value = '';

    searchInput.addEventListener('input', function() {
        const query = this.value.toLowerCase();
        const resultsContainer = document.getElementById('search-results');
        resultsContainer.innerHTML = '';

        if (query.length > 0) {
            const games = [
                { name: 'The Elder Scrolls 5: Skyrim', url: 'product-details.html' },
                { name: 'Grand Theft Auto: San Andreas', url: 'https://example.com/mario' },
                { name: 'Far Cry 3', url: 'https://example.com/rdr2' },
                { name: 'Grand Theft Auto 4', url: 'https://example.com/godofwar' },
                { name: 'Assassins Creed 2', url: 'https://example.com/witcher3' },
                { name: 'Mass Effect 2', url: 'https://example.com/minecraft' },
                { name: 'Mafia 2', url: 'https://example.com/fortnite' },
                { name: 'Call of Duty: Modern Warfare 2', url: 'https://example.com/overwatch' },
                { name: 'Fallout 3', url: 'https://example.com/cyberpunk' },
                { name: 'Helldrivers 2', url: 'https://example.com/genshin' }
            ];

            const filteredGames = games.filter(game => game.name.toLowerCase().includes(query));
            
            filteredGames.forEach(game => {
                const div = document.createElement('div');
                div.innerHTML = `<a href="${game.url}" target="_blank">${game.name}</a>`;
                div.className = 'search-item';
                resultsContainer.appendChild(div);
            });
        }
    });
});








//------------------------------------------
    /* slider active */
    $('.slider-active').owlCarousel({
        loop: true,
        navText: ['<i class="icon-arrow-left"></i>', '<i class="icon-arrow-right"></i>'],
        nav: true,
        autoplay: false,
        autoplayTimeout: 5000,
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        item: 1,
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 1
            },
            1000: {
                items: 1
            }
        }
    })
    
    
    /*------ Wow Active ----*/
    new WOW().init();
    



//КОРЗИНКА
document.addEventListener('DOMContentLoaded', function() {
    console.log('Document Loaded');
    
    if (document.querySelectorAll('.add-to-cart').length > 0) {
        updateCartCount();
        const addToCartButtons = document.querySelectorAll('.add-to-cart');
        addToCartButtons.forEach(button => {
            button.addEventListener('click', function(event) {
                event.preventDefault();
                const id = this.getAttribute('data-id');
                const name = this.getAttribute('data-name');
                const price = this.getAttribute('data-price');
                const image = this.getAttribute('data-image');
                addToCart(id, name, price, image);
                console.log('Добавление товара в корзину:', { id, name, price, image });
                window.location.href = 'cart.html';
            });
        });
    }

    if (document.getElementById('cart-items')) {
        loadCart();
    }
});

function isLocalStorageSupported() {
    try {
        const testKey = 'test';
        localStorage.setItem(testKey, 'testValue');
        localStorage.removeItem(testKey);
        return true;
    } catch (error) {
        console.error('localStorage is not supported:', error);
        return false;
    }
}

function addToCart(id, name, price, image) {
    if (!isLocalStorageSupported()) return;

    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    console.log('Текущая корзина:', cart);

    const existingItem = cart.find(item => item.id === id);

    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push({ id, name, price, image, quantity: 1 });
    }

    localStorage.setItem('cart', JSON.stringify(cart));
    console.log('Корзина после добавления товара:', JSON.parse(localStorage.getItem('cart')));
    updateCartCount();
}

function loadCart() {
    if (!isLocalStorageSupported()) return;

    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    console.log('Загрузка корзины:', cart);
    const cartItemsContainer = document.getElementById('cart-items');

    if (!cartItemsContainer) {
        console.error('Element with id "cart-items" not found');
        return;
    }

    cartItemsContainer.innerHTML = '';

    if (cart.length === 0) {
        cartItemsContainer.innerHTML = '<tr><td colspan="6">Корзина пуста</td></tr>';
        return;
    }

    cart.forEach(item => {
        const total = (item.price * item.quantity).toFixed(2);
        const cartItem = `
            <tr>
                <td class="product-thumbnail"><a href="#"><img src="${item.image}" alt=""></a></td>
                <td class="product-name"><a href="#">${item.name}</a></td>
                <td class="product-price-cart"><span class="amount">${item.price}₽</span></td>
                <td class="product-quantity">
                    <div class="cart-plus-minus">
                        <input class="cart-plus-minus-box" type="text" name="qtybutton" value="${item.quantity}" data-id="${item.id}" onchange="updateQuantity(this)">
                    </div>
                </td>
                <td class="product-subtotal">${total}₽</td>
                <td class="product-remove"><a href="#" onclick="removeFromCart('${item.id}')"><i class="ti-trash"></i></a></td>
            </tr>
        `;
        cartItemsContainer.insertAdjacentHTML('beforeend', cartItem);
    });
}

function updateQuantity(element) {
    if (!isLocalStorageSupported()) return;

    const id = element.getAttribute('data-id');
    const newQuantity = parseInt(element.value);
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    const item = cart.find(item => item.id === id);

    if (item) {
        item.quantity = newQuantity;
    }

    localStorage.setItem('cart', JSON.stringify(cart));
    loadCart();
}

function removeFromCart(id) {
    if (!isLocalStorageSupported()) return;

    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart = cart.filter(item => item.id !== id);
    localStorage.setItem('cart', JSON.stringify(cart));
    loadCart();
}

function clearCart() {
    if (!isLocalStorageSupported()) return;

    localStorage.removeItem('cart');
    loadCart();
}

function updateCartCount() {
    if (!isLocalStorageSupported()) return;

    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const count = cart.reduce((total, item) => total + item.quantity, 0);
    const cartCountElement = document.querySelector('.icon-cart .count-style');
    if (cartCountElement) {
        cartCountElement.textContent = count;
    } else {
        console.error('Element with class "icon-cart .count-style" not found');
    }
}












    
    /*----------------------------
    	Cart Plus Minus Button
    ------------------------------ */
    var CartPlusMinus = $('.cart-plus-minus');
    CartPlusMinus.prepend('<div class="dec qtybutton">-</div>');
    CartPlusMinus.append('<div class="inc qtybutton">+</div>');
    $(".qtybutton").on("click", function() {
        var $button = $(this);
        var oldValue = $button.parent().find("input").val();
        if ($button.text() === "+") {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            // Don't allow decrementing below zero
            if (oldValue > 0) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 1;
            }
        }
        $button.parent().find("input").val(newVal);
    });
    
   


    /*---------------------
    shop grid list
    --------------------- */
    $('.view-mode li a').on('click', function() {
        var $proStyle = $(this).data('view');
        $('.view-mode li').removeClass('active');
        $(this).parent('li').addClass('active');
        $('.product-view').removeClass('product-grid product-list').addClass($proStyle);
    })
    
    /* counterUp */
    $('.count').counterUp({
        delay: 10,
        time: 1000
    });
    
    /* product-dec-slider active */
    $('.product-dec-slider').owlCarousel({
        loop: true,
        autoplay: false,
        autoplayTimeout: 5000,
        navText: ['<i class="ti-arrow-left"></i>', '<i class="ti-arrow-right"></i>'],
        nav: true,
        item: 4,
        margin: 12,
        responsive: {
            0: {
                items: 2
            },
            576: {
                items: 3
            },
            768: {
                items: 3
            },
            1000: {
                items: 4
            }
        }
    })
    
    /* related-product-active active */
    $('.related-product-active').owlCarousel({
        loop: true,
        autoplay: false,
        autoplayTimeout: 5000,
        nav: false,
        item: 4,
        margin: 30,
        responsive: {
            0: {
                items: 1
            },
            576: {
                items: 2
            },
            768: {
                items: 3
            },
            1000: {
                items: 4
            }
        }
    })
    
    /*--------------------------
	 Zoom
	---------------------------- */	
	$("#zoompro").elevateZoom({
		gallery : "gallery",
		galleryActiveClass: "active",
		zoomWindowWidth:300,
		zoomWindowHeight:100,
		scrollZoom : false,
        zoomType : "inner",
        cursor: "crosshair"
	});  
    
    /*--
    Menu Stick
    -----------------------------------*/
    var header = $('.transparent-bar');
    var win = $(window);
    
    win.on('scroll', function() {
        var scroll = win.scrollTop();
        if (scroll < 200) {
            header.removeClass('stick');
        } else {
            header.addClass('stick');
        }
    });
    
    /*--------------------------
     ScrollUp
    ---------------------------- */
    $.scrollUp({
        scrollText: '<i class="ti-arrow-up"></i>',
        easingType: 'linear',
        scrollSpeed: 900,
        animation: 'fade'
    });
    
    
    /*---------------------
        Countdown
    --------------------- */
    $('[data-countdown]').each(function() {
        var $this = $(this),
            finalDate = $(this).data('countdown');
        $this.countdown(finalDate, function(event) {
            $this.html(event.strftime('<span class="cdown day">%-D <p>Days</p></span> <span class="cdown hour">%-H <p>Hour</p></span> <span class="cdown minutes">%M <p>Min</p></span class="cdown second"> <span>%S <p>Sec</p></span>'));
        });
    });
    
    
    /*--
    Testimonial Slick Carousel
    -----------------------------------*/
        $('.testimonial-text-slider').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        draggable: false,
        fade: true,
        asNavFor: '.slider-nav',
    });
    
    /*--
        Testimonial Slick Carousel as Nav
    -----------------------------------*/
    $('.testimonial-image-slider').slick({
      slidesToShow: 3,
      slidesToScroll: 1,
      asNavFor: '.testimonial-text-slider',
      dots: false,
      arrows: false,
      centerMode: true,
      focusOnSelect: true,
      centerPadding: '0px',
      responsive: [
        {
          breakpoint: 767,
          settings: {
            dots: false,
            centerPadding: '0px',
          }
        },
        {
          breakpoint: 420,
          settings: {
            autoplay: true,
            dots: false,
            slidesToShow: 1,
            centerMode: false,
          }
        }
      ]
    });
    
    
    
})(jQuery);
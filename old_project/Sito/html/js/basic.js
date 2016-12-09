
function addPage(page, book) {

	var id, pages = book.turn('pages');
	// Crea un nuovo elemento per questa pagina
	var element = $('<div />', {});
	// Aggiungi la pagina al libro
	if (book.turn('addPage', element, page)) {
		// Carica il codice HTML iniziale
		// Conterrà un indicatore di caricamento e il gradiente 
		element.html('<div class="gradient"></div><div class="loader"></div>');
		// Carica la pagina
		loadPage(page, element);
	}

}

function loadPage(page, pageElement) {

	// Crea un elemento 'immagine'
	var img = $('<img />');

	img.mousedown(function(e) {
		e.preventDefault();
	});

	img.load(function() {
		
		// Imposta la dimensione
		$(this).css({width: '100%', height: '100%'});
		// Aggiunge l'immagine alla pagina dopo il caricamento
		$(this).appendTo(pageElement);
		// Rimuove l'indicatore di caricamento
		pageElement.find('.loader').remove();

	});

	// Carica la pagina
	img.attr('src', 'pages/' +  page + '.jpg');

}


function loadLargePage(page, pageElement) {
	
	var img = $('<img />');

	img.load(function() {

		var prevImg = pageElement.find('img');
		$(this).css({width: '100%', height: '100%'});
		$(this).appendTo(pageElement);
		prevImg.remove();
		
	});
	
	// Carica nuova pagina
	img.attr('src', 'pages/' +  page + '-large.jpg');

}


function loadSmallPage(page, pageElement) {
	
	var img = pageElement.find('img');
	img.css({width: '100%', height: '100%'});
	img.unbind('load');
	// Carica nuova pagina
	img.attr('src', 'pages/' +  page + '.jpg');

}


// http://code.google.com/p/chromium/issues/detail?id=128488
function isChrome() {
	return navigator.userAgent.indexOf('Chrome') != -1;
}

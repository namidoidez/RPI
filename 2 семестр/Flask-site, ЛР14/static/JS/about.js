function init() {
	let point = [55.78208663493767,49.1078834320751];
	
	let map = new ymaps.Map('map', {
		center: point,
		zoom: 12
	});
	
	let placemark = new ymaps.Placemark(point, {
		hintContent: 'Основной офис TechFix - ул. Нариманова д. 45'
	});
	map.geoObjects.add(placemark);
}

ymaps.ready(init);
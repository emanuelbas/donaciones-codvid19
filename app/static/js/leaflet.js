var mymap = L.map('mapid').setView([51.505, -0.09], 13);

const initializeMap = (selector) => {
	map = L.map(selector).setView([-34.9187,-57.956],13);
	L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
	map.on('click', mapClickHandler)
}

const mapClickHandler = (e) => {
	addMarker(e.latlng);
}
const addMarker = ({ lat , lng }) => {
	if (marker) marker.remove();
	marker = L.marker([lat,lng]).addTo(map);
}

const submitHandler = (event) => {
	if (!marker) {
		event.preventDefault();
		alert('Debes seleccionar una ubicación en el mapa.')
	}
	else {
		latlng = marker.getLatLng();
		document.getElementById('corx').setAttribute('value', latlng.lat)
		document.getElementById('cory').setAttribute('value', latlng.lng)
	}
}


window.onload = () => {

	initializeMap('mapid');
}
setCookie = (cName, cValue, exDays) => {
	let d = new Date();
	d.setTime(d.getTime() + (exDays * 24 * 60 * 60 * 1000));
	const expires = "expires=" + d.toUTCString();
	document.cookie = cName + "=" + cValue + "; " + expires + "; path=/";
}

getCookie = (cName) => {
	const name = cName + "=";
	const cDecoded = decodeURIComponent(document.cookie);
	const cArr = cDecoded.split("; ");
	let value;
	cArr.forEach(val =>{
		if(val.indexOf(name) === 0) value = val.substring(name.length);
	})
	return value;
}

document.querySelector("#aceita").addEventListener("click", () => {
	document.querySelector("#aceitacookies").style.display = "none";
	setCookie("cookie", true, 1);
})

cookieMessage = () => {
	if(!getCookie("cookie"))
		document.querySelector("#aceitacookies").style.display = "block";
}
window.addEventListener("load", cookieMessage);










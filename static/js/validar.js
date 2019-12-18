function validar() {
	var user, password;
	user = document.getElementById("user").value;
	password = document.getElementById("password").value;

	if(user === ""){
		alert("No hay datos")
		return false;
	}
}
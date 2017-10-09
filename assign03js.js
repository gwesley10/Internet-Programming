
var counter = 1;
var array = []


function addInput(){

	var lengthh = 0;
	var oldDiv = document.getElementById('dynamicInput');
	var newDiv = document.createElement('div');
	var divIdName = (counter+1);
	var textBox = ""
	newDiv.setAttribute('id', divIdName);
	newDiv.innerHTML = divIdName + '<input type="text"'+'value=""'+ 'onkeyup=fun_length(lengthh)>' + lengthh;
	oldDiv.appendChild(newDiv);
	counter++;

}

function fun_length(lengthh){
	//alert("calculate length");
	lengthh++;
	array.push("");
}

function removeInput(input){
	//document.getElementById('dynamicInput').removeAttribute();
}


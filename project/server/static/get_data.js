/**
 * Created by Michael_Zhang on 11/13/16.
 */

function getData() {
 	var money = document.getElementById("money_form").value;
 	var xhr = new XMLHttpRequest();
 	var data = xhr.open('GET', '/graphs?amount=' + money, true);
 	console.log(data); 
}


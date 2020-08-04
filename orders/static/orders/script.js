
document.addEventListener('DOMContentLoaded',function(){
	document.querySelectorAll('.add_button').forEach(function(button){
		button.onclick = function(){
			current = button.dataset.item_id;
			no_of_toppings = button.dataset.no_toppings;
			document.querySelector('#toppings-alert').innerHTML = "";
			console.log(current);
			document.querySelector('.topping').style.display = 'Block';
			console.log(button.dataset.name);
			document.querySelector('#name_order').innerHTML = button.dataset.name;
			document.querySelector('#size_order').innerHTML = button.dataset.size;
			document.querySelector('#cost_order').innerHTML = '$' + button.dataset.cost;
			document.querySelector('#menu_item').value = parseInt(current);
		};
	});

	document.querySelector("form").onsubmit = function(){
		let count = 0;
		document.querySelectorAll('.topping_check').forEach(function(box){	
			if (box.checked == true)
				count++;
		});	
		if(count != parseInt(no_of_toppings)){
			document.querySelector('#toppings-alert').innerHTML = "Too many toppings"
			console.log("Too many or less toppings");
			return false;
		}
		// document.querySelector('.topping').style.display = 'none';
		// request = new XMLHttpRequest();
		// request.open('post','/cart');
		// request.onload = function(){

		// };
		// const data = new FormData();
		// data.append('menu_item',parseInt(current));
		// data.append('topping',toppings);
		// request.send(data);
		// return false;
	};
});


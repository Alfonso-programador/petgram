window.onload = function() {
    const url = window.location.href;

    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');
    const resultBox = document.getElementById('results-box');
    const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    
    const sendSearchData = (user) =>{
    	$.ajax({
    		type:"POST",
    		url:'users/search/',
    		data:{
    			'csrfmiddlewaretoken':csrf,
    			'user':user,
    		},
    		success:(res)=>{
    			const data = res.data
    			resultBox.innerHTML = ""
    			if (Array.isArray(data)){
    				data.forEach(user=>{
    					resultBox.innerHTML += `
    						<a href="p/${user.email}" class="item">
    							<div class="row mt-2 mb-2">
    								<div class="col-2">
    									<img src="${user.picture}" class="user-img">
    								</div>
    								<div class="col-10" >
    									<h5 style="margin-left:10px;">${user.username}</h5>
    									<p class="text-muted" style="margin-left:10px;">${user.first_name} ${user.last_name}</p>
    								</div>
    							</div>
    						</a>
 

    					` 
    				})
    			}else{
    				if(searchInput.value.length>0){
    					resultBox.innerHTML = `<b>${data}</b>`
    				}else{
    					resultBox.classList.add('not-visible')
    				}
    			}
    		},
    		error:(err)=>{
    			console.log(err)
    		}
    	})
    }

    searchInput.addEventListener('keyup',e=>{
    	if(resultBox.classList.contains('not-visible')){
    		resultBox.classList.remove('not-visible');
    	}
    	sendSearchData(e.target.value)})
}


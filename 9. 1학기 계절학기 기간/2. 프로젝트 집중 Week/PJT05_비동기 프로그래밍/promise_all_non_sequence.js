const axios = require('axios');

async function request(sub_path){
	
	const url = 'http://13.124.193.201:8844/' + sub_path
	
	try{
	
		const response = await axios.get(url);							
				
		return response.data
	}
	catch(e){

		console.log(e)
	}
}


const array = [{path:'a'}, {path:'b'}, {path:'c'}, {path:'d'}, {path:'e'}]


array.forEach(async (item) => {
	
	request(item.path).then((resolve) => {console.log(resolve)})			
})

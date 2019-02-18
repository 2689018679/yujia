 	let i = 0;
 	let time = setInterval(run, 2000)
	function run(){
		$(".photo img").eq(i-1).css("z-index","5");  
	    if(i>1){                            
	        i=0;
	    }
	    $(".photo img").eq(i).css("z-index","10");      
	    i++;
	}
	$(".photo img").hover(function(){
		clearInterval(time)
	},function(){
		time = setInterval(run, 2000)
	})
	
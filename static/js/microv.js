function greeting(time){
    if(time < 20){

        if (time < 10){
            greeting = 'Good morning'
        
        }else{
            greeting = 'Good day'
    }
   
    }else{
        greeting = 'Good evening'
    }
    return greeting

}

const greet = greeting(10)
console.log(greet)
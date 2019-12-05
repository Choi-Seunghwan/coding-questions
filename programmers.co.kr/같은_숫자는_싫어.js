const solution = arr => {
    return arr.filter( (el, i, arr) => {
        if(i === 0 )
            return true;
         else{
            if(el === arr[i-1]) return false;
            else return true
            }
        })    
}

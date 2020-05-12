function deepEquals(R, S) {
    
    if (Object.keys(R).length == Object.keys(S).length) 
      return true;
    if (Object.keys(R).length != Object.keys(S).length)
      return false;
    if (R == null || typeof R != "object" || S == null || typeof S != "object" )
    return false;
    var propsInR = 0;
    var propsInS = 0;
    for (var prop in R)
        propsInR += 1;
         
    for (var propes in S) {
       
        propsInS += 1;
        
        if (!(propes in R) || !deepEquals(R[propes], S[propes]))
        return false;
}
return propsInR == propsInS;
}
let test = {here: 5, object: 2};

// ****************       UNIT TESTING         ************************* /////////

console.log(deepEquals(test, {here: 5}));
console.log(deepEquals(test, test));


function solution(s, n){
  s = s.split('').map( (el) => {
    let code = el.charCodeAt();

    if (code === 32){
      return el;
    }else if (65 <= code && code <= 90){
      code += n;
      code = code > 90 ? code - 26 : code;
      el = String.fromCharCode(code);
    }else if ( 97 <= code && code <= 122){
      code += n;
      code = code > 122 ? code - 26 : code;
      el = String.fromCharCode(code);
    }

    return el
  });
  return s.join('');
}

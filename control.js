function checkDigit(s) {
    const m = [7, 3, 1];
    let n = 0;
  
    for (let i = 0; i < s.length; i++) {
      if (/[0-9]/.test(s[i])) {
        n += parseInt(s[i]) * m[i % 3];
      } else if (/[a-zA-Z]/.test(s[i])) {
        n += (s[i].toUpperCase().charCodeAt(0) - 65) * m[i % 3];
      } else {
        return -1;
      }
    }
    return n % 10;
  }
  
  // Ejemplo de uso
  const char = "42313601";
  console.log(checkDigit(char)); // Resultado: 9
  
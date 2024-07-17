let a = 1;
let b = 2;

function compare_values(a, b) {
  if (a > b) return ">";
  if (b > a) return "<";
  if (a == b) return "==";
}

console.log(compare_values(a, b));

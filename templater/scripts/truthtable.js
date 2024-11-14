function pad(num, size) {
  // num is a string representation of a binary number; size is the length of the 
  // of the desired padded result. "000000000" has to be modfied for desired lengths longer than this
    var s = "000000000000" + num;
    return s.slice(s.length-size);
}

async function genTruthTable(tp) {
  params = await tp.system.prompt("inputs,ouputs?")

  params = params.split(",")
  const inp = parseInt(params[0])
  const outp = parseInt(params[1])

  var binary, line, lines, rows;
  lines = ["", ""];
  lines[0] = "i|".repeat(inp) + "o|".repeat(outp - 1) + "o";
  lines[1] = "-|".repeat(inp + outp - 1) + "-";
  rows = Math.pow(2, inp);

  for (var n = 0, _pj_a = rows; n < _pj_a; n += 1) {
    binary = pad(n.toString(2), inp);
    line = binary.replace(/0/g, "0|").replace(/1/g, "1|");
    line += "|".repeat(outp - 1);
    lines.push(line);
  }

  return lines.join('\n');
}

module.exports = genTruthTable;
// Generated automatically by nearley
// http://github.com/Hardmath123/nearley
(function () {
function id(x) {return x[0]; }

  const lodashFlattenDeep = require('lodash.flattendeep')

  const filter = d => {
    return d.filter((token) => {
      return token !== null;
    });
  };

  function assignAll(objs) {
    return objs.reduce((prev, obj) => Object.assign(prev, obj))
  }



  const toImperial = {
    '0402': '01005',
    '0603': '0201',
    '1005': '0402',
    '1608': '0603',
    '2012': '0805',
    '2520': '1008',
    '3216': '1206',
    '3225': '1210',
    '4516': '1806',
    '4532': '1812',
    '5025': '2010',
    '6332': '2512',
  }


  function capacitance(d) {
    const [quantity, , metricPrefix, , farad] = d

    return {capacitance: parseFloat(`${quantity}${metricPrefix}`)}
  }


  function resistance(d, i, reject) {
    const [significantQuantity, metricPrefix, subQuantity, ohm] = d
    if (subQuantity) {
      if (/\./.test(significantQuantity.toString())) {
        return reject
      }
      var quantity = `${significantQuantity}.${subQuantity}`
    } else {
      var quantity = significantQuantity
    }
    return {resistance: parseFloat(`${quantity}${metricPrefix}`)}
  }
var grammar = {
    Lexer: undefined,
    ParserRules: [
    {"name": "unsigned_int$ebnf$1", "symbols": [/[0-9]/]},
    {"name": "unsigned_int$ebnf$1", "symbols": ["unsigned_int$ebnf$1", /[0-9]/], "postprocess": function arrpush(d) {return d[0].concat([d[1]]);}},
    {"name": "unsigned_int", "symbols": ["unsigned_int$ebnf$1"], "postprocess": 
        function(d) {
            return parseInt(d[0].join(""));
        }
        },
    {"name": "int$ebnf$1$subexpression$1", "symbols": [{"literal":"-"}]},
    {"name": "int$ebnf$1$subexpression$1", "symbols": [{"literal":"+"}]},
    {"name": "int$ebnf$1", "symbols": ["int$ebnf$1$subexpression$1"], "postprocess": id},
    {"name": "int$ebnf$1", "symbols": [], "postprocess": function(d) {return null;}},
    {"name": "int$ebnf$2", "symbols": [/[0-9]/]},
    {"name": "int$ebnf$2", "symbols": ["int$ebnf$2", /[0-9]/], "postprocess": function arrpush(d) {return d[0].concat([d[1]]);}},
    {"name": "int", "symbols": ["int$ebnf$1", "int$ebnf$2"], "postprocess": 
        function(d) {
            if (d[0]) {
                return parseInt(d[0][0]+d[1].join(""));
            } else {
                return parseInt(d[1].join(""));
            }
        }
        },
    {"name": "unsigned_decimal$ebnf$1", "symbols": [/[0-9]/]},
    {"name": "unsigned_decimal$ebnf$1", "symbols": ["unsigned_decimal$ebnf$1", /[0-9]/], "postprocess": function arrpush(d) {return d[0].concat([d[1]]);}},
    {"name": "unsigned_decimal$ebnf$2$subexpression$1$ebnf$1", "symbols": [/[0-9]/]},
    {"name": "unsigned_decimal$ebnf$2$subexpression$1$ebnf$1", "symbols": ["unsigned_decimal$ebnf$2$subexpression$1$ebnf$1", /[0-9]/], "postprocess": function arrpush(d) {return d[0].concat([d[1]]);}},
    {"name": "unsigned_decimal$ebnf$2$subexpression$1", "symbols": [{"literal":"."}, "unsigned_decimal$ebnf$2$subexpression$1$ebnf$1"]},
    {"name": "unsigned_decimal$ebnf$2", "symbols": ["unsigned_decimal$ebnf$2$subexpression$1"], "postprocess": id},
    {"name": "unsigned_decimal$ebnf$2", "symbols": [], "postprocess": function(d) {return null;}},
    {"name": "unsigned_decimal", "symbols": ["unsigned_decimal$ebnf$1", "unsigned_decimal$ebnf$2"], "postprocess": 
        function(d) {
            return parseFloat(
                d[0].join("") +
                (d[1] ? "."+d[1][1].join("") : "")
            );
        }
        },
    {"name": "decimal$ebnf$1", "symbols": [{"literal":"-"}], "postprocess": id},
    {"name": "decimal$ebnf$1", "symbols": [], "postprocess": function(d) {return null;}},
    {"name": "decimal$ebnf$2", "symbols": [/[0-9]/]},
    {"name": "decimal$ebnf$2", "symbols": ["decimal$ebnf$2", /[0-9]/], "postprocess": function arrpush(d) {return d[0].concat([d[1]]);}},
    {"name": "decimal$ebnf$3$subexpression$1$ebnf$1", "symbols": [/[0-9]/]},
    {"name": "decimal$ebnf$3$subexpression$1$ebnf$1", "symbols": ["decimal$ebnf$3$subexpression$1$ebnf$1", /[0-9]/], "postprocess": function arrpush(d) {return d[0].concat([d[1]]);}},
    {"name": "decimal$ebnf$3$subexpression$1", "symbols": [{"literal":"."}, "decimal$ebnf$3$subexpression$1$ebnf$1"]},
    {"name": "decimal$ebnf$3", "symbols": ["decimal$ebnf$3$subexpression$1"], "postprocess": id},
    {"name": "decimal$ebnf$3", "symbols": [], "postprocess": function(d) {return null;}},
    {"name": "decimal", "symbols": ["decimal$ebnf$1", "decimal$ebnf$2", "decimal$ebnf$3"], "postprocess": 
        function(d) {
            return parseFloat(
                (d[0] || "") +
                d[1].join("") +
                (d[2] ? "."+d[2][1].join("") : "")
            );
        }
        },
    {"name": "percentage", "symbols": ["decimal", {"literal":"%"}], "postprocess": 
        function(d) {
            return d[0]/100;
        }
        },
    {"name": "jsonfloat$ebnf$1", "symbols": [{"literal":"-"}], "postprocess": id},
    {"name": "jsonfloat$ebnf$1", "symbols": [], "postprocess": function(d) {return null;}},
    {"name": "jsonfloat$ebnf$2", "symbols": [/[0-9]/]},
    {"name": "jsonfloat$ebnf$2", "symbols": ["jsonfloat$ebnf$2", /[0-9]/], "postprocess": function arrpush(d) {return d[0].concat([d[1]]);}},
    {"name": "jsonfloat$ebnf$3$subexpression$1$ebnf$1", "symbols": [/[0-9]/]},
    {"name": "jsonfloat$ebnf$3$subexpression$1$ebnf$1", "symbols": ["jsonfloat$ebnf$3$subexpression$1$ebnf$1", /[0-9]/], "postprocess": function arrpush(d) {return d[0].concat([d[1]]);}},
    {"name": "jsonfloat$ebnf$3$subexpression$1", "symbols": [{"literal":"."}, "jsonfloat$ebnf$3$subexpression$1$ebnf$1"]},
    {"name": "jsonfloat$ebnf$3", "symbols": ["jsonfloat$ebnf$3$subexpression$1"], "postprocess": id},
    {"name": "jsonfloat$ebnf$3", "symbols": [], "postprocess": function(d) {return null;}},
    {"name": "jsonfloat$ebnf$4$subexpression$1$ebnf$1", "symbols": [/[+-]/], "postprocess": id},
    {"name": "jsonfloat$ebnf$4$subexpression$1$ebnf$1", "symbols": [], "postprocess": function(d) {return null;}},
    {"name": "jsonfloat$ebnf$4$subexpression$1$ebnf$2", "symbols": [/[0-9]/]},
    {"name": "jsonfloat$ebnf$4$subexpression$1$ebnf$2", "symbols": ["jsonfloat$ebnf$4$subexpression$1$ebnf$2", /[0-9]/], "postprocess": function arrpush(d) {return d[0].concat([d[1]]);}},
    {"name": "jsonfloat$ebnf$4$subexpression$1", "symbols": [/[eE]/, "jsonfloat$ebnf$4$subexpression$1$ebnf$1", "jsonfloat$ebnf$4$subexpression$1$ebnf$2"]},
    {"name": "jsonfloat$ebnf$4", "symbols": ["jsonfloat$ebnf$4$subexpression$1"], "postprocess": id},
    {"name": "jsonfloat$ebnf$4", "symbols": [], "postprocess": function(d) {return null;}},
    {"name": "jsonfloat", "symbols": ["jsonfloat$ebnf$1", "jsonfloat$ebnf$2", "jsonfloat$ebnf$3", "jsonfloat$ebnf$4"], "postprocess": 
        function(d) {
            return parseFloat(
                (d[0] || "") +
                d[1].join("") +
                (d[2] ? "."+d[2][1].join("") : "") +
                (d[3] ? "e" + (d[3][1] || "+") + d[3][2].join("") : "")
            );
        }
        },
    {"name": "_$ebnf$1", "symbols": []},
    {"name": "_$ebnf$1", "symbols": ["_$ebnf$1", /[\s]/], "postprocess": function arrpush(d) {return d[0].concat([d[1]]);}},
    {"name": "_", "symbols": ["_$ebnf$1"], "postprocess": () => null},
    {"name": "__$ebnf$1", "symbols": [/[\s]/]},
    {"name": "__$ebnf$1", "symbols": ["__$ebnf$1", /[\s]/], "postprocess": function arrpush(d) {return d[0].concat([d[1]]);}},
    {"name": "__", "symbols": ["__$ebnf$1"], "postprocess": () => null},
    {"name": "A", "symbols": [{"literal":"A"}]},
    {"name": "A", "symbols": [{"literal":"a"}]},
    {"name": "B", "symbols": [{"literal":"B"}]},
    {"name": "B", "symbols": [{"literal":"b"}]},
    {"name": "C", "symbols": [{"literal":"C"}]},
    {"name": "C", "symbols": [{"literal":"c"}]},
    {"name": "D", "symbols": [{"literal":"D"}]},
    {"name": "D", "symbols": [{"literal":"d"}]},
    {"name": "E", "symbols": [{"literal":"E"}]},
    {"name": "E", "symbols": [{"literal":"e"}]},
    {"name": "F", "symbols": [{"literal":"F"}]},
    {"name": "F", "symbols": [{"literal":"f"}]},
    {"name": "G", "symbols": [{"literal":"G"}]},
    {"name": "G", "symbols": [{"literal":"g"}]},
    {"name": "H", "symbols": [{"literal":"H"}]},
    {"name": "H", "symbols": [{"literal":"h"}]},
    {"name": "I", "symbols": [{"literal":"I"}]},
    {"name": "I", "symbols": [{"literal":"i"}]},
    {"name": "J", "symbols": [{"literal":"J"}]},
    {"name": "J", "symbols": [{"literal":"j"}]},
    {"name": "K", "symbols": [{"literal":"K"}]},
    {"name": "K", "symbols": [{"literal":"k"}]},
    {"name": "L", "symbols": [{"literal":"L"}]},
    {"name": "L", "symbols": [{"literal":"l"}]},
    {"name": "M", "symbols": [{"literal":"M"}]},
    {"name": "M", "symbols": [{"literal":"m"}]},
    {"name": "N", "symbols": [{"literal":"N"}]},
    {"name": "N", "symbols": [{"literal":"n"}]},
    {"name": "O", "symbols": [{"literal":"O"}]},
    {"name": "O", "symbols": [{"literal":"o"}]},
    {"name": "P", "symbols": [{"literal":"P"}]},
    {"name": "P", "symbols": [{"literal":"p"}]},
    {"name": "Q", "symbols": [{"literal":"Q"}]},
    {"name": "Q", "symbols": [{"literal":"q"}]},
    {"name": "R", "symbols": [{"literal":"R"}]},
    {"name": "R", "symbols": [{"literal":"r"}]},
    {"name": "S", "symbols": [{"literal":"S"}]},
    {"name": "S", "symbols": [{"literal":"s"}]},
    {"name": "T", "symbols": [{"literal":"T"}]},
    {"name": "T", "symbols": [{"literal":"t"}]},
    {"name": "U", "symbols": [{"literal":"U"}]},
    {"name": "U", "symbols": [{"literal":"u"}]},
    {"name": "V", "symbols": [{"literal":"V"}]},
    {"name": "V", "symbols": [{"literal":"v"}]},
    {"name": "W", "symbols": [{"literal":"W"}]},
    {"name": "W", "symbols": [{"literal":"w"}]},
    {"name": "X", "symbols": [{"literal":"X"}]},
    {"name": "X", "symbols": [{"literal":"x"}]},
    {"name": "Y", "symbols": [{"literal":"Y"}]},
    {"name": "Y", "symbols": [{"literal":"y"}]},
    {"name": "Z", "symbols": [{"literal":"Z"}]},
    {"name": "Z", "symbols": [{"literal":"z"}]},
    {"name": "metricPrefix", "symbols": ["giga"], "postprocess": () => 'e9  '},
    {"name": "metricPrefix", "symbols": ["mega"], "postprocess": () => 'e6  '},
    {"name": "metricPrefix", "symbols": ["kilo"], "postprocess": () => 'e3  '},
    {"name": "metricPrefix", "symbols": ["micro"], "postprocess": () => 'e-6 '},
    {"name": "metricPrefix", "symbols": ["nano"], "postprocess": () => 'e-9 '},
    {"name": "metricPrefix", "symbols": ["pico"], "postprocess": () => 'e-12'},
    {"name": "metricPrefix", "symbols": ["femto"], "postprocess": () => 'e-15'},
    {"name": "metricPrefix", "symbols": [], "postprocess": () => ''},
    {"name": "exa", "symbols": [{"literal":"E"}]},
    {"name": "exa", "symbols": ["E", "X", "A"]},
    {"name": "peta", "symbols": [{"literal":"P"}]},
    {"name": "peta", "symbols": ["P", "E", "T", "A"]},
    {"name": "tera", "symbols": [{"literal":"T"}]},
    {"name": "tera", "symbols": ["T", "E", "R", "A"]},
    {"name": "giga", "symbols": [{"literal":"G"}]},
    {"name": "giga", "symbols": ["G", "I", "G", "A"]},
    {"name": "mega", "symbols": [{"literal":"M"}]},
    {"name": "mega", "symbols": ["M", "E", "G", "A"]},
    {"name": "kilo", "symbols": [{"literal":"k"}]},
    {"name": "kilo", "symbols": ["K", "I", "L", "O"]},
    {"name": "hecto", "symbols": [{"literal":"h"}]},
    {"name": "hecto", "symbols": ["H", "E", "C", "T", "O"]},
    {"name": "deci", "symbols": [{"literal":"d"}]},
    {"name": "deci", "symbols": ["D", "E", "C", "I"]},
    {"name": "centi", "symbols": [{"literal":"c"}]},
    {"name": "centi", "symbols": ["C", "E", "N", "T", "I"]},
    {"name": "milli", "symbols": [{"literal":"m"}]},
    {"name": "milli", "symbols": ["M", "I", "L", "L", "I"]},
    {"name": "micro", "symbols": [{"literal":"u"}]},
    {"name": "micro", "symbols": [/[\u03BC]/]},
    {"name": "micro", "symbols": [/[\u00B5]/]},
    {"name": "micro", "symbols": [/[\uD835]/, /[\uDECD]/]},
    {"name": "micro", "symbols": [/[\uD835]/, /[\uDF07]/]},
    {"name": "micro", "symbols": [/[\uD835]/, /[\uDF41]/]},
    {"name": "micro", "symbols": [/[\uD835]/, /[\uDF7B]/]},
    {"name": "micro", "symbols": [/[\uD835]/, /[\uDFB5]/]},
    {"name": "micro", "symbols": ["M", "I", "C", "R", "O"]},
    {"name": "nano", "symbols": [{"literal":"n"}]},
    {"name": "nano", "symbols": ["N", "A", "N", "O"]},
    {"name": "pico", "symbols": [{"literal":"p"}]},
    {"name": "pico", "symbols": ["P", "I", "C", "O"]},
    {"name": "femto", "symbols": [{"literal":"f"}]},
    {"name": "femto", "symbols": ["F", "E", "M", "T", "O"]},
    {"name": "atto", "symbols": [{"literal":"a"}]},
    {"name": "atto", "symbols": ["A", "T", "T", "O"]},
    {"name": "packageSize", "symbols": ["_packageSize"], "postprocess": d => ({size: filter(lodashFlattenDeep(d))[0]})},
    {"name": "_packageSize", "symbols": ["_imperialSize"]},
    {"name": "_packageSize", "symbols": ["_metricSize"]},
    {"name": "_imperialSize$string$1", "symbols": [{"literal":"0"}, {"literal":"1"}, {"literal":"0"}, {"literal":"0"}, {"literal":"5"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "_imperialSize", "symbols": ["_imperialSize$string$1"]},
    {"name": "_imperialSize$string$2", "symbols": [{"literal":"0"}, {"literal":"2"}, {"literal":"0"}, {"literal":"1"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "_imperialSize", "symbols": ["_imperialSize$string$2"]},
    {"name": "_imperialSize$string$3", "symbols": [{"literal":"0"}, {"literal":"4"}, {"literal":"0"}, {"literal":"2"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "_imperialSize", "symbols": ["_imperialSize$string$3"]},
    {"name": "_imperialSize$string$4", "symbols": [{"literal":"0"}, {"literal":"6"}, {"literal":"0"}, {"literal":"3"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "_imperialSize", "symbols": ["_imperialSize$string$4"]},
    {"name": "_imperialSize$string$5", "symbols": [{"literal":"0"}, {"literal":"8"}, {"literal":"0"}, {"literal":"5"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "_imperialSize", "symbols": ["_imperialSize$string$5"]},
    {"name": "_imperialSize$string$6", "symbols": [{"literal":"1"}, {"literal":"0"}, {"literal":"0"}, {"literal":"8"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "_imperialSize", "symbols": ["_imperialSize$string$6"]},
    {"name": "_imperialSize$string$7", "symbols": [{"literal":"1"}, {"literal":"2"}, {"literal":"0"}, {"literal":"6"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "_imperialSize", "symbols": ["_imperialSize$string$7"]},
    {"name": "_imperialSize$string$8", "symbols": [{"literal":"1"}, {"literal":"2"}, {"literal":"1"}, {"literal":"0"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "_imperialSize", "symbols": ["_imperialSize$string$8"]},
    {"name": "_imperialSize$string$9", "symbols": [{"literal":"1"}, {"literal":"8"}, {"literal":"0"}, {"literal":"6"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "_imperialSize", "symbols": ["_imperialSize$string$9"]},
    {"name": "_imperialSize$string$10", "symbols": [{"literal":"2"}, {"literal":"0"}, {"literal":"1"}, {"literal":"0"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "_imperialSize", "symbols": ["_imperialSize$string$10"]},
    {"name": "_imperialSize$string$11", "symbols": [{"literal":"2"}, {"literal":"5"}, {"literal":"1"}, {"literal":"2"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "_imperialSize", "symbols": ["_imperialSize$string$11"]},
    {"name": "_metricSize$ebnf$1", "symbols": []},
    {"name": "_metricSize$ebnf$1", "symbols": ["_metricSize$ebnf$1", /[\s]/], "postprocess": function arrpush(d) {return d[0].concat([d[1]]);}},
    {"name": "_metricSize", "symbols": ["__metricSize", "_metricSize$ebnf$1", "M", "E", "T", "R", "I", "C"], "postprocess": d => toImperial[d[0]]},
    {"name": "_metricSize$ebnf$2", "symbols": []},
    {"name": "_metricSize$ebnf$2", "symbols": ["_metricSize$ebnf$2", /[\s]/], "postprocess": function arrpush(d) {return d[0].concat([d[1]]);}},
    {"name": "_metricSize", "symbols": ["M", "E", "T", "R", "I", "C", "_metricSize$ebnf$2", "__metricSize"], "postprocess": d => toImperial[d[7]]},
    {"name": "_metricSize", "symbols": ["unambigiousMetricSize"], "postprocess": d => toImperial[d[0]]},
    {"name": "unambigiousMetricSize$string$1", "symbols": [{"literal":"1"}, {"literal":"0"}, {"literal":"0"}, {"literal":"5"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "unambigiousMetricSize", "symbols": ["unambigiousMetricSize$string$1"]},
    {"name": "unambigiousMetricSize$string$2", "symbols": [{"literal":"1"}, {"literal":"6"}, {"literal":"0"}, {"literal":"8"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "unambigiousMetricSize", "symbols": ["unambigiousMetricSize$string$2"]},
    {"name": "unambigiousMetricSize$string$3", "symbols": [{"literal":"2"}, {"literal":"0"}, {"literal":"1"}, {"literal":"2"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "unambigiousMetricSize", "symbols": ["unambigiousMetricSize$string$3"]},
    {"name": "unambigiousMetricSize$string$4", "symbols": [{"literal":"2"}, {"literal":"5"}, {"literal":"2"}, {"literal":"0"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "unambigiousMetricSize", "symbols": ["unambigiousMetricSize$string$4"]},
    {"name": "unambigiousMetricSize$string$5", "symbols": [{"literal":"3"}, {"literal":"2"}, {"literal":"1"}, {"literal":"6"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "unambigiousMetricSize", "symbols": ["unambigiousMetricSize$string$5"]},
    {"name": "unambigiousMetricSize$string$6", "symbols": [{"literal":"3"}, {"literal":"2"}, {"literal":"2"}, {"literal":"5"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "unambigiousMetricSize", "symbols": ["unambigiousMetricSize$string$6"]},
    {"name": "unambigiousMetricSize$string$7", "symbols": [{"literal":"4"}, {"literal":"5"}, {"literal":"1"}, {"literal":"6"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "unambigiousMetricSize", "symbols": ["unambigiousMetricSize$string$7"]},
    {"name": "unambigiousMetricSize$string$8", "symbols": [{"literal":"5"}, {"literal":"0"}, {"literal":"2"}, {"literal":"5"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "unambigiousMetricSize", "symbols": ["unambigiousMetricSize$string$8"]},
    {"name": "unambigiousMetricSize$string$9", "symbols": [{"literal":"6"}, {"literal":"3"}, {"literal":"3"}, {"literal":"2"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "unambigiousMetricSize", "symbols": ["unambigiousMetricSize$string$9"]},
    {"name": "__metricSize", "symbols": ["unambigiousMetricSize"]},
    {"name": "__metricSize$string$1", "symbols": [{"literal":"0"}, {"literal":"4"}, {"literal":"0"}, {"literal":"2"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "__metricSize", "symbols": ["__metricSize$string$1"]},
    {"name": "__metricSize$string$2", "symbols": [{"literal":"0"}, {"literal":"6"}, {"literal":"0"}, {"literal":"3"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "__metricSize", "symbols": ["__metricSize$string$2"]},
    {"name": "M", "symbols": [{"literal":"M"}]},
    {"name": "M", "symbols": [{"literal":"m"}]},
    {"name": "E", "symbols": [{"literal":"E"}]},
    {"name": "E", "symbols": [{"literal":"e"}]},
    {"name": "T", "symbols": [{"literal":"T"}]},
    {"name": "T", "symbols": [{"literal":"t"}]},
    {"name": "R", "symbols": [{"literal":"R"}]},
    {"name": "R", "symbols": [{"literal":"r"}]},
    {"name": "I", "symbols": [{"literal":"I"}]},
    {"name": "I", "symbols": [{"literal":"i"}]},
    {"name": "C", "symbols": [{"literal":"C"}]},
    {"name": "C", "symbols": [{"literal":"c"}]},
    {"name": "main", "symbols": ["component"], "postprocess": d => assignAll(filter(lodashFlattenDeep(d)))},
    {"name": "component", "symbols": ["capacitor"]},
    {"name": "component", "symbols": ["resistor"]},
    {"name": "capacitor$ebnf$1", "symbols": ["packageSize"], "postprocess": id},
    {"name": "capacitor$ebnf$1", "symbols": [], "postprocess": function(d) {return null;}},
    {"name": "capacitor", "symbols": ["cSpecs", "capacitance", "cSpecs", "capacitor$ebnf$1", "cSpecs"]},
    {"name": "capacitor$ebnf$2", "symbols": ["packageSize"], "postprocess": id},
    {"name": "capacitor$ebnf$2", "symbols": [], "postprocess": function(d) {return null;}},
    {"name": "capacitor", "symbols": ["cSpecs", "capacitor$ebnf$2", "cSpecs", "capacitance", "cSpecs"]},
    {"name": "cSpecs$ebnf$1", "symbols": []},
    {"name": "cSpecs$ebnf$1$subexpression$1", "symbols": ["_", "cSpec", "_"]},
    {"name": "cSpecs$ebnf$1", "symbols": ["cSpecs$ebnf$1", "cSpecs$ebnf$1$subexpression$1"], "postprocess": function arrpush(d) {return d[0].concat([d[1]]);}},
    {"name": "cSpecs", "symbols": ["cSpecs$ebnf$1"]},
    {"name": "cSpecs", "symbols": ["__"]},
    {"name": "cSpec", "symbols": ["tolerance"]},
    {"name": "cSpec", "symbols": ["characteristic"]},
    {"name": "characteristic", "symbols": ["_characteristic"], "postprocess": d => ({characteristic: d[0]})},
    {"name": "_characteristic", "symbols": ["X", {"literal":"7"}, "R"], "postprocess": d => "X7R"},
    {"name": "_characteristic", "symbols": ["X", {"literal":"5"}, "R"], "postprocess": d => "X5R"},
    {"name": "_characteristic$macrocall$2", "symbols": ["C", {"literal":"0"}, "G"]},
    {"name": "_characteristic$macrocall$3", "symbols": ["N", "P", {"literal":"0"}]},
    {"name": "_characteristic$macrocall$1", "symbols": ["_characteristic$macrocall$2"]},
    {"name": "_characteristic$macrocall$1", "symbols": ["_characteristic$macrocall$3"]},
    {"name": "_characteristic$macrocall$1", "symbols": ["_characteristic$macrocall$2", {"literal":"/"}, "_characteristic$macrocall$3"]},
    {"name": "_characteristic$macrocall$1", "symbols": ["_characteristic$macrocall$3", {"literal":"/"}, "_characteristic$macrocall$2"]},
    {"name": "_characteristic", "symbols": ["_characteristic$macrocall$1"], "postprocess": () => 'C0G'},
    {"name": "_characteristic$macrocall$5$string$1", "symbols": [{"literal":"1"}, {"literal":"0"}, {"literal":"0"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "_characteristic$macrocall$5", "symbols": ["P", "_characteristic$macrocall$5$string$1"]},
    {"name": "_characteristic$macrocall$6", "symbols": ["M", {"literal":"7"}, "G"]},
    {"name": "_characteristic$macrocall$4", "symbols": ["_characteristic$macrocall$5"]},
    {"name": "_characteristic$macrocall$4", "symbols": ["_characteristic$macrocall$6"]},
    {"name": "_characteristic$macrocall$4", "symbols": ["_characteristic$macrocall$5", {"literal":"/"}, "_characteristic$macrocall$6"]},
    {"name": "_characteristic$macrocall$4", "symbols": ["_characteristic$macrocall$6", {"literal":"/"}, "_characteristic$macrocall$5"]},
    {"name": "_characteristic", "symbols": ["_characteristic$macrocall$4"], "postprocess": () => 'M7G'},
    {"name": "_characteristic$macrocall$8$string$1", "symbols": [{"literal":"3"}, {"literal":"3"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "_characteristic$macrocall$8", "symbols": ["N", "_characteristic$macrocall$8$string$1"]},
    {"name": "_characteristic$macrocall$9", "symbols": ["H", {"literal":"2"}, "G"]},
    {"name": "_characteristic$macrocall$7", "symbols": ["_characteristic$macrocall$8"]},
    {"name": "_characteristic$macrocall$7", "symbols": ["_characteristic$macrocall$9"]},
    {"name": "_characteristic$macrocall$7", "symbols": ["_characteristic$macrocall$8", {"literal":"/"}, "_characteristic$macrocall$9"]},
    {"name": "_characteristic$macrocall$7", "symbols": ["_characteristic$macrocall$9", {"literal":"/"}, "_characteristic$macrocall$8"]},
    {"name": "_characteristic", "symbols": ["_characteristic$macrocall$7"], "postprocess": () => 'H2G'},
    {"name": "_characteristic$macrocall$11$string$1", "symbols": [{"literal":"7"}, {"literal":"5"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "_characteristic$macrocall$11", "symbols": ["N", "_characteristic$macrocall$11$string$1"]},
    {"name": "_characteristic$macrocall$12", "symbols": ["L", {"literal":"2"}, "G"]},
    {"name": "_characteristic$macrocall$10", "symbols": ["_characteristic$macrocall$11"]},
    {"name": "_characteristic$macrocall$10", "symbols": ["_characteristic$macrocall$12"]},
    {"name": "_characteristic$macrocall$10", "symbols": ["_characteristic$macrocall$11", {"literal":"/"}, "_characteristic$macrocall$12"]},
    {"name": "_characteristic$macrocall$10", "symbols": ["_characteristic$macrocall$12", {"literal":"/"}, "_characteristic$macrocall$11"]},
    {"name": "_characteristic", "symbols": ["_characteristic$macrocall$10"], "postprocess": () => 'L2G'},
    {"name": "_characteristic$macrocall$14$string$1", "symbols": [{"literal":"1"}, {"literal":"5"}, {"literal":"0"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "_characteristic$macrocall$14", "symbols": ["N", "_characteristic$macrocall$14$string$1"]},
    {"name": "_characteristic$macrocall$15", "symbols": ["P", {"literal":"2"}, "H"]},
    {"name": "_characteristic$macrocall$13", "symbols": ["_characteristic$macrocall$14"]},
    {"name": "_characteristic$macrocall$13", "symbols": ["_characteristic$macrocall$15"]},
    {"name": "_characteristic$macrocall$13", "symbols": ["_characteristic$macrocall$14", {"literal":"/"}, "_characteristic$macrocall$15"]},
    {"name": "_characteristic$macrocall$13", "symbols": ["_characteristic$macrocall$15", {"literal":"/"}, "_characteristic$macrocall$14"]},
    {"name": "_characteristic", "symbols": ["_characteristic$macrocall$13"], "postprocess": () => 'P2H'},
    {"name": "_characteristic$macrocall$17$string$1", "symbols": [{"literal":"2"}, {"literal":"2"}, {"literal":"0"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "_characteristic$macrocall$17", "symbols": ["N", "_characteristic$macrocall$17$string$1"]},
    {"name": "_characteristic$macrocall$18", "symbols": ["R", {"literal":"2"}, "H"]},
    {"name": "_characteristic$macrocall$16", "symbols": ["_characteristic$macrocall$17"]},
    {"name": "_characteristic$macrocall$16", "symbols": ["_characteristic$macrocall$18"]},
    {"name": "_characteristic$macrocall$16", "symbols": ["_characteristic$macrocall$17", {"literal":"/"}, "_characteristic$macrocall$18"]},
    {"name": "_characteristic$macrocall$16", "symbols": ["_characteristic$macrocall$18", {"literal":"/"}, "_characteristic$macrocall$17"]},
    {"name": "_characteristic", "symbols": ["_characteristic$macrocall$16"], "postprocess": () => 'R2H'},
    {"name": "_characteristic$macrocall$20$string$1", "symbols": [{"literal":"3"}, {"literal":"3"}, {"literal":"0"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "_characteristic$macrocall$20", "symbols": ["N", "_characteristic$macrocall$20$string$1"]},
    {"name": "_characteristic$macrocall$21", "symbols": ["S", {"literal":"2"}, "H"]},
    {"name": "_characteristic$macrocall$19", "symbols": ["_characteristic$macrocall$20"]},
    {"name": "_characteristic$macrocall$19", "symbols": ["_characteristic$macrocall$21"]},
    {"name": "_characteristic$macrocall$19", "symbols": ["_characteristic$macrocall$20", {"literal":"/"}, "_characteristic$macrocall$21"]},
    {"name": "_characteristic$macrocall$19", "symbols": ["_characteristic$macrocall$21", {"literal":"/"}, "_characteristic$macrocall$20"]},
    {"name": "_characteristic", "symbols": ["_characteristic$macrocall$19"], "postprocess": () => 'S2H'},
    {"name": "_characteristic$macrocall$23$string$1", "symbols": [{"literal":"4"}, {"literal":"7"}, {"literal":"0"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "_characteristic$macrocall$23", "symbols": ["N", "_characteristic$macrocall$23$string$1"]},
    {"name": "_characteristic$macrocall$24", "symbols": ["T", {"literal":"2"}, "H"]},
    {"name": "_characteristic$macrocall$22", "symbols": ["_characteristic$macrocall$23"]},
    {"name": "_characteristic$macrocall$22", "symbols": ["_characteristic$macrocall$24"]},
    {"name": "_characteristic$macrocall$22", "symbols": ["_characteristic$macrocall$23", {"literal":"/"}, "_characteristic$macrocall$24"]},
    {"name": "_characteristic$macrocall$22", "symbols": ["_characteristic$macrocall$24", {"literal":"/"}, "_characteristic$macrocall$23"]},
    {"name": "_characteristic", "symbols": ["_characteristic$macrocall$22"], "postprocess": () => 'T2H'},
    {"name": "_characteristic$macrocall$26$string$1", "symbols": [{"literal":"7"}, {"literal":"5"}, {"literal":"0"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "_characteristic$macrocall$26", "symbols": ["N", "_characteristic$macrocall$26$string$1"]},
    {"name": "_characteristic$macrocall$27", "symbols": ["U", {"literal":"2"}, "J"]},
    {"name": "_characteristic$macrocall$25", "symbols": ["_characteristic$macrocall$26"]},
    {"name": "_characteristic$macrocall$25", "symbols": ["_characteristic$macrocall$27"]},
    {"name": "_characteristic$macrocall$25", "symbols": ["_characteristic$macrocall$26", {"literal":"/"}, "_characteristic$macrocall$27"]},
    {"name": "_characteristic$macrocall$25", "symbols": ["_characteristic$macrocall$27", {"literal":"/"}, "_characteristic$macrocall$26"]},
    {"name": "_characteristic", "symbols": ["_characteristic$macrocall$25"], "postprocess": () => 'U2J'},
    {"name": "_characteristic$macrocall$29$string$1", "symbols": [{"literal":"1"}, {"literal":"0"}, {"literal":"0"}, {"literal":"0"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "_characteristic$macrocall$29", "symbols": ["N", "_characteristic$macrocall$29$string$1"]},
    {"name": "_characteristic$macrocall$30", "symbols": ["Q", {"literal":"3"}, "K"]},
    {"name": "_characteristic$macrocall$28", "symbols": ["_characteristic$macrocall$29"]},
    {"name": "_characteristic$macrocall$28", "symbols": ["_characteristic$macrocall$30"]},
    {"name": "_characteristic$macrocall$28", "symbols": ["_characteristic$macrocall$29", {"literal":"/"}, "_characteristic$macrocall$30"]},
    {"name": "_characteristic$macrocall$28", "symbols": ["_characteristic$macrocall$30", {"literal":"/"}, "_characteristic$macrocall$29"]},
    {"name": "_characteristic", "symbols": ["_characteristic$macrocall$28"], "postprocess": () => 'Q3K'},
    {"name": "_characteristic$macrocall$32$string$1", "symbols": [{"literal":"1"}, {"literal":"5"}, {"literal":"0"}, {"literal":"0"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "_characteristic$macrocall$32", "symbols": ["N", "_characteristic$macrocall$32$string$1"]},
    {"name": "_characteristic$macrocall$33", "symbols": ["P", {"literal":"3"}, "K"]},
    {"name": "_characteristic$macrocall$31", "symbols": ["_characteristic$macrocall$32"]},
    {"name": "_characteristic$macrocall$31", "symbols": ["_characteristic$macrocall$33"]},
    {"name": "_characteristic$macrocall$31", "symbols": ["_characteristic$macrocall$32", {"literal":"/"}, "_characteristic$macrocall$33"]},
    {"name": "_characteristic$macrocall$31", "symbols": ["_characteristic$macrocall$33", {"literal":"/"}, "_characteristic$macrocall$32"]},
    {"name": "_characteristic", "symbols": ["_characteristic$macrocall$31"], "postprocess": () => 'P3K'},
    {"name": "tolerance$ebnf$1$subexpression$1", "symbols": ["plusMinus", "_"]},
    {"name": "tolerance$ebnf$1", "symbols": ["tolerance$ebnf$1$subexpression$1"], "postprocess": id},
    {"name": "tolerance$ebnf$1", "symbols": [], "postprocess": function(d) {return null;}},
    {"name": "tolerance", "symbols": ["tolerance$ebnf$1", "decimal", "_", {"literal":"%"}], "postprocess": d => ({tolerance: d[1]})},
    {"name": "plusMinus$string$1", "symbols": [{"literal":"+"}, {"literal":"/"}, {"literal":"-"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "plusMinus", "symbols": ["plusMinus$string$1"]},
    {"name": "plusMinus", "symbols": [{"literal":"±"}]},
    {"name": "plusMinus$string$2", "symbols": [{"literal":"+"}, {"literal":"-"}], "postprocess": function joiner(d) {return d.join('');}},
    {"name": "plusMinus", "symbols": ["plusMinus$string$2"]},
    {"name": "capacitance", "symbols": ["decimal", "_", "metricPrefix", "_", "farad"], "postprocess": capacitance},
    {"name": "farad", "symbols": [{"literal":"F"}], "postprocess": () => null},
    {"name": "farad", "symbols": ["F", "A", "R", "A", "D"], "postprocess": () => null},
    {"name": "resistor$ebnf$1", "symbols": ["packageSize"], "postprocess": id},
    {"name": "resistor$ebnf$1", "symbols": [], "postprocess": function(d) {return null;}},
    {"name": "resistor", "symbols": ["rSpecs", "resistance", "rSpecs", "resistor$ebnf$1", "rSpecs"]},
    {"name": "resistor$ebnf$2", "symbols": ["packageSize"], "postprocess": id},
    {"name": "resistor$ebnf$2", "symbols": [], "postprocess": function(d) {return null;}},
    {"name": "resistor", "symbols": ["rSpecs", "resistor$ebnf$2", "rSpecs", "resistance", "rSpecs"]},
    {"name": "rSpecs$ebnf$1", "symbols": []},
    {"name": "rSpecs$ebnf$1$subexpression$1", "symbols": ["_", "rSpec", "_"]},
    {"name": "rSpecs$ebnf$1", "symbols": ["rSpecs$ebnf$1", "rSpecs$ebnf$1$subexpression$1"], "postprocess": function arrpush(d) {return d[0].concat([d[1]]);}},
    {"name": "rSpecs", "symbols": ["rSpecs$ebnf$1"]},
    {"name": "rSpecs", "symbols": ["__"]},
    {"name": "rSpec", "symbols": ["tolerance"]},
    {"name": "resistance$ebnf$1", "symbols": ["int"], "postprocess": id},
    {"name": "resistance$ebnf$1", "symbols": [], "postprocess": function(d) {return null;}},
    {"name": "resistance$ebnf$2$subexpression$1", "symbols": ["_", "ohm"]},
    {"name": "resistance$ebnf$2", "symbols": ["resistance$ebnf$2$subexpression$1"], "postprocess": id},
    {"name": "resistance$ebnf$2", "symbols": [], "postprocess": function(d) {return null;}},
    {"name": "resistance", "symbols": ["decimal", "metricPrefix", "resistance$ebnf$1", "resistance$ebnf$2"], "postprocess": resistance},
    {"name": "ohm", "symbols": ["O", "H", "M"], "postprocess": () => null}
]
  , ParserStart: "main"
}
if (typeof module !== 'undefined'&& typeof module.exports !== 'undefined') {
   module.exports = grammar;
} else {
   window.grammar = grammar;
}
})();
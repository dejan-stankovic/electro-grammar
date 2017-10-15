from lark import Lark, Transformer

grammar = '!n_unsigned_int: xrule_0-> alias_0\n!n_int: xrule_3 xrule_0-> alias_1\n!n_unsigned_decimal: xrule_0 xrule_5-> alias_2\n!n_decimal: xrule_6 xrule_0 xrule_5-> alias_3\n!n_percentage: n_decimal xrule_7-> alias_4\n!n_jsonfloat: xrule_6 xrule_0 xrule_5 xrule_9-> alias_5\n!n__ws_maybe: xrule_10-> alias_6\n!n__ws: xrule_11-> alias_7\n!n_a: xrule_12\n    |xrule_13\n!n_b: xrule_14\n    |xrule_15\n!n_c: xrule_16\n    |xrule_17\n!n_d: xrule_18\n    |xrule_19\n!n_e: xrule_20\n    |xrule_21\n!n_f: xrule_22\n    |xrule_23\n!n_g: xrule_24\n    |xrule_25\n!n_h: xrule_26\n    |xrule_27\n!n_i: xrule_28\n    |xrule_29\n!n_j: xrule_30\n    |xrule_31\n!n_k: xrule_32\n    |xrule_33\n!n_l: xrule_34\n    |xrule_35\n!n_m: xrule_36\n    |xrule_37\n!n_n: xrule_38\n    |xrule_39\n!n_o: xrule_40\n    |xrule_41\n!n_p: xrule_42\n    |xrule_43\n!n_q: xrule_44\n    |xrule_45\n!n_r: xrule_46\n    |xrule_47\n!n_s: xrule_48\n    |xrule_49\n!n_t: xrule_50\n    |xrule_51\n!n_u: xrule_52\n    |xrule_53\n!n_v: xrule_54\n    |xrule_55\n!n_w: xrule_56\n    |xrule_57\n!n_x: xrule_58\n    |xrule_59\n!n_y: xrule_60\n    |xrule_61\n!n_z: xrule_62\n    |xrule_63\n!n_exa: xrule_20\n    |n_e n_x n_a\n!n_peta: xrule_42\n    |n_p n_e n_t n_a\n!n_tera: xrule_50\n    |n_t n_e n_r n_a\n!n_giga: xrule_24\n    |n_g n_i n_g n_a\n!n_mega: xrule_36\n    |n_m n_e n_g n_a\n!n_kilo: xrule_33\n    |n_k n_i n_l n_o\n!n_hecto: xrule_27\n    |n_h n_e n_c n_t n_o\n!n_deci: xrule_19\n    |n_d n_e n_c n_i\n!n_centi: xrule_17\n    |n_c n_e n_n n_t n_i\n!n_milli: xrule_37\n    |n_m n_i n_l n_l n_i\n!n_micro: xrule_53\n    |/[\\u03BC]/\n    |/[\\u00B5]/\n    |/[\\uD835]/ /[\\uDECD]/\n    |/[\\uD835]/ /[\\uDF07]/\n    |/[\\uD835]/ /[\\uDF41]/\n    |/[\\uD835]/ /[\\uDF7B]/\n    |/[\\uD835]/ /[\\uDFB5]/\n    |n_m n_i n_c n_r n_o\n!n_nano: xrule_39\n    |n_n n_a n_n n_o\n!n_pico: xrule_43\n    |n_p n_i n_c n_o\n!n_femto: xrule_23\n    |n_f n_e n_m n_t n_o\n!n_atto: xrule_13\n    |n_a n_t n_t n_o\n!n_packagesize: n__packagesize-> alias_8\n!n__packagesize: n__imperialsize\n    |n__metricsize\n!n__imperialsize: xrule_64\n    |xrule_65\n    |xrule_66\n    |xrule_67\n    |xrule_68\n    |xrule_69\n    |xrule_70\n    |xrule_71\n    |xrule_72\n    |xrule_73\n    |xrule_74\n!n__metricsize: n___metricsize xrule_10 n_m n_e n_t n_r n_i n_c-> alias_9\n    |n_m n_e n_t n_r n_i n_c xrule_10 n___metricsize-> alias_10\n    |n_unambigiousmetricsize-> alias_11\n!n_unambigiousmetricsize: xrule_75\n    |xrule_76\n    |xrule_77\n    |xrule_78\n    |xrule_79\n    |xrule_80\n    |xrule_81\n    |xrule_82\n    |xrule_83\n!n___metricsize: n_unambigiousmetricsize\n    |xrule_66\n    |xrule_67\n!n_main: n_component-> alias_12\n!n_component: n_capacitor-> alias_13\n    |n_resistor-> alias_14\n    |n_led-> alias_15\n!n_capacitor: n_cspecs n_capacitance n_cspecs xrule_84 n_cspecs\n    |n_cspecs xrule_84 n_cspecs n_capacitance n_cspecs\n    |n_cap n_cspecs xrule_84 n_cspecs n_capacitancenofarad\n    |n_capacitance n_cspecs\n    |n_cap n_cspecs n_capacitancenofarad\n    |n_capacitance n_cspecs xrule_84 n_cspecs\n!n_cap: n_c xrule_85 xrule_86 xrule_85 xrule_87 xrule_88 xrule_89 xrule_90 xrule_91-> alias_16\n!n_cspecs: xrule_92\n    |n__ws\n!n_cspec: n_tolerance\n    |n_characteristic\n    |n_voltage_rating\n!n_voltage_rating: n_decimal n__ws_maybe n_v-> alias_17\n!n_characteristic: n_characteristic_-> alias_18\n!n_characteristic_: n_class1\n    |n_class2\n!n_class1: n_c xrule_93 n_g-> alias_19\n    |n_n n_p xrule_93-> alias_20\n    |n_p xrule_94-> alias_21\n    |n_m xrule_95 n_g-> alias_22\n    |n_n xrule_96-> alias_23\n    |n_h xrule_97 n_g-> alias_24\n    |n_n xrule_98-> alias_25\n    |n_l xrule_97 n_g-> alias_26\n    |n_n xrule_99-> alias_27\n    |n_p xrule_97 n_h-> alias_28\n    |n_n xrule_100-> alias_29\n    |n_r xrule_97 n_h-> alias_30\n    |n_n xrule_101-> alias_31\n    |n_s xrule_97 n_h-> alias_32\n    |n_n xrule_102-> alias_33\n    |n_t xrule_97 n_h-> alias_34\n    |n_n xrule_103-> alias_35\n    |n_u xrule_97 n_j-> alias_36\n    |n_n xrule_104-> alias_37\n    |n_q xrule_105 n_k-> alias_38\n    |n_n xrule_106-> alias_39\n    |n_p xrule_105 n_k-> alias_40\n!n_class2: n_class2_letter n_class2_number n_class2_code-> alias_41\n!n_class2_letter: n_x\n    |n_y\n    |n_z\n!n_class2_number: xrule_107\n    |xrule_108\n    |xrule_109\n    |xrule_95\n    |xrule_110\n    |xrule_111\n!n_class2_code: n_p\n    |n_r\n    |n_s\n    |n_t\n    |n_u\n    |n_v\n!n_tolerance: xrule_112 n_decimal n__ws_maybe xrule_7-> alias_42\n!n_plusminus: xrule_113\n    |xrule_114\n    |xrule_115\n!n_capacitance: n_decimal n__ws_maybe xrule_116 n__ws_maybe n_farad-> alias_43\n!n_capacitancenofarad: n_decimal n__ws_maybe xrule_116-> alias_44\n!n_farad: n_f-> alias_45\n    |n_f n_a n_r n_a n_d-> alias_46\n!n_resistor: n_rspecs n_resistance n_rspecs xrule_84 n_rspecs\n    |n_rspecs xrule_84 n_rspecs n_resistance n_rspecs\n!n_rspecs: xrule_117\n    |n__ws\n!n_rspec: n_tolerance\n    |n_power_rating\n!n_power_rating: n_decimal n__ws_maybe xrule_118 n__ws_maybe n_watts-> alias_47\n!n_watts: n_watts_-> alias_48\n!n_watts_: n_w\n    |n_w n_a n_t n_t n_s\n!n_resistance: n_decimal n__ws_maybe n_rest-> alias_49\n!n_rest: n_rmetricprefix xrule_119 xrule_120\n    |n_ohm\n!n_ohm: n_ohm_-> alias_50\n!n_ohm_: n_o n_h n_m\n    |xrule_121\n    |xrule_122\n!n_led: n_led_letters n_ledspecs\n    |n_ledspecs n_led_letters\n    |n_ledspecs n_led_letters n_ledspecs\n!n_led_letters: n_l n_e n_d-> alias_51\n!n_ledspecs: xrule_123\n!n_ledspec: n_packagesize\n    |n_color\n!n_color: n_color_name-> alias_52\n!n_color_name: n_r n_e n_d-> alias_53\n    |n_g n_r n_e n_e n_n-> alias_54\n    |n_b n_l n_u n_e-> alias_55\n    |n_y n_e n_l n_l n_o n_w-> alias_56\n    |n_o n_r n_a n_n n_g n_e-> alias_57\n    |n_w n_h n_i n_t n_e-> alias_58\n    |n_a n_m n_b n_e n_r-> alias_59\n    |n_c n_y n_a n_n-> alias_60\n    |n_p n_u n_r n_p n_l n_e-> alias_61\n    |n_y n_e n_l n_l n_o n_w n__ws_maybe n_g n_r n_e n_e n_n-> alias_62\n!n_powermetricprefix: n_giga-> alias_63\n    |n_mega-> alias_64\n    |n_kilo-> alias_65\n    |n_milli-> alias_66\n    |n_micro-> alias_67\n    |n_nano-> alias_68\n    |n_pico-> alias_69\n    |n_femto-> alias_70\n!n_rmetricprefix: n_giga-> alias_71\n    |n_mega-> alias_72\n    |n_kilo-> alias_73\n    |n_r-> alias_74\n!n_cmetricprefix: n_micro-> alias_75\n    |n_nano-> alias_76\n    |n_pico-> alias_77\n!xrule_62: "Z"\n!xrule_111: "9"\n!xrule_37: "m"\n!xrule_38: "N"\n!xrule_16: "C"\n!xrule_84: (n_packagesize)?\n!xrule_19: "d"\n!xrule_65: "0201"\n!xrule_72: "1806"\n!xrule_87: (n_c)?\n!xrule_94: "100"\n!xrule_49: "s"\n!xrule_90: (n_o)?\n!xrule_52: "U"\n!xrule_67: "0603"\n!xrule_70: "1206"\n!xrule_102: "470"\n!xrule_82: "5025"\n!xrule_44: "Q"\n!xrule_105: "3"\n!xrule_42: "P"\n!xrule_100: "220"\n!xrule_56: "W"\n!xrule_50: "T"\n!xrule_0: (/[0-9]/)+\n!xrule_2: "+"\n!xrule_92: (n__ws_maybe n_cspec n__ws_maybe)*\n!xrule_107: "4"\n!xrule_91: (n_r)?\n!xrule_98: "75"\n!xrule_122: "Ω"\n!xrule_119: (n_int)?\n!xrule_55: "v"\n!xrule_123: (n__ws_maybe n_ledspec n__ws_maybe)+\n!xrule_48: "S"\n!xrule_23: "f"\n!xrule_66: "0402"\n!xrule_24: "G"\n!xrule_22: "F"\n!xrule_79: "3216"\n!xrule_81: "4516"\n!xrule_118: (n_powermetricprefix)?\n!xrule_58: "X"\n!xrule_35: "l"\n!xrule_21: "e"\n!xrule_1: "-"\n!xrule_20: "E"\n!xrule_60: "Y"\n!xrule_41: "o"\n!xrule_36: "M"\n!xrule_10: (/[\\s]/)*\n!xrule_80: "3225"\n!xrule_8: (/[+-]/)?\n!xrule_101: "330"\n!xrule_106: "1500"\n!xrule_69: "1008"\n!xrule_6: (xrule_1)?\n!xrule_59: "x"\n!xrule_51: "t"\n!xrule_54: "V"\n!xrule_30: "J"\n!xrule_114: "±"\n!xrule_61: "y"\n!xrule_93: "0"\n!xrule_45: "q"\n!xrule_73: "2010"\n!xrule_104: "1000"\n!xrule_75: "1005"\n!xrule_109: "6"\n!xrule_57: "w"\n!xrule_46: "R"\n!xrule_18: "D"\n!xrule_26: "H"\n!xrule_68: "0805"\n!xrule_86: (n_p)?\n!xrule_3: (xrule_1\n    |xrule_2)?\n!xrule_33: "k"\n!xrule_83: "6332"\n!xrule_29: "i"\n!xrule_12: "A"\n!xrule_34: "L"\n!xrule_7: "%"\n!xrule_96: "33"\n!xrule_85: (n_a)?\n!xrule_115: "+-"\n!xrule_47: "r"\n!xrule_76: "1608"\n!xrule_13: "a"\n!xrule_28: "I"\n!xrule_32: "K"\n!xrule_39: "n"\n!xrule_78: "2520"\n!xrule_11: (/[\\s]/)+\n!xrule_116: (n_cmetricprefix)?\n!xrule_117: (n__ws_maybe n_rspec n__ws_maybe)*\n!xrule_43: "p"\n!xrule_112: (n_plusminus n__ws_maybe)?\n!xrule_71: "1210"\n!xrule_103: "750"\n!xrule_110: "8"\n!xrule_25: "g"\n!xrule_64: "01005"\n!xrule_53: "u"\n!xrule_97: "2"\n!xrule_74: "2512"\n!xrule_99: "150"\n!xrule_27: "h"\n!xrule_9: (/[eE]/ xrule_8 xrule_0)?\n!xrule_88: (n_i)?\n!xrule_15: "b"\n!xrule_63: "z"\n!xrule_108: "5"\n!xrule_40: "O"\n!xrule_120: (n__ws_maybe n_ohm)?\n!xrule_17: "c"\n!xrule_89: (n_t)?\n!xrule_5: (xrule_4 xrule_0)?\n!xrule_121: "Ω"\n!xrule_113: "+/-"\n!xrule_95: "7"\n!xrule_31: "j"\n!xrule_77: "2012"\n!xrule_14: "B"\n!xrule_4: "."'

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['id', 'nuller', 'flat', 'resistance', 'flatten', 'filter', 'capacitance', 'toImperial', 'type'])
@Js
def PyJsHoisted_id_(x, this, arguments, var=var):
    var = Scope({'x':x, 'arguments':arguments, 'this':this}, var)
    var.registers(['x'])
    return var.get('x').get('0')
PyJsHoisted_id_.func_name = 'id'
var.put('id', PyJsHoisted_id_)
@Js
def PyJsHoisted_resistance_(d, i, reject, this, arguments, var=var):
    var = Scope({'i':i, 'arguments':arguments, 'd':d, 'reject':reject, 'this':this}, var)
    var.registers(['integral', 'd', 'i', 'metricPrefix', 'quantity', 'ohm', 'fractional', 'reject'])
    var.put('integral', var.get('d').get('0'))
    var.put('metricPrefix', var.get('d').get('2').get('0'))
    var.put('fractional', var.get('d').get('2').get('1'))
    var.put('ohm', var.get('d').get('2').get('2'))
    if var.get('fractional'):
        if JsRegExp('/\\./').callprop('test', var.get('integral').callprop('toString')):
            return var.get('reject')
        var.put('quantity', ((var.get('integral')+Js('.'))+var.get('fractional')))
    else:
        var.put('quantity', var.get('integral'))
    PyJs_Object_7_ = Js({'resistance':var.get('parseFloat')((var.get('quantity')+(var.get('metricPrefix') or Js(''))))})
    return PyJs_Object_7_
PyJsHoisted_resistance_.func_name = 'resistance'
var.put('resistance', PyJsHoisted_resistance_)
@Js
def PyJsHoisted_flatten_(arr, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'arr':arr, 'this':this}, var)
    var.registers(['arr'])
    return var.get('flat')(var.get('arr'), Js([]))
PyJsHoisted_flatten_.func_name = 'flatten'
var.put('flatten', PyJsHoisted_flatten_)
@Js
def PyJsHoisted_flat_(arr, res, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'res':res, 'arr':arr, 'this':this}, var)
    var.registers(['i', 'len', 'res', 'cur', 'arr'])
    var.put('i', Js(0.0))
    var.put('len', var.get('arr').get('length'))
    #for JS loop
    
    while (var.get('i')<var.get('len')):
        try:
            var.put('cur', var.get('arr').get(var.get('i')))
            (var.get('flat')(var.get('cur'), var.get('res')) if var.get('Array').callprop('isArray', var.get('cur')) else var.get('res').callprop('push', var.get('cur')))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('res')
PyJsHoisted_flat_.func_name = 'flat'
var.put('flat', PyJsHoisted_flat_)
@Js
def PyJsHoisted_capacitance_(d, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'd':d, 'this':this}, var)
    var.registers(['farad', 'metricPrefix', 'd', 'quantity'])
    var.put('quantity', var.get('d').get('0'))
    var.put('metricPrefix', var.get('d').get('2'))
    var.put('farad', var.get('d').get('4'))
    PyJs_Object_6_ = Js({'capacitance':var.get('parseFloat')((var.get('quantity')+(var.get('metricPrefix') or Js(''))))})
    return PyJs_Object_6_
PyJsHoisted_capacitance_.func_name = 'capacitance'
var.put('capacitance', PyJsHoisted_capacitance_)
@Js
def PyJsHoisted_type_(t, this, arguments, var=var):
    var = Scope({'arguments':arguments, 't':t, 'this':this}, var)
    var.registers(['t'])
    @Js
    def PyJs_anonymous_4_(d, this, arguments, var=var):
        var = Scope({'arguments':arguments, 'd':d, 'this':this}, var)
        var.registers(['d'])
        PyJs_Object_5_ = Js({'type':var.get('t')})
        return Js([PyJs_Object_5_]).callprop('concat', var.get('d'))
    PyJs_anonymous_4_._set_name('anonymous')
    return PyJs_anonymous_4_
PyJsHoisted_type_.func_name = 'type'
var.put('type', PyJsHoisted_type_)
pass
Js('use strict')
pass
pass
@Js
def PyJs_anonymous_0_(d, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'd':d, 'this':this}, var)
    var.registers(['d'])
    @Js
    def PyJs_anonymous_1_(t, this, arguments, var=var):
        var = Scope({'arguments':arguments, 't':t, 'this':this}, var)
        var.registers(['t'])
        return PyJsStrictNeq(var.get('t'),var.get(u"null"))
    PyJs_anonymous_1_._set_name('anonymous')
    return var.get('d').callprop('filter', PyJs_anonymous_1_)
PyJs_anonymous_0_._set_name('anonymous')
var.put('filter', PyJs_anonymous_0_)
@Js
def PyJs_anonymous_2_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return var.get(u"null")
PyJs_anonymous_2_._set_name('anonymous')
var.put('nuller', PyJs_anonymous_2_)
PyJs_Object_3_ = Js({'0402':Js('01005'),'0603':Js('0201'),'1005':Js('0402'),'1608':Js('0603'),'2012':Js('0805'),'2520':Js('1008'),'3216':Js('1206'),'3225':Js('1210'),'4516':Js('1806'),'4532':Js('1812'),'5025':Js('2010'),'6332':Js('2512')})
var.put('toImperial', PyJs_Object_3_)
pass
pass
pass
@Js
def PyJs_anonymous_8_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('yellow')
PyJs_anonymous_8_._set_name('anonymous')
var.put('alias_56', PyJs_anonymous_8_)
@Js
def PyJs_anonymous_9_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('e-12')
PyJs_anonymous_9_._set_name('anonymous')
var.put('alias_69', PyJs_anonymous_9_)
@Js
def PyJs_anonymous_10_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('e6  ')
PyJs_anonymous_10_._set_name('anonymous')
var.put('alias_72', PyJs_anonymous_10_)
@Js
def PyJs_anonymous_11_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('e9  ')
PyJs_anonymous_11_._set_name('anonymous')
var.put('alias_63', PyJs_anonymous_11_)
@Js
def PyJs_anonymous_12_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('P2H')
PyJs_anonymous_12_._set_name('anonymous')
var.put('alias_27', PyJs_anonymous_12_)
@Js
def PyJs_anonymous_13_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('C0G')
PyJs_anonymous_13_._set_name('anonymous')
var.put('alias_20', PyJs_anonymous_13_)
@Js
def PyJs_anonymous_14_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('T2H')
PyJs_anonymous_14_._set_name('anonymous')
var.put('alias_33', PyJs_anonymous_14_)
var.put('alias_45', var.get('nuller'))
@Js
def PyJs_anonymous_15_(d, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'd':d, 'this':this}, var)
    var.registers(['d'])
    return var.get('parseInt')(var.get('d').get('0').callprop('join', Js('')))
PyJs_anonymous_15_._set_name('anonymous')
var.put('alias_0', PyJs_anonymous_15_)
@Js
def PyJs_anonymous_16_(d, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'd':d, 'this':this}, var)
    var.registers(['d'])
    PyJs_Object_17_ = Js({'color':var.get('d').get('0')})
    return PyJs_Object_17_
PyJs_anonymous_16_._set_name('anonymous')
var.put('alias_52', PyJs_anonymous_16_)
@Js
def PyJs_anonymous_18_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('M7G')
PyJs_anonymous_18_._set_name('anonymous')
var.put('alias_22', PyJs_anonymous_18_)
@Js
def PyJs_anonymous_19_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('red')
PyJs_anonymous_19_._set_name('anonymous')
var.put('alias_53', PyJs_anonymous_19_)
@Js
def PyJs_anonymous_20_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('e-15')
PyJs_anonymous_20_._set_name('anonymous')
var.put('alias_70', PyJs_anonymous_20_)
@Js
def PyJs_anonymous_21_(d, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'd':d, 'this':this}, var)
    var.registers(['d'])
    PyJs_Object_22_ = Js({'characteristic':var.get('d').get('0').get('0')})
    return PyJs_Object_22_
PyJs_anonymous_21_._set_name('anonymous')
var.put('alias_18', PyJs_anonymous_21_)
@Js
def PyJs_anonymous_23_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('P3K')
PyJs_anonymous_23_._set_name('anonymous')
var.put('alias_40', PyJs_anonymous_23_)
var.put('alias_48', var.get('nuller'))
@Js
def PyJs_anonymous_24_(d, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'd':d, 'this':this}, var)
    var.registers(['d'])
    return var.get('d').callprop('join', Js('')).callprop('toUpperCase')
PyJs_anonymous_24_._set_name('anonymous')
var.put('alias_41', PyJs_anonymous_24_)
@Js
def PyJs_anonymous_25_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('e-9 ')
PyJs_anonymous_25_._set_name('anonymous')
var.put('alias_68', PyJs_anonymous_25_)
@Js
def PyJs_anonymous_26_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('L2G')
PyJs_anonymous_26_._set_name('anonymous')
var.put('alias_25', PyJs_anonymous_26_)
@Js
def PyJs_anonymous_27_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('green')
PyJs_anonymous_27_._set_name('anonymous')
var.put('alias_54', PyJs_anonymous_27_)
@Js
def PyJs_anonymous_28_(d, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'd':d, 'this':this}, var)
    var.registers(['d'])
    PyJs_Object_29_ = Js({'tolerance':var.get('d').get('1')})
    return PyJs_Object_29_
PyJs_anonymous_28_._set_name('anonymous')
var.put('alias_42', PyJs_anonymous_28_)
var.put('alias_49', var.get('resistance'))
@Js
def PyJs_anonymous_30_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('orange')
PyJs_anonymous_30_._set_name('anonymous')
var.put('alias_57', PyJs_anonymous_30_)
@Js
def PyJs_anonymous_31_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('e-6 ')
PyJs_anonymous_31_._set_name('anonymous')
var.put('alias_75', PyJs_anonymous_31_)
@Js
def PyJs_anonymous_32_(d, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'd':d, 'this':this}, var)
    var.registers(['d'])
    return var.get('parseFloat')((((var.get('d').get('0') or Js(''))+var.get('d').get('1').callprop('join', Js('')))+((Js('.')+var.get('d').get('2').get('1').callprop('join', Js(''))) if var.get('d').get('2') else Js(''))))
PyJs_anonymous_32_._set_name('anonymous')
var.put('alias_3', PyJs_anonymous_32_)
@Js
def PyJs_anonymous_33_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('P3K')
PyJs_anonymous_33_._set_name('anonymous')
var.put('alias_39', PyJs_anonymous_33_)
var.put('alias_15', var.get('type')(Js('led')))
@Js
def PyJs_anonymous_34_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('e3  ')
PyJs_anonymous_34_._set_name('anonymous')
var.put('alias_73', PyJs_anonymous_34_)
@Js
def PyJs_anonymous_35_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('H2G')
PyJs_anonymous_35_._set_name('anonymous')
var.put('alias_24', PyJs_anonymous_35_)
@Js
def PyJs_anonymous_36_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('R2H')
PyJs_anonymous_36_._set_name('anonymous')
var.put('alias_30', PyJs_anonymous_36_)
@Js
def PyJs_anonymous_37_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('')
PyJs_anonymous_37_._set_name('anonymous')
var.put('alias_74', PyJs_anonymous_37_)
@Js
def PyJs_anonymous_38_(d, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'd':d, 'this':this}, var)
    var.registers(['d'])
    return var.get('toImperial').get(var.get('d').get('0'))
PyJs_anonymous_38_._set_name('anonymous')
var.put('alias_11', PyJs_anonymous_38_)
var.put('alias_16', var.get('nuller'))
var.put('alias_50', var.get('nuller'))
@Js
def PyJs_anonymous_39_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('C0G')
PyJs_anonymous_39_._set_name('anonymous')
var.put('alias_19', PyJs_anonymous_39_)
@Js
def PyJs_anonymous_40_(d, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'd':d, 'this':this}, var)
    var.registers(['d'])
    PyJs_Object_41_ = Js({'voltage_rating':var.get('d').get('0')})
    return PyJs_Object_41_
PyJs_anonymous_40_._set_name('anonymous')
var.put('alias_17', PyJs_anonymous_40_)
@Js
def PyJs_anonymous_42_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('P2H')
PyJs_anonymous_42_._set_name('anonymous')
var.put('alias_28', PyJs_anonymous_42_)
var.put('alias_14', var.get('type')(Js('resistor')))
@Js
def PyJs_anonymous_43_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('Q3K')
PyJs_anonymous_43_._set_name('anonymous')
var.put('alias_38', PyJs_anonymous_43_)
@Js
def PyJs_anonymous_44_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('e9  ')
PyJs_anonymous_44_._set_name('anonymous')
var.put('alias_71', PyJs_anonymous_44_)
@Js
def PyJs_anonymous_45_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('white')
PyJs_anonymous_45_._set_name('anonymous')
var.put('alias_58', PyJs_anonymous_45_)
@Js
def PyJs_anonymous_46_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('Q3K')
PyJs_anonymous_46_._set_name('anonymous')
var.put('alias_37', PyJs_anonymous_46_)
@Js
def PyJs_anonymous_47_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('U2J')
PyJs_anonymous_47_._set_name('anonymous')
var.put('alias_35', PyJs_anonymous_47_)
var.put('alias_43', var.get('capacitance'))
@Js
def PyJs_anonymous_48_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('H2G')
PyJs_anonymous_48_._set_name('anonymous')
var.put('alias_23', PyJs_anonymous_48_)
var.put('alias_13', var.get('type')(Js('capacitor')))
@Js
def PyJs_anonymous_49_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('e-6 ')
PyJs_anonymous_49_._set_name('anonymous')
var.put('alias_67', PyJs_anonymous_49_)
@Js
def PyJs_anonymous_50_(d, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'd':d, 'this':this}, var)
    var.registers(['d'])
    return var.get('toImperial').get(var.get('d').get('7'))
PyJs_anonymous_50_._set_name('anonymous')
var.put('alias_10', PyJs_anonymous_50_)
@Js
def PyJs_anonymous_51_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('e6  ')
PyJs_anonymous_51_._set_name('anonymous')
var.put('alias_64', PyJs_anonymous_51_)
@Js
def PyJs_anonymous_52_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('e-12')
PyJs_anonymous_52_._set_name('anonymous')
var.put('alias_77', PyJs_anonymous_52_)
@Js
def PyJs_anonymous_53_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('e-3 ')
PyJs_anonymous_53_._set_name('anonymous')
var.put('alias_66', PyJs_anonymous_53_)
@Js
def PyJs_anonymous_54_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return var.get(u"null")
PyJs_anonymous_54_._set_name('anonymous')
var.put('alias_6', PyJs_anonymous_54_)
var.put('alias_46', var.get('nuller'))
@Js
def PyJs_anonymous_55_(d, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'd':d, 'this':this}, var)
    var.registers(['d'])
    if var.get('d').get('0'):
        return var.get('parseInt')((var.get('d').get('0').get('0')+var.get('d').get('1').callprop('join', Js(''))))
    else:
        return var.get('parseInt')(var.get('d').get('1').callprop('join', Js('')))
PyJs_anonymous_55_._set_name('anonymous')
var.put('alias_1', PyJs_anonymous_55_)
@Js
def PyJs_anonymous_56_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('L2G')
PyJs_anonymous_56_._set_name('anonymous')
var.put('alias_26', PyJs_anonymous_56_)
@Js
def PyJs_anonymous_57_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('blue')
PyJs_anonymous_57_._set_name('anonymous')
var.put('alias_55', PyJs_anonymous_57_)
@Js
def PyJs_anonymous_58_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('R2H')
PyJs_anonymous_58_._set_name('anonymous')
var.put('alias_29', PyJs_anonymous_58_)
@Js
def PyJs_anonymous_59_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('T2H')
PyJs_anonymous_59_._set_name('anonymous')
var.put('alias_34', PyJs_anonymous_59_)
@Js
def PyJs_anonymous_60_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('U2J')
PyJs_anonymous_60_._set_name('anonymous')
var.put('alias_36', PyJs_anonymous_60_)
@Js
def PyJs_anonymous_61_(d, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'd':d, 'this':this}, var)
    var.registers(['d'])
    PyJs_Object_62_ = Js({'size':var.get('filter')(var.get('flatten')(var.get('d'))).get('0')})
    return PyJs_Object_62_
PyJs_anonymous_61_._set_name('anonymous')
var.put('alias_8', PyJs_anonymous_61_)
@Js
def PyJs_anonymous_63_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return var.get(u"null")
PyJs_anonymous_63_._set_name('anonymous')
var.put('alias_7', PyJs_anonymous_63_)
@Js
def PyJs_anonymous_64_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('amber')
PyJs_anonymous_64_._set_name('anonymous')
var.put('alias_59', PyJs_anonymous_64_)
@Js
def PyJs_anonymous_65_(d, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'd':d, 'this':this}, var)
    var.registers(['metricPrefix', 'd', 'quantity'])
    var.put('quantity', var.get('d').get('0'))
    var.put('metricPrefix', var.get('d').get('2'))
    PyJs_Object_66_ = Js({'power_rating':var.get('parseFloat')((var.get('quantity')+(var.get('metricPrefix') or Js(''))))})
    return PyJs_Object_66_
PyJs_anonymous_65_._set_name('anonymous')
var.put('alias_47', PyJs_anonymous_65_)
@Js
def PyJs_anonymous_67_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('S2H')
PyJs_anonymous_67_._set_name('anonymous')
var.put('alias_31', PyJs_anonymous_67_)
@Js
def PyJs_anonymous_68_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('S2H')
PyJs_anonymous_68_._set_name('anonymous')
var.put('alias_32', PyJs_anonymous_68_)
@Js
def PyJs_anonymous_69_(d, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'd':d, 'this':this}, var)
    var.registers(['d'])
    return var.get('parseFloat')((var.get('d').get('0').callprop('join', Js(''))+((Js('.')+var.get('d').get('1').get('1').callprop('join', Js(''))) if var.get('d').get('1') else Js(''))))
PyJs_anonymous_69_._set_name('anonymous')
var.put('alias_2', PyJs_anonymous_69_)
@Js
def PyJs_anonymous_70_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('yellow green')
PyJs_anonymous_70_._set_name('anonymous')
var.put('alias_62', PyJs_anonymous_70_)
@Js
def PyJs_anonymous_71_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('e-9 ')
PyJs_anonymous_71_._set_name('anonymous')
var.put('alias_76', PyJs_anonymous_71_)
@Js
def PyJs_anonymous_72_(d, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'd':d, 'this':this}, var)
    var.registers(['d'])
    return var.get('filter')(var.get('flatten')(var.get('d')))
PyJs_anonymous_72_._set_name('anonymous')
var.put('alias_12', PyJs_anonymous_72_)
@Js
def PyJs_anonymous_73_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('purple')
PyJs_anonymous_73_._set_name('anonymous')
var.put('alias_61', PyJs_anonymous_73_)
@Js
def PyJs_anonymous_74_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('cyan')
PyJs_anonymous_74_._set_name('anonymous')
var.put('alias_60', PyJs_anonymous_74_)
var.put('alias_51', var.get('nuller'))
@Js
def PyJs_anonymous_75_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('e3  ')
PyJs_anonymous_75_._set_name('anonymous')
var.put('alias_65', PyJs_anonymous_75_)
@Js
def PyJs_anonymous_76_(d, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'd':d, 'this':this}, var)
    var.registers(['d'])
    return (var.get('d').get('0')/Js(100.0))
PyJs_anonymous_76_._set_name('anonymous')
var.put('alias_4', PyJs_anonymous_76_)
@Js
def PyJs_anonymous_77_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return Js('M7G')
PyJs_anonymous_77_._set_name('anonymous')
var.put('alias_21', PyJs_anonymous_77_)
@Js
def PyJs_anonymous_78_(d, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'd':d, 'this':this}, var)
    var.registers(['d'])
    return var.get('toImperial').get(var.get('d').get('0'))
PyJs_anonymous_78_._set_name('anonymous')
var.put('alias_9', PyJs_anonymous_78_)
var.put('alias_44', var.get('capacitance'))
@Js
def PyJs_anonymous_79_(d, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'd':d, 'this':this}, var)
    var.registers(['d'])
    return var.get('parseFloat')(((((var.get('d').get('0') or Js(''))+var.get('d').get('1').callprop('join', Js('')))+((Js('.')+var.get('d').get('2').get('1').callprop('join', Js(''))) if var.get('d').get('2') else Js('')))+(((Js('e')+(var.get('d').get('3').get('1') or Js('+')))+var.get('d').get('3').get('2').callprop('join', Js(''))) if var.get('d').get('3') else Js(''))))
PyJs_anonymous_79_._set_name('anonymous')
var.put('alias_5', PyJs_anonymous_79_)
pass

class TranformNearley(Transformer):
    alias_56 = var.get('alias_56').to_python()
    alias_69 = var.get('alias_69').to_python()
    alias_72 = var.get('alias_72').to_python()
    alias_63 = var.get('alias_63').to_python()
    alias_27 = var.get('alias_27').to_python()
    alias_20 = var.get('alias_20').to_python()
    alias_33 = var.get('alias_33').to_python()
    alias_45 = var.get('alias_45').to_python()
    alias_0 = var.get('alias_0').to_python()
    alias_52 = var.get('alias_52').to_python()
    alias_22 = var.get('alias_22').to_python()
    alias_53 = var.get('alias_53').to_python()
    alias_70 = var.get('alias_70').to_python()
    alias_18 = var.get('alias_18').to_python()
    alias_40 = var.get('alias_40').to_python()
    alias_48 = var.get('alias_48').to_python()
    alias_41 = var.get('alias_41').to_python()
    alias_68 = var.get('alias_68').to_python()
    alias_25 = var.get('alias_25').to_python()
    alias_54 = var.get('alias_54').to_python()
    alias_42 = var.get('alias_42').to_python()
    alias_49 = var.get('alias_49').to_python()
    alias_57 = var.get('alias_57').to_python()
    alias_75 = var.get('alias_75').to_python()
    alias_3 = var.get('alias_3').to_python()
    alias_39 = var.get('alias_39').to_python()
    alias_15 = var.get('alias_15').to_python()
    alias_73 = var.get('alias_73').to_python()
    alias_24 = var.get('alias_24').to_python()
    alias_30 = var.get('alias_30').to_python()
    alias_74 = var.get('alias_74').to_python()
    alias_11 = var.get('alias_11').to_python()
    alias_16 = var.get('alias_16').to_python()
    alias_50 = var.get('alias_50').to_python()
    alias_19 = var.get('alias_19').to_python()
    alias_17 = var.get('alias_17').to_python()
    alias_28 = var.get('alias_28').to_python()
    alias_14 = var.get('alias_14').to_python()
    alias_38 = var.get('alias_38').to_python()
    alias_71 = var.get('alias_71').to_python()
    alias_58 = var.get('alias_58').to_python()
    alias_37 = var.get('alias_37').to_python()
    alias_35 = var.get('alias_35').to_python()
    alias_43 = var.get('alias_43').to_python()
    alias_23 = var.get('alias_23').to_python()
    alias_13 = var.get('alias_13').to_python()
    alias_67 = var.get('alias_67').to_python()
    alias_10 = var.get('alias_10').to_python()
    alias_64 = var.get('alias_64').to_python()
    alias_77 = var.get('alias_77').to_python()
    alias_66 = var.get('alias_66').to_python()
    alias_6 = var.get('alias_6').to_python()
    alias_46 = var.get('alias_46').to_python()
    alias_1 = var.get('alias_1').to_python()
    alias_26 = var.get('alias_26').to_python()
    alias_55 = var.get('alias_55').to_python()
    alias_29 = var.get('alias_29').to_python()
    alias_34 = var.get('alias_34').to_python()
    alias_36 = var.get('alias_36').to_python()
    alias_8 = var.get('alias_8').to_python()
    alias_7 = var.get('alias_7').to_python()
    alias_59 = var.get('alias_59').to_python()
    alias_47 = var.get('alias_47').to_python()
    alias_31 = var.get('alias_31').to_python()
    alias_32 = var.get('alias_32').to_python()
    alias_2 = var.get('alias_2').to_python()
    alias_62 = var.get('alias_62').to_python()
    alias_76 = var.get('alias_76').to_python()
    alias_12 = var.get('alias_12').to_python()
    alias_61 = var.get('alias_61').to_python()
    alias_60 = var.get('alias_60').to_python()
    alias_51 = var.get('alias_51').to_python()
    alias_65 = var.get('alias_65').to_python()
    alias_4 = var.get('alias_4').to_python()
    alias_21 = var.get('alias_21').to_python()
    alias_9 = var.get('alias_9').to_python()
    alias_44 = var.get('alias_44').to_python()
    alias_5 = var.get('alias_5').to_python()
    __default__ = lambda self, n, c: c if c else None

parser = Lark(grammar, start="n_main")
def parse(text):
    return TranformNearley().transform(parser.parse(text))


resDict = {
    1 :  1,
    2 :  2,
    3 :  3,
    4 :  4,
    5 :  5,
    6 :  6,
    7 :  7,
    8 :  8,
    9 :  9,
    10 :  10,
    11 :  11,
    12 :  12,
    13 :  13,
    14 :  14,
    15 :  15,
    16 :  16,
    17 :  17,
    18 :  18,
    19 :  19,
    20 :  20,
    21 :  22,
    22 :  22,
    23 :  23,
    24 :  25,
    25 :  25,
    26 :  26,
    27 :  28,
    28 :  28,
    29 :  29,
    30 :  29,
    31 :  33,
    32 :  33,
    33 :  33,
    34 :  33,
    35 :  36,
    36 :  36,
    37 :  36,
    38 :  39,
    39 :  39,
    40 :  40,
    41 :  40,
    42 :  44,
    43 :  44,
    44 :  44,
    45 :  45,
    46 :  46,
    47 :  47,
    48 :  48,
    49 :  49,
    50 :  50,
    51 :  50,
    52 :  50,
    53 :  55,
    54 :  55,
    55 :  55,
    56 :  56,
    57 :  58,
    58 :  58,
    59 :  59,
    60 :  59,
    61 :  59,
    62 :  59,
    63 :  66,
    64 :  66,
    65 :  66,
    66 :  66,
    67 :  66,
    68 :  69,
    69 :  69,
    70 :  70,
    71 :  70,
    72 :  70,
    73 :  70,
    74 :  77,
    75 :  77,
    76 :  77,
    77 :  77,
    78 :  78,
    79 :  79,
    80 :  80,
    81 :  80,
    82 :  80,
    83 :  80,
    84 :  88,
    85 :  88,
    86 :  88,
    87 :  88,
    88 :  88,
    89 :  89,
    90 :  89,
    91 :  89,
    92 :  89,
    93 :  89,
    94 :  99,
    95 :  99,
    96 :  99,
    97 :  99,
    98 :  99,
    99 :  99,
    100 :  100,
    101 :  100,
    102 :  100,
    103 :  100,
    104 :  100,
    105 :  110,
    106 :  110,
    107 :  110,
    108 :  110,
    109 :  110,
    110 :  110,
    111 :  111,
    112 :  112,
    113 :  113,
    114 :  114,
    115 :  115,
    116 :  116,
    117 :  117,
    118 :  118,
    119 :  119,
    120 :  120,
    121 :  122,
    122 :  122,
    123 :  123,
    124 :  125,
    125 :  125,
    126 :  126,
    127 :  128,
    128 :  128,
    129 :  129,
    130 :  129,
    131 :  133,
    132 :  133,
    133 :  133,
    134 :  133,
    135 :  136,
    136 :  136,
    137 :  136,
    138 :  139,
    139 :  139,
    140 :  140,
    141 :  140,
    142 :  144,
    143 :  144,
    144 :  144,
    145 :  145,
    146 :  146,
    147 :  147,
    148 :  148,
    149 :  149,
    150 :  150,
    151 :  150,
    152 :  150,
    153 :  155,
    154 :  155,
    155 :  155,
    156 :  156,
    157 :  158,
    158 :  158,
    159 :  159,
    160 :  159,
    161 :  159,
    162 :  159,
    163 :  166,
    164 :  166,
    165 :  166,
    166 :  166,
    167 :  166,
    168 :  169,
    169 :  169,
    170 :  170,
    171 :  170,
    172 :  170,
    173 :  170,
    174 :  177,
    175 :  177,
    176 :  177,
    177 :  177,
    178 :  178,
    179 :  179,
    180 :  180,
    181 :  180,
    182 :  180,
    183 :  180,
    184 :  188,
    185 :  188,
    186 :  188,
    187 :  188,
    188 :  188,
    189 :  189,
    190 :  189,
    191 :  189,
    192 :  189,
    193 :  189,
    194 :  199,
    195 :  199,
    196 :  199,
    197 :  199,
    198 :  199,
    199 :  199,
    200 :  200,
}


def main():
    t = int(input())
    for i in range(t):
        target = int(input())
        print(resDict[target])

main()
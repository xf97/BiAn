'''
Info:
This program was developed by daejunpark, 
you can find it in this git repository:
https://github.com/daejunpark/evm-disassembler/.
'''

#Error: sometime it runs wrong! need modify

#!/usr/bin/env python

import sys

opcodes = {
    '00' : 'STOP',
    '01' : 'ADD',
    '02' : 'MUL',
    '03' : 'SUB',
    '04' : 'DIV',
    '05' : 'SDIV',
    '06' : 'MOD',
    '07' : 'SMOD',
    '08' : 'ADDMOD',
    '09' : 'MULMOD',
    '0a' : 'EXP',
    '0b' : 'SIGNEXTEND',
    '10' : 'LT',
    '11' : 'GT',
    '12' : 'SLT',
    '13' : 'SGT',
    '14' : 'EQ',
    '15' : 'ISZERO',
    '16' : 'AND',
    '17' : 'OR', # 'EVMOR'
    '18' : 'XOR',
    '19' : 'NOT',
    '1a' : 'BYTE',
    '1b' : 'SHL',
    '1c' : 'SHR',
    '1d' : 'SAR',
    '20' : 'SHA3',
    '30' : 'ADDRESS',
    '31' : 'BALANCE',
    '32' : 'ORIGIN',
    '33' : 'CALLER',
    '34' : 'CALLVALUE',
    '35' : 'CALLDATALOAD',
    '36' : 'CALLDATASIZE',
    '37' : 'CALLDATACOPY',
    '38' : 'CODESIZE',
    '39' : 'CODECOPY',
    '3a' : 'GASPRICE',
    '3b' : 'EXTCODESIZE',
    '3c' : 'EXTCODECOPY',
    '3d' : 'RETURNDATASIZE',
    '3e' : 'RETURNDATACOPY',
    '3f' : 'EXTCODEHASH',
    '40' : 'BLOCKHASH',
    '41' : 'COINBASE',
    '42' : 'TIMESTAMP',
    '43' : 'NUMBER',
    '44' : 'DIFFICULTY',
    '45' : 'GASLIMIT',
    '50' : 'POP',
    '51' : 'MLOAD',
    '52' : 'MSTORE',
    '53' : 'MSTORE8',
    '54' : 'SLOAD',
    '55' : 'SSTORE',
    '56' : 'JUMP',
    '57' : 'JUMPI',
    '58' : 'PC',
    '59' : 'MSIZE',
    '5a' : 'GAS',
    '5b' : 'JUMPDEST',
    '60' : 'PUSH1',
    '61' : 'PUSH2',
    '62' : 'PUSH3',
    '63' : 'PUSH4',
    '64' : 'PUSH5',
    '65' : 'PUSH6',
    '66' : 'PUSH7',
    '67' : 'PUSH8',
    '68' : 'PUSH9',
    '69' : 'PUSH10',
    '6a' : 'PUSH11',
    '6b' : 'PUSH12',
    '6c' : 'PUSH13',
    '6d' : 'PUSH14',
    '6e' : 'PUSH15',
    '6f' : 'PUSH16',
    '70' : 'PUSH17',
    '71' : 'PUSH18',
    '72' : 'PUSH19',
    '73' : 'PUSH20',
    '74' : 'PUSH21',
    '75' : 'PUSH22',
    '76' : 'PUSH23',
    '77' : 'PUSH24',
    '78' : 'PUSH25',
    '79' : 'PUSH26',
    '7a' : 'PUSH27',
    '7b' : 'PUSH28',
    '7c' : 'PUSH29',
    '7d' : 'PUSH30',
    '7e' : 'PUSH31',
    '7f' : 'PUSH32',
    '80' : 'DUP1',
    '81' : 'DUP2',
    '82' : 'DUP3',
    '83' : 'DUP4',
    '84' : 'DUP5',
    '85' : 'DUP6',
    '86' : 'DUP7',
    '87' : 'DUP8',
    '88' : 'DUP9',
    '89' : 'DUP10',
    '8a' : 'DUP11',
    '8b' : 'DUP12',
    '8c' : 'DUP13',
    '8d' : 'DUP14',
    '8e' : 'DUP15',
    '8f' : 'DUP16',
    '90' : 'SWAP1',
    '91' : 'SWAP2',
    '92' : 'SWAP3',
    '93' : 'SWAP4',
    '94' : 'SWAP5',
    '95' : 'SWAP6',
    '96' : 'SWAP7',
    '97' : 'SWAP8',
    '98' : 'SWAP9',
    '99' : 'SWAP10',
    '9a' : 'SWAP11',
    '9b' : 'SWAP12',
    '9c' : 'SWAP13',
    '9d' : 'SWAP14',
    '9e' : 'SWAP15',
    '9f' : 'SWAP16',
    'a0' : 'LOG0',
    'a1' : 'LOG1',
    'a2' : 'LOG2',
    'a3' : 'LOG3',
    'a4' : 'LOG4',
    'f0' : 'CREATE',
    'f1' : 'CALL',
    'f2' : 'CALLCODE',
    'f3' : 'RETURN',
    'f4' : 'DELEGATECALL',
    'f5' : 'CREATE2',
    'fa' : 'STATICCALL',
    'fd' : 'REVERT',
    'fe' : 'INVALID',
    'ff' : 'SELFDESTRUCT',
#   'ff' : 'SUICIDE',
}

def push_bytes(h, mode):
    i = str(int(h, 16))
    return {
        'hex'     :           '0x' + h  ,
        'int'     : i                   ,
        'int:hex' : i + ':' + '0x' + h  ,
    }[mode]

def pc(cnt, size):
    return '[' + str(cnt).zfill(size) + ']'

# Decode ByteCodes to Opcodes
def decode(hexcode, mode):
    size = len(str(len(hexcode)))
    h = ''
    o = ''
    pushcnt = 0
    cnt = -1
    for item in hexcode:
        cnt += 1
        if pushcnt > 0:
            h += item.lower()
            pushcnt -= 1
            if pushcnt == 0:
                i = str(int(h, 16))
                o += push_bytes(h, mode) + '\n'
                h = ''
        elif isinstance(item, str) and item.lower() in opcodes:
            o += pc(cnt, size) + ' ' + item.lower() + ' ' + opcodes[item.lower()]
            if int('60', 16) <= int(item, 16) <= int('7f', 16):
                pushcnt = int(item, 16) - int('60', 16) + 1
                o += ' '
            else:
                o += '\n'
        else:
            o += pc(cnt, size) + ' ' + item.lower() + ' ERROR\n'
#           raise Exception("Invalid opcode: " + str(item))
    if h:
        o += 'ERROR ' + push_bytes(h, mode) + ' (' + str(pushcnt) + ' bytes missed)\n'
#       raise Exception("Not enough push bytes: " + h)
    return o.strip()

# usage: <cmd> [int|hex|int:hex]
if __name__ == '__main__':
    mode = 'int:hex' if len(sys.argv) < 2 else sys.argv[1]
    hexcode=input()
    print(decode([hexcode[i:i+2] for i in range(2, len(hexcode), 2)], mode))
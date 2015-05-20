import struct

from disasm import H8ImmOper, H8RegDirOper, H8RegIndirOper, H8AbsAddrOper
from regs import metaFrom8, metaFrom16
from const import *

def p_CCR_Rd(va, val, buf, off, tsize):
    # stc
    iflags = 0
    op = val>>4
    rd = val & 0xf
    opers = (
            H8RegDirOper(REG_FLAGS, 4, va),
            H8RegDirOper(rd, tsize, va),
            )
    return (op, None, opers, iflags, 2)

def p_Rs_CCR(va, val, buf, off, tsize):
    # ldc
    iflags = 0
    op = val>>4
    rs = metaFrom8(val & 0xf)
    opers = (
            H8RegDirOper(rs, tsize, va),
            H8RegDirOper(REG_FLAGS, tsize, va),
            )
    return (op, None, opers, iflags, 2)

def p_aAA8_Rd(va, val, buf, off, tsize):
    # mov 0x2###
    iflags = 0
    op = val>>12
    Rd = convertMeta((val >> 8) & 0xf, tsize)
    aAA8 = val & 0xf

    opers = (
            H8RegDirOper(Rn, tsize, va, 0),
            H8AbsAddrOper(aAA8),
            )
    return (op, None, opers, iflags, 2)

def p_Rs_aAA8(va, val, buf, off, tsize):
    # mov 0x3###
    iflags = 0
    op = val>>12
    Rs = convertMeta((val >> 8) & 0xf, tsize)
    aAA8 = val & 0xf

    opers = (
            H8AbsAddrOper(aAA8),
            H8RegDirOper(Rn, tsize, va, 0),
            )
    return (op, None, opers, iflags, 2)

def p_i2(va, val, buf, off, tsize):
    # trapa
    iflags = 0
    op = 0x57
    i2 = (val >> 4) & 0x3

    opers = (
            H8ImmOper(i2),
            )
    return (op, None, opers, iflags, 2)

def p_i3_Rd(va, val, buf, off, tsize):
    # band, bclr, biand, bild, bior, bist, bixor, bld, bnot, bor, bset, bst, btst, bxor
    iflags = 0
    op = val >> 7
    i3 = (val >> 4) & 0x7
    Rd = convertMeta(val & 0xf, tsize)

    opers = (
            H8ImmOper(i3),
            H8RegDirOper(Rd, tsize, va, 0),
            )
    return (op, None, opers, iflags, 2)

def p_i3_aERd(va, val, buf, off, tsize): 
    # band, bclr, biand, bild, bior, bist, bixor, bld, bnot, bor, bset, bst, btst, bxor
    val2, = struct.unpack('>H', buf[off+2: off+4])

    iflags = 0
    op = ((((val >> 3)&0xfff0) | (val&0xf))<<13) | ((val2>>3)&0xfff0) | (val&0xf)
    i3 = (val2 >> 4) & 0x7
    ERd = (val >> 4) & 0x7

    opers = (
            H8ImmOper(i3),
            H8RegIndirOper(ERd, tsize, va, 0),
            )
    return (op, None, opers, iflags, 4)

def p_i3_aAA8(va, val, buf, off, tsize): 
    # band, bclr, biand, bild, bior, bist, bixor, bld, bnot, bor, bset, bst, btst, bxor
    val2, = struct.unpack('>H', buf[off+2: off+4])

    iflags = 0
    op = (val >> 16) | (val&0xf) | (val2>>15) | (val&0xf)
    i3 = (val2 >> 4) & 0x7
    aa = val & 0xff

    opers = (
            H8ImmOper(i3),
            H8AbsAddrOper(aa),
            )
    return (op, None, opers, iflags, 4)

def p_i8_CCR(va, val, buf, off, tsize): 
    # andc
    iflags = 0
    op = val >> 8
    i8 = val & 0xff

    opers = (
            H8ImmOper(i8),
            )
    return (op, None, opers, iflags, 2)

def p_i8_Rd(va, val, buf, off, tsize): 
    # add.b, addx, and.b, cmp.b
    iflags = 0
    op = val >> 4
    i8 = val & 0xff
    Rd = (val >> 8) & 0xf

    opers = (
            H8ImmOper(i8),
            H8RegDirOper(Rd, tsize, va, 0),
            )
    return (op, None, opers, iflags, 2)

def p_i16_Rd(va, val, buf, off, tsize): 
    # add.w, and.w, cmp.w
    val2, = struct.unpack('>H', buf[off+2: off+4])

    iflags = 0
    op = val >> 4
    i16 = val2
    Rd = val & 0xf

    opers = (
            H8ImmOper(i16),
            H8RegDirOper(Rd, tsize, va, 0),
            )
    return (op, None, opers, iflags, 4)

def p_i32_ERd(va, val, buf, off, tsize): 
    # add.l, and.l, cmp.l
    val2, = struct.unpack('>I', buf[off+2: off+6])

    iflags = 0
    op = val >> 3
    i32 = val2
    ERd = val & 0x7

    opers = (
            H8ImmOper(i32),
            H8RegIndirOper(ERd, tsize, va, 0),
            )
    return (op, None, opers, iflags, 6)

def p_Rd(va, val, buf, off, tsize): 
    # daa, das, dec.b, exts.w, extu.w, inc.b
    iflags = 0
    op = val >> 4
    Rd = val & 0xf

    opers = (
            H8RegDirOper(Rd, tsize, va, 0),
            )
    return (op, None, opers, iflags, 2)

def p_Rs_Rd(va, val, buf, off, tsize):  
    # add.b, add.w, addx, and.b, and.w, cmp.b, cmp.w, divxu.b
    iflags = 0
    op = val >> 16
    Rs = (val >> 4) & 0xf
    Rd = val & 0xf

    opers = (
            H8RegDirOper(Rs, tsize, va, 0),
            H8RegDirOper(Rd, tsize, va, 0),
            )
    return (op, None, opers, iflags, 2)

def p_Rs_Rd_4b(va, val, buf, off, tsize):  
    # divxs.b
    val2, = struct.unpack('>H', buf[off+2: off+4])
    iflags = 0
    op = (val << 8) | (val2 >> 8)
    Rs = (val2 >> 4) & 0xf
    Rd = val2 & 0xf

    opers = (
            H8RegDirOper(Rs, tsize, va, 0),
            H8RegDirOper(Rd, tsize, va, 0),
            )
    return (op, None, opers, iflags, 4)

def p_Rs_ERd(va, val, buf, off, tsize):  
    # mulxu.w, divxu.w
    iflags = 0
    op = ((val >> 8) << 1) | ((val >> 3) & 1)
    Rs = (val >> 4) & 0xf
    ERd = val & 0x7

    # FIXME: make sure ER# and R# have correct metaregister values
    opers = (
            H8RegDirOper(Rs, tsize, va, 0),
            H8RegDirOper(ERd, tsize, va, 0),
            )
    return (op, None, opers, iflags, 2)


def p_ERs_ERd(va, val, buf, off, tsize):  
    # add.l, cmp.l
    iflags = 0
    op = ((val >> 7)&0xfffe) | (val&1)
    ERs = (val >> 4) & 0x7
    ERd = val & 0x7

    opers = (
            H8RegDirOper(Rs, tsize, va, 0),
            H8RegDirOper(ERd, tsize, va, 0),
            )
    return (op, None, opers, iflags, 2)

def p_Rs_ERd_4b(va, val, buf, off, tsize):  
    # divxs.w
    val2, = struct.unpack('>H', buf[off+2: off+4])
    iflags = 0
    op = (val << 8) | (val2 >> 8)
    Rs = (val2 >> 4) & 0xf
    ERd = val2 & 0x7

    opers = (
            H8RegDirOper(Rs, tsize, va, 0),
            H8RegDirOper(ERd, tsize, va, 0),
            )
    return (op, None, opers, iflags, 4)


def p_ERd(va, val, buf, off, tsize):  
    # exts.l, extu.l
    iflags = 0
    op = val >> 4
    ERd = val & 0x7

    opers = (
            H8RegDirOper(ERd, tsize, va, 0),
            )
    return (op, None, opers, iflags, 2)

def p_ERs_ERd_4b(va, val, buf, off, tsize):  
    # and.l, or.l
    val2, = struct.unpack('>H', buf[off+2: off+4])

    iflags = 0
    op = (val << 2) | ((val2 >> 6)&2) | ((val2 >> 3)&1)
    ERs = (val2 >> 4) & 0x7
    ERd = val2 & 0x7

    opers = (
            H8RegDirOper(ERs, tsize, va, 0),
            H8RegDirOper(ERd, tsize, va, 0),
            )
    return (op, None, opers, iflags, 4)

def p_Rn_Rd(va, val, buf, off, tsize):  
    # bclr, bset, btst
    iflags = 0
    op = val >> 8
    Rn = (val >> 4) & 0xf
    Rd = val & 0xf

    opers = (
            H8RegDirOper(Rn, tsize, va, 0),
            H8RegDirOper(Rd, tsize, va, 0),
            )
    return (op, None, opers, iflags, 2)

def p_aERs_Rd(va, val, buf, off, tsize):  
    # mov 0x68
    iflags = 0
    op = (val >> 7)
    aERs = (val >> 4) & 0x7
    Rd = (val) & 0xf

    opers = (
            H8RegIndirOper(aERs, tsize, va, disp=0, oflags=0),
            H8RegDirOper(Rd, tsize, va, 0),
            )
    return (op, None, opers, iflags, 4)

def p_Rn_aERd(va, val, buf, off, tsize):  
    # bclr, bset, btst
    val2, = struct.unpack('>H', buf[off+2: off+4])

    iflags = 0
    op = ((val >> 12)&0xfff0) | (val&0xf) | ((val2>>4)&0xfff0) | (val2&0xf)
    aERd = (val >> 4) & 0x7
    Rn = (val2 >> 4) & 0xf

    opers = (
            H8RegDirOper(Rn, tsize, va, 0),
            H8RegIndirOper(aERd, tsize, va, disp=0, oflags=0),
            )
    return (op, None, opers, iflags, 4)

def p_Rn_aAA8(va, val, buf, off, tsize):  
    # bclr, bset, btst
    val2, = struct.unpack('>H', buf[off+2: off+4])

    iflags = 0
    op = (val & 0xff00) | ((val2 >> 4)&0xff0) | (val2&0xf)
    Rn = (val2 >> 4) & 0xf
    aAA8 = val & 0xff

    opers = (
            H8RegDirOper(Rn, tsize, va, 0),
            H8AbsAddrOper(aAA8),
            )
    return (op, None, opers, iflags, 4)

def p_aERn(va, val, buf, off, tsize):  
    # jmp, jsr
    iflags = 0
    op = ((val >> 3)&0xfff0) | (val&0xf)
    aERn = (val >> 4) & 0x7

    opers = (
            H8RegIndirOper(aERn, tsize, va, 0),
            )
    return (op, None, opers, iflags, 2)

def p_aAA24(va, val, buf, off, tsize):  
    # jmp, jsr
    val2, = struct.unpack('>H', buf[off+2: off+4])

    iflags = 0
    op = val >> 8
    aAA24 = ((val&0xf) << 16) | val2

    opers = (
            H8AbsAddrOper(aAA24),
            )
    return (op, None, opers, iflags, 2)

def p_aaAA8(va, val, buf, off, tsize):  
    # jmp, jsr
    iflags = 0
    op = val >> 8
    aaAA8 = val & 0xff

    opers = (
            H8MemIndirOper(aaAA8),
            )
    return (op, None, opers, iflags, 2)

def p_1_Rd(va, val, buf, off, tsize):  
    # dec.w, inc.w
    iflags = 0
    op = val >> 4
    Rd = val & 0xf

    opers = (
            H8ImmOper(1),
            H8RegDirOper(Rd, tsize, va, 0),
            )
    return (op, None, opers, iflags, 2)

def p_2_Rd(va, val, buf, off, tsize):  
    # dec.w, inc.w
    iflags = 0
    op = val >> 4
    Rd = val & 0xf

    opers = (
            H8ImmOper(2),
            H8RegDirOper(Rd, tsize, va, 0),
            )
    return (op, None, opers, iflags, 2)

def p_4_Rd(va, val, buf, off, tsize):  
    # dec.w
    iflags = 0
    op = val >> 4
    Rd = val & 0xf

    opers = (
            H8ImmOper(4),
            H8RegDirOper(Rd, tsize, va, 0),
            )
    return (op, None, opers, iflags, 2)

def p_1_ERd(va, val, buf, off, tsize):  
    # adds, dec.l, inc.l
    iflags = 0
    op = val >> 3
    ERd = val & 0x7

    opers = (
            H8ImmOper(1),
            H8RegDirOper(ERd, tsize, va, 0),
            )
    return (op, None, opers, iflags, 2)

def p_2_ERd(va, val, buf, off, tsize):  
    # adds, dec.l, inc.l
    iflags = 0
    op = val >> 3
    ERd = val & 0x7

    opers = (
            H8ImmOper(1),
            H8RegDirOper(ERd, tsize, va, 0),
            )
    return (op, None, opers, iflags, 2)

def p_4_ERd(va, val, buf, off, tsize):  
    # adds, dec.l
    iflags = 0
    op = val >> 3
    ERd = val & 0x7

    opers = (
            H8ImmOper(1),
            H8RegDirOper(ERd, tsize, va, 0),
            )
    return (op, None, opers, iflags, 2)

def p_disp8(va, val, buf, off, tsize):  
    # bcc, bsr
    iflags = 0
    op = val >> 8
    disp8 = val & 0xff

    opers = (
            H8PcOffsetOper(disp8, va),
            )
    return (op, None, opers, iflags, 2)

def p_disp16(va, val, buf, off, tsize):  
    # bcc, bsr
    val2, = struct.unpack('>H', buf[off+2: off+4])

    iflags = 0
    op = val
    disp16 = val2
    
    mnem = None
    if (op & 0x800):
        opnibble = (val>>4) & 0xf
        mnem = bcc[opnibble]

    opers = (
            H8PcOffsetOper(disp16, va),
            )
    return (op, None, opers, iflags, 4)

def p_Rs_aAA16(va, val, buf, off, tsize):
    val2, = struct.unpack('>H', buf[off+2: off+4])

    iflags = 0
    op = val >> 4
    Rs = val & 0xf
    aAA16 = val2

    opers = (
            H8RegDirOper(Rs, tsize, va),
            H8AbsAddrOper(aAA16),
            )
    return (op, None, opers, iflags, 4)

def p_Rs_aAA24(va, val, buf, off, tsize):
    val2, = struct.unpack('>I', buf[off+2: off+6])

    iflags = 0
    op = val >> 4
    Rs = val & 0xf
    aAA24 = val2 & 0xffffff

    opers = (
            H8RegDirOper(Rs, tsize, va),
            H8AbsAddrOper(aAA24),
            )
    return (op, None, opers, iflags, 6)

def p_aAA16_Rd(va, val, buf, off, tsize):  
    val2, = struct.unpack('>H', buf[off+2: off+4])

    iflags = 0
    op = val >> 4
    Rd = val & 0xf
    aAA16 = val2

    opers = (
            H8AbsAddrOper(aAA16),
            H8RegDirOper(Rd, tsize, va),
            )
    return (op, None, opers, iflags, 4)

def p_aAA24_Rd(va, val, buf, off, tsize):  
    val2, = struct.unpack('>I', buf[off+2: off+6])

    iflags = 0
    op = val >> 4
    Rd = val & 0xf
    aAA16 = val2 & 0xffffff

    opers = (
            H8AbsAddrOper(aAA16),
            H8RegDirOper(Rd, tsize, va),
            )
    return (op, None, opers, iflags, 6)

def p_nooperands(va, val, buf, off, tsize):  
    # eepmov.b, eepmov.w, 
    iflags = 0
    op = val

    opers = ()
    return (op, None, opers, iflags, 2)

def _p_BccDoubles(va, vak, buf, off, tsize):
    # Bcc
    disp, = struct.unpack('>H', buf[off+2: off+4])
    op = val

    iflags = 0
    opnibble = (val>>4) & 0xf
    mnem = bcc[opnibble]

    opers = (
            H8PcOffsetOper(),
            )
    return (op, mnem, opers, iflags, 4)

bit_dbles = [
        ('error', 0),
        ('error', 0),
        ('error', 0),
        ('error', 0),
        ('error', 0),
        ('error', 0),
        ('bst', 0),
        ('bist', 0),
        ('bor', 0),
        ('bior', 0),
        ('bxor', 0),
        ('bixor', 0),
        ('band', 0),
        ('biand', 0),
        ('bld', 0),
        ('bild', 0),
        ]

def getBitDbl_OpMnem(val, bitlist=bit_dbles):
    op = val >> 7
    mnem, flags = bitlist[(op & 0x1f)]
    return op, mnem, flags

def p_Bit_Doubles(va, val, buf, off, tsize):
    op, mnem, iflags = getBitDbl_OpMnem(val)
    
    i3 = (val>>4) & 0x7
    Rd = val & 0xf

    opers = (
            H8ImmOper(i3),
            H8RegDirOper(Rd, tsize, va, 0),
            )
    return (op, mnem, opers, iflags, 2)

def p_Mov_6A(va, val, buf, off, tsize):
    op = val >> 4
    if op & 0x8:
        # Rs, @aa:16/24
        if op & 0x2:
            return p_Rs_aAA24(va, val, buf, off, tsize)
        return p_Rs_aAA16(va, val, buf, off, tsize)

    else:
        # @aa:16/24, Rd
        if op & 0x2:
            return p_aAA24_Rd(va, val, buf, off, tsize)

        return p_aAA16_Rd(va, val, buf, off, tsize)

def p_Mov_6C(va, val, buf, off, tsize):
    op = val >> 7
    if op & 0x1:
        # @ERs+, Rd
        return p_Rs_aAA16(va, val, buf, off, tsize)

    else:
        # @aa:16/24, Rd
        return p_aAA16_Rd(va, val, buf, off, tsize)

def p_Mov_78(va, val, buf, off, tsize):
    val2, val3_4 = struct.unpack(">HI", buf[off+2:off+8])

    op = (val3_4 >> 24) | ((val2&0xfff0)<<4) | ((val&0xff80)<<(20+1)) | ((val&0xf)<<20)
    #FIXME: complex and ugly.  do we even need these in this impl?

    mnem = None
    disp = val3_4 & 0xffffff

    # tsize is all over the map.  must determine here.
    tsz_opt = (val2 >> 8) & 1
    tsize = (1, 2)[tsz_opt]

    if (val2 & 8):
        ers = (val>>4) & 0x7
        rd  = val2 & 0xf
        opers = (
                H8RegIndirOper(ers, tsize, va, disp=disp, oflags=0),
                H8RegOper(rd),
                )
    else:
        erd = (val>>4) & 0x7
        rs  = val2 & 0xf
        opers = (
                H8RegOper(rs),
                H8RegIndirOper(erd, tsize, va, disp=disp, oflags=0),
                )

    return (op, mnem, opers, iflags, 2)

mnem_79a = (
        'mov',
        'add',
        'cmp',
        'sub',
        'or',
        'xor',
        'and',
        )

def p_79(va, val, buf, off, tsize):
    op, m, opers, iflags, osz = p_i16_Rd(va, val, buf, off, tsize)
    mnem = mnem_79a[(val>>4)&0xf]
    return op, mnem, opers, iflags, osz

def p_7a(va, val, buf, off, tsize):
    op, m, opers, iflags, osz = p_i32_ERd(va, val, buf, off, tsize)
    mnem = mnem_79a[(val>>4)&0xf]
    return op, mnem, opers, iflags, osz

def p_eepmov(va, val, buf, off, tsize):
    val2, = struct.unpack('>H', buf[off+2: off+4])
    op = (val<<8) | val2
    tsize = (1,2)[ (val>>7)&1]
    return op, None, (), 0, 4

def p_7c(va, val, buf, off, tsize):
    # btst, bor, bior, bxor, bixor, band, biand, bid, bild (erd)
    val2, = struct.unpack('>H', buf[off+2: off+4])
    iflags = 0
    op, mnem, flags = getBitDbl_OpMnem(val2)
    op |= ((val & 0xff80)<<9)

    telltale = (val2>>8) 
    
    # FIXME: is any of this redundant with previous encodings?
    if telltale == 0x63:
        # btst (0x####63##
        mnem = 'btst'
        erd = (val>>4) & 0x7
        rn = (val2>>4) & 0xf
        opers = (
                H8RegDirOper(rn, tsize=tsize),
                H8RegIndirOper(erd, tsize, va),
                )

    elif telltale == 0x73:
        # btst (0x####73##
        mnem = 'btst'
        erd = (val>>4) & 0x7
        imm = (val2>>4) & 0x7
        opers = (
                H8ImmOper(imm),
                H8RegIndirOper(erd, tsize, va),
                )

    elif 0x78 > telltale > 0x73:
        # other bit-halves:
        i3 = (val2>>4) & 0x7
        erd = (val >>4) & 0x7

        opers = (
                H8ImmOper(i3),
                H8RegIndirOper(erd, tsize, va, 0),
                )
    
    return op, mnem, opers, iflags, 4

bit_dble7df = [
        ('bset', 0),
        ('bset', 0),
        ('bnot', 0),
        ('bnot', 0),
        ('bclr', 0),
        ('bclr', 0),
        None, 
        None, 
        None, 
        None,
        None, 
        None, 
        None, 
        None,
        ('bst', 0),
        ('bist', 0),
        ]
bit_dble7df.extend(bit_dble7df)

def p_7d(va, val, buf, off, tsize):
    # bset, bnor, bclr, bst/bist
    val2, = struct.unpack('>H', buf[off+2: off+4])

    op, mnem, iflags = getBitDbl_OpMnem(val2, bit_dble7df)
    op |= ((val & 0xff80)<<9)

    erd = (val>>4) & 0x7
    imm = (val2>>4) & 0x7
    opers = (
            H8ImmOper(imm),
            H8RegIndirOper(erd, tsize, va)
            )

    return op, mnem, opers, iflags, 4

def p_7e(va, val, buf, off, tsize):
    # btst, bor, bior, bxor, bixor, band, biand, bid, bild (erd)
    val2, = struct.unpack('>H', buf[off+2: off+4])

    op, mnem, iflags = getBitDbl_OpMnem(val2)
    op |= ((val & 0xff80)<<9)
    aa = val & 0xff

    telltale = (val2>>8) 
    
    # FIXME: is any of this redundant with previous encodings?
    if telltale == 0x63:
        # btst (0x####63##
        mnem = 'btst'
        rn = (val2>>4) & 0xf
        opers = (
                H8RegDirOper(rn, tsize, va, 0),
                H8AbsAddrOper(aa, tsize=tsize),
                )

    elif telltale == 0x73:
        # btst (0x####73##
        mnem = 'btst'
        i3 = (val2>>4) & 0x7
        opers = (
                H8ImmOper(i3, tsize=tsize),
                H8AbsAddrOper(aa, tsize=tsize),
                )

    elif 0x78 > telltale > 0x73:
        # other bit-halves:
        i3 = (val2>>4) & 0x7

        opers = (
                H8ImmOper(i3),
                H8AbsAddrOper(aa, tsize=tsize),
                )
    
    return op, mnem, opers, iflags, 4

def p_7f(va, val, buf, off, tsize):
    # bset, bnor, bclr
    val2, = struct.unpack('>H', buf[off+2: off+4])

    op, mnem, iflags = getBitDbl_OpMnem(val2, bit_dble7df)
    op |= ((val & 0xff80)<<9)

    erd = (val>>4) & 0x7
    imm = (val2>>4) & 0x7
    opers = (
            H8ImmOper(imm),
            H8RegIndirOper(erd, tsize, va)
            )

    return op, mnem, opers, iflags, 4


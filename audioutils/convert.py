import ctypes
from ctypes.wintypes import LPCSTR, UINT
import os
import os.path

INFILE =os.path.join('audio', 'in.wav')
OUTFILE=os.path.join('audio', 'out.a18')
CHECKFILE=os.path.join('audio', 'out.wav')

a1800dll = ctypes.WinDLL('a1800.dll')

# enc doesn't seem to work - need to double-check the parms
encproto = ctypes.WINFUNCTYPE(ctypes.c_uint, LPCSTR, LPCSTR, UINT, ctypes.POINTER(UINT), UINT)
encparamflags = ((1, 'infile'), (1, 'outfile'), (1, 'samprate', 16000), (2, 'fh'), (1,'unk', 0))
encfunc = encproto(('enc', a1800dll), encparamflags)

decproto = ctypes.WINFUNCTYPE(ctypes.c_uint, LPCSTR, LPCSTR, ctypes.POINTER(UINT), UINT, UINT)
decparamflags = ((1, 'infile'), (1, 'outfile'), (2, 'fp'), (1, 'unk1', 16000), (1,'unk2', 0))
decfunc = decproto(('dec', a1800dll), decparamflags)

ret=encfunc(infile=LPCSTR(INFILE.encode('ascii')), outfile=LPCSTR(OUTFILE.encode('ascii')))
print(ret)
ret=decfunc(infile=LPCSTR(OUTFILE.encode('ascii')), outfile=LPCSTR(CHECKFILE.encode('ascii')))
print(ret)

#files=os.listdir('3410') # directory with the a18 files extracted from the DLC
#for f in files:
#   fname = '3410/' + f
#    outfile = 'wavs/' + f + '.wav' # directy to output to
#    print(fname)
#    decfunc(infile=LPCSTR(fname.encode('ascii')), outfile=LPCSTR(outfile.encode('ascii')))



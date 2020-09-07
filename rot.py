#!/usr/bin/env python3
import sys
from argparse import *

parser=ArgumentParser(prog='rots',usage='%(prog)s [Option]',epilog='Example: rot -r13 "hello world"',\
        description="ROT cipher is a simple cipher used in communition \
        Type \""+sys.argv[0]+" --show\" to display all ascii characters used in rot cipher. While encountering symbols like `,!\
        \', \", ;, which may be defined to process system commands to overcome the issue use \
        backslash(\"\\\") to return the appropriate output instead of getting an error.")
parser.add_argument('-r5','--rot5',help='rotate only numbers by 5 places',metavar='')
parser.add_argument('-r13','--rot13',help='rotate alphabets by 13 places(upper and lowercase alphabets',metavar='')
parser.add_argument('-r18','--rot18',help='rotate alphanumberic characters by 18 places.',metavar='')
parser.add_argument('-r47','--rot47',help='rotate symbols and alpha numberic characters by 47 places.',metavar='')
parser.add_argument('-a','--rotall',help='automate rot1-rot25 (upper and lowercase alphabets).',metavar='')
parser.add_argument('-r','--rot',help='shift/rotation to use(specify only after -a option)',type=int,metavar='',action='append')
parser.add_argument('-o','--output',help='output to the file',metavar='')
parser.add_argument('--show',help='show the ascii characters used in ROT ciphers.',action='store_true')
parser.add_argument('--sample',help='show sample inputs to be provided.', action='store_true')
args=parser.parse_args()

arg = sys.argv

class Rotate:
    """To manipulate ROT5 and ROT13"""

    def RotateString(gettuple):
        out=''
        shift=gettuple[0]
        rotatestring=gettuple[1]
        for i in rotatestring:
            if (ord(i)>=110) and (ord(i)<=122):
                if shift > 13:
                    count=ord(i) - (26-shift)
                else:
                    count = ord(i) + shift
                    if count > 122:
                        count=count-26
                out+=chr(count)
            elif (ord(i)>=97) and (ord(i)<=109):
                count=ord(i)+shift
                if count > 122:
                    count=count-26
                out+=chr(count)
            elif (ord(i)>=78) and (ord(i)<=90):
                if shift > 13:
                    count=ord(i) - (26 - shift)
                else:
                    count = ord(i) + shift
                    if count > 90:
                        count=count-26
                out+=chr(count)
            elif (ord(i)>=65) and (ord(i)<=77):
                count=ord(i) + shift
                if count > 90:
                    count = count - 26
                out+=chr(count)
            else:
                out+=i
        return out

    def RotateNum(getstring):
        out=""
        rotatenum=getstring
        for i in rotatenum:
            if (ord(i)>=53) and (ord(i)<=57):
                num=ord(i)
                out+=str(chr(num-5))
            elif (ord(i)>=48) and (ord(i)<=52):
                num=ord(i)
                out+=str(chr(num+5))
            else:
                out+=i
        return out

def rot5():
    try:
        global rot5
        rot5=args.rot5
        print(f"[+]ROT5 \t:\t"+Rotate.RotateNum(rot5))
    except:
        pass
    finally:
        rot13()

def rot13():
    try:
        global shift_1,rot13
        if args.rot13:
            rot13=args.rot13
            shift_1=13
            print(f'[+]ROT{shift_1}\t:\t'+Rotate.RotateString((shift_1,rot13)))
    except:
        pass
    finally:
        rot18()

def rot18():
    try:
        global shift_3,rot18
        if args.rot18:
            rot18=args.rot18
            shift_3=13
            StringResponse = Rotate.RotateString((shift_3,rot18))
            NumResponse = Rotate.RotateNum(StringResponse) 
            print(f'[+]ROT18\t:\t'+NumResponse)
    except:
        pass
    finally:
        rot47()

def rot47():
    try:
        out=""
        shift=47
        for i in args.rot47:
            if (ord(i)>=80) and (ord(i)<=126):
                count = ord(i) - shift
                out += chr(count)
            elif (ord(i) >= 33) and (ord(i) <= 79):
                count = ord(i) + shift
                out += chr(count)
            else:
                out += i
        print(f'[+]ROT47\t:\t{out}')
    except:
        pass
    finally:
        rot1_25()

def rot1_25():
    try:
        global shift_2,rotall
        if args.rotall:
            n=26;rotall = args.rotall
            if args.rot:#print(args.rot)
                print('\nCustom ROT cipher declared by @user')
                for i in args.rot:
                    shift_2=i
                    if shift_2 <= 26:
                        print(f'[+]ROT{shift_2} \t:\t'+Rotate.RotateString((shift_2,rotall)))
                    else:
                        print("Invalid shift number.\nPlease specify shift inbetween 0 - 26.")
            else:
                print('\nAll RoT cipher(only alphabets) from 0-25\nIn below output, ROT0 is what you given as input!!')
                for i in range(0,n):
                    shift_2=i
                    print(f'|-> ROT{shift_2}:\t'+Rotate.RotateString((shift_2,rotall)))
                print()
    except:
        pass
 
def write_output():
    try:
        global output, temp
        output = args.output
        print(f'Results get stored in "{output}" file.\n')
        temp = sys.stdout
        sys.stdout=open(output,'w')
    except:
        pass

def read_output():
    with open(output,'r') as file:
        print(file.read())

def show():
    print('Characters Used:\n')
    print('  ROT5  : 0123456789')
    print('  ROT13 : ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    print('  ROT18 : 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    print('  ROT47 : !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ')
    print('\nWhile encountering symbols like `,!,\', \", ;, which may be defined to process system commands to overcome the issue use backslash(\"\\\") to return the appropriate output instead of getting an error.\n')

def help_ex():
    print('Samples: \n\trot -r5 012345')
    print('\trot -r18 abcdABCD12345') 
    print('\trot -r47 "abCD!@#12<=+" -r5 "1234567" -r13 "abcdABCD" ')
    print('\trot -a "hello WORLD"')
    print('\trot -a "hello world" -r 11 -r=22 -r47 "@#$ABxy93" \n')


if __name__ == "__main__":
    if args.show:
        show()
    elif args.sample:
        help_ex()
    elif len(sys.argv) > 1:
        try:
            if args.output:
                write_output()
            rot5()
        except KeyboardInterrupt:
            print('Quitting....')
        finally:
            if args.output:
                sys.stdout.close()
                sys.stdout = temp
                read_output()
            exit()
    else:
        parser.print_help()
        print()
        help_ex()


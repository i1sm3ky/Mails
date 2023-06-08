import random

def Encrypt(Input):
    ValidCharSet = 'ab1cdefgh2ijklmn4opqr3)stuvwx6yz(5ABC*DEF!G7H0IJKL?8MNOPQ.R9ST UV,WXYZ'
    CompleteCharSet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@$%^&*()_-=+\|/?.>,[]{} '
    TempCharSet = CompleteCharSet
    Key = ''
    EncryptedOutput = ''
    for Element in ValidCharSet:
        Element = random.choice(TempCharSet)
        Key += Element
        TempCharSet = TempCharSet.replace(Element, "")
    for _ in Input:
        EncryptedOutput += Key[ValidCharSet.index(_)]
    return (EncryptedOutput, Key)

def Encryption(Input):
    ValidCharSet = 'ab1cdefgh2ijklmn4opqr3)stuvwx6yz(5ABC*DEF!G7H0IJKL?8MNOPQ.R9ST UV,WXYZ'
    Key = '6WI4!5D|}S=z/iT\\*?-8ovhLd$r{k.1,t+7uBnNya03][ecZ%V&gMqF>xKJfEmH )RUC9j'
    EncryptedOutput = ''
    for _ in Input:
        EncryptedOutput += Key[ValidCharSet.index(_)]
    return EncryptedOutput


def GeneratePassword():
    ValidCharSet = 'ab1cdefgh2ijklmn4opqr3)stuvwx6yz(5ABC*DEF!G7H0IJKL?8MNOPQ.R9ST UV,WXYZ'
    Password = ''
    for _ in range(16):
        Password += random.choice(ValidCharSet)
    return Password

def Decrypt(Input):
    CharSet = 'ab1cdefgh2ijklmn4opqr3)stuvwx6yz(5ABC*DEF!G7H0IJKL?8MNOPQ.R9ST UV,WXYZ'
    DecryptedOutput = ''
    for _ in Input[0]:
        DecryptedOutput += CharSet[Input[1].index(_)]
    return DecryptedOutput

def ChangeToAlpha(Number):
    Num = "0123456789"
    Char = "abcdefghi"
    AlphaName = ""
    for Digit in Number:
        AlphaName += Char[Num.index(Digit)]
    return AlphaName
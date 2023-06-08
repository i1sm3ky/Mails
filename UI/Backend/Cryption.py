def Encrypt(Input):
    ValidCharSet = 'ab1cdefgh2ijklmn4opqr3)stuvwx6yz(5ABC*DEF!G7H0IJKL?8MNOPQ.R9ST UV,WXYZ'
    Key = '6WI4!5D|}S=z/iT\\*?-8ovhLd$r{k.1,t+7uBnNya03][ecZ%V&gMqF>xKJfEmH )RUC9j'
    EncryptedOutput = ''
    for _ in Input:
        EncryptedOutput += Key[ValidCharSet.index(_)]
    return EncryptedOutput

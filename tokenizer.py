#import codecs
def tokenize( inpstring, categories ):
    string = inpstring.replace('\r\n', '').replace('\n', ' ')
    token = ''
    tokens = []
    category = None
    for char in string:
        if token:
            if category and char in category:
                token += char
            else:
                if token != ' ':
                    tokens.append( token )
                token = char
                category = None
                for cat in categories:
                    if char in cat:
                        category = cat
                        break
        else:
            category = None
            if not category:
                for cat in categories:
                    if char in cat:
                        category = cat
                        break
            token += char
    if token:
        tokens.append( token )
    return tokens
# f = codecs.open("D:\\Hira\\Hira-OLD\\Learning\\Courses\\NLP\\python code\\test_bn.txt","r", "utf-8")
# string = f.read().replace('\r\n', '').replace('\n', '')

# tokens = tokenize( string, [ '০১২৩৪৫৬৭৮৯', ',.;:!?-', 'অআইঈউঊএঐওঔকখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমযরলশষসহড়ঢ়য়ৎ‌়◌াি◌ী◌ু◌ূ◌ৃেৈোৌ◌্' ] )

# tokens

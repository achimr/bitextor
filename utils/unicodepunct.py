import unicodedata
import string


# Function that returns all the punctuation signs in unicode and ascii
def get_unicode_punct():
    unicodepunct = []
    unicodepunct.append(unicodedata.lookup("EN QUAD"))
    unicodepunct.append(unicodedata.lookup("EN QUAD"))
    unicodepunct.append(unicodedata.lookup("EN QUAD"))
    unicodepunct.append(unicodedata.lookup("EM QUAD"))
    unicodepunct.append(unicodedata.lookup("EN SPACE"))
    unicodepunct.append(unicodedata.lookup("EM SPACE"))
    unicodepunct.append(unicodedata.lookup("THREE-PER-EM SPACE"))
    unicodepunct.append(unicodedata.lookup("FOUR-PER-EM SPACE"))
    unicodepunct.append(unicodedata.lookup("SIX-PER-EM SPACE"))
    unicodepunct.append(unicodedata.lookup("FIGURE SPACE"))
    unicodepunct.append(unicodedata.lookup("PUNCTUATION SPACE"))
    unicodepunct.append(unicodedata.lookup("THIN SPACE"))
    unicodepunct.append(unicodedata.lookup("HAIR SPACE"))
    unicodepunct.append(unicodedata.lookup("ZERO WIDTH SPACE"))
    unicodepunct.append(unicodedata.lookup("ZERO WIDTH NON-JOINER"))
    unicodepunct.append(unicodedata.lookup("ZERO WIDTH JOINER"))
    unicodepunct.append(unicodedata.lookup("LEFT-TO-RIGHT MARK"))
    unicodepunct.append(unicodedata.lookup("RIGHT-TO-LEFT MARK"))
    unicodepunct.append(unicodedata.lookup("HYPHEN"))
    unicodepunct.append(unicodedata.lookup("NON-BREAKING HYPHEN"))
    unicodepunct.append(unicodedata.lookup("FIGURE DASH"))
    unicodepunct.append(unicodedata.lookup("EN DASH"))
    unicodepunct.append(unicodedata.lookup("EM DASH"))
    unicodepunct.append(unicodedata.lookup("HORIZONTAL BAR"))
    unicodepunct.append(unicodedata.lookup("DOUBLE VERTICAL LINE"))
    unicodepunct.append(unicodedata.lookup("DOUBLE LOW LINE"))
    unicodepunct.append(unicodedata.lookup("LEFT SINGLE QUOTATION MARK"))
    unicodepunct.append(unicodedata.lookup("RIGHT SINGLE QUOTATION MARK"))
    unicodepunct.append(unicodedata.lookup("SINGLE LOW-9 QUOTATION MARK"))
    unicodepunct.append(unicodedata.lookup("SINGLE HIGH-REVERSED-9 QUOTATION MARK"))
    unicodepunct.append(unicodedata.lookup("LEFT DOUBLE QUOTATION MARK"))
    unicodepunct.append(unicodedata.lookup("RIGHT DOUBLE QUOTATION MARK"))
    unicodepunct.append(unicodedata.lookup("DOUBLE LOW-9 QUOTATION MARK"))
    unicodepunct.append(unicodedata.lookup("DOUBLE HIGH-REVERSED-9 QUOTATION MARK"))
    unicodepunct.append(unicodedata.lookup("DAGGER"))
    unicodepunct.append(unicodedata.lookup("DOUBLE DAGGER"))
    unicodepunct.append(unicodedata.lookup("BULLET"))
    unicodepunct.append(unicodedata.lookup("TRIANGULAR BULLET"))
    unicodepunct.append(unicodedata.lookup("ONE DOT LEADER"))
    unicodepunct.append(unicodedata.lookup("TWO DOT LEADER"))
    unicodepunct.append(unicodedata.lookup("HORIZONTAL ELLIPSIS"))
    unicodepunct.append(unicodedata.lookup("HYPHENATION POINT"))
    unicodepunct.append(unicodedata.lookup("LINE SEPARATOR"))
    unicodepunct.append(unicodedata.lookup("PARAGRAPH SEPARATOR"))
    unicodepunct.append(unicodedata.lookup("LEFT-TO-RIGHT EMBEDDING"))
    unicodepunct.append(unicodedata.lookup("RIGHT-TO-LEFT EMBEDDING"))
    unicodepunct.append(unicodedata.lookup("POP DIRECTIONAL FORMATTING"))
    unicodepunct.append(unicodedata.lookup("LEFT-TO-RIGHT OVERRIDE"))
    unicodepunct.append(unicodedata.lookup("RIGHT-TO-LEFT OVERRIDE"))
    unicodepunct.append(unicodedata.lookup("NARROW NO-BREAK SPACE"))
    unicodepunct.append(unicodedata.lookup("PER MILLE SIGN"))
    unicodepunct.append(unicodedata.lookup("PER TEN THOUSAND SIGN"))
    unicodepunct.append(unicodedata.lookup("PRIME"))
    unicodepunct.append(unicodedata.lookup("DOUBLE PRIME"))
    unicodepunct.append(unicodedata.lookup("TRIPLE PRIME"))
    unicodepunct.append(unicodedata.lookup("REVERSED PRIME"))
    unicodepunct.append(unicodedata.lookup("REVERSED DOUBLE PRIME"))
    unicodepunct.append(unicodedata.lookup("REVERSED TRIPLE PRIME"))
    unicodepunct.append(unicodedata.lookup("CARET"))
    unicodepunct.append(unicodedata.lookup("SINGLE LEFT-POINTING ANGLE QUOTATION MARK"))
    unicodepunct.append(unicodedata.lookup("SINGLE RIGHT-POINTING ANGLE QUOTATION MARK"))
    unicodepunct.append(unicodedata.lookup("REFERENCE MARK"))
    unicodepunct.append(unicodedata.lookup("DOUBLE EXCLAMATION MARK"))
    unicodepunct.append(unicodedata.lookup("INTERROBANG"))
    unicodepunct.append(unicodedata.lookup("OVERLINE"))
    unicodepunct.append(unicodedata.lookup("UNDERTIE"))
    unicodepunct.append(unicodedata.lookup("CHARACTER TIE"))
    unicodepunct.append(unicodedata.lookup("CARET INSERTION POINT"))
    unicodepunct.append(unicodedata.lookup("ASTERISM"))
    unicodepunct.append(unicodedata.lookup("HYPHEN BULLET"))
    unicodepunct.append(unicodedata.lookup("FRACTION SLASH"))
    unicodepunct.append(unicodedata.lookup("LEFT SQUARE BRACKET WITH QUILL"))
    unicodepunct.append(unicodedata.lookup("RIGHT SQUARE BRACKET WITH QUILL"))
    unicodepunct.append(unicodedata.lookup("DOUBLE QUESTION MARK"))
    unicodepunct.append(unicodedata.lookup("QUESTION EXCLAMATION MARK"))
    unicodepunct.append(unicodedata.lookup("EXCLAMATION QUESTION MARK"))
    unicodepunct.append(unicodedata.lookup("TIRONIAN SIGN ET"))
    unicodepunct.append(unicodedata.lookup("REVERSED PILCROW SIGN"))
    unicodepunct.append(unicodedata.lookup("BLACK LEFTWARDS BULLET"))
    unicodepunct.append(unicodedata.lookup("BLACK RIGHTWARDS BULLET"))
    unicodepunct.append(unicodedata.lookup("LOW ASTERISK"))
    unicodepunct.append(unicodedata.lookup("REVERSED SEMICOLON"))
    unicodepunct.append(unicodedata.lookup("CLOSE UP"))
    unicodepunct.append(unicodedata.lookup("TWO ASTERISKS ALIGNED VERTICALLY"))
    unicodepunct.append(unicodedata.lookup("COMMERCIAL MINUS SIGN"))
    unicodepunct.append(unicodedata.lookup("SWUNG DASH"))
    unicodepunct.append(unicodedata.lookup("INVERTED UNDERTIE"))
    unicodepunct.append(unicodedata.lookup("FLOWER PUNCTUATION MARK"))
    unicodepunct.append(unicodedata.lookup("THREE DOT PUNCTUATION"))
    unicodepunct.append(unicodedata.lookup("QUADRUPLE PRIME"))
    unicodepunct.append(unicodedata.lookup("FOUR DOT PUNCTUATION"))
    unicodepunct.append(unicodedata.lookup("FIVE DOT PUNCTUATION"))
    unicodepunct.append(unicodedata.lookup("TWO DOT PUNCTUATION"))
    unicodepunct.append(unicodedata.lookup("FOUR DOT MARK"))
    unicodepunct.append(unicodedata.lookup("DOTTED CROSS"))
    unicodepunct.append(unicodedata.lookup("TRICOLON"))
    unicodepunct.append(unicodedata.lookup("VERTICAL FOUR DOTS"))
    unicodepunct.append(unicodedata.lookup("MEDIUM MATHEMATICAL SPACE"))
    unicodepunct.append(unicodedata.lookup("WORD JOINER"))
    unicodepunct.append(unicodedata.lookup("FUNCTION APPLICATION"))
    unicodepunct.append(unicodedata.lookup("INVISIBLE TIMES"))
    unicodepunct.append(unicodedata.lookup("INVISIBLE SEPARATOR"))
    unicodepunct.append(unicodedata.lookup("INVISIBLE PLUS"))
    unicodepunct.append(unicodedata.lookup("INHIBIT SYMMETRIC SWAPPING"))
    unicodepunct.append(unicodedata.lookup("ACTIVATE SYMMETRIC SWAPPING"))
    unicodepunct.append(unicodedata.lookup("INHIBIT ARABIC FORM SHAPING"))
    unicodepunct.append(unicodedata.lookup("ACTIVATE ARABIC FORM SHAPING"))
    unicodepunct.append(unicodedata.lookup("NATIONAL DIGIT SHAPES"))
    unicodepunct.append(unicodedata.lookup("NOMINAL DIGIT SHAPES"))

    # Returning the standard punctuation + the list of unicode punctuation characters
    return string.punctuation + ''.join(unicodepunct)

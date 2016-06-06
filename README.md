# PyFmter

This package contains different functions for beautifying Python string formatting.

NOTE: All the functions suit for both Python 2.x and 3.x.

## Function List

1. **align(text, space, alignment)**
Align texts contain Chinese or English characters  `left`, `right` or `center`.

## Example

1. align(text, space, alignment)
```
from PyFmter import align
text = '你好！我叫Seahon.'
print('1234567890' * 6)
print(align(text, 30, 'center'))
```
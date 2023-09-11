# Given string containing International Phonetic Alphabet characters, print rough pronunciation respelling
# Only works for English IPA
# "Dumb" - no syllable separation or stressors, output string slightly idiosyncratic

import sys

# vowels = {'æ': 'a', 'ɑː': 'ah', 'ɛər': 'air', 'ɑr': 'ar', \
#         'ær': 'arr', 'ɔː': 'aw', 'eɪ': 'ay', 'ə': 'uh', 'ɨ': 'uh', \
#         'ər': 'er', 'ɚ': 'er', 'ɛ': 'e', 'iː': 'ee', 'i': 'ee', \
#         'ɪər': 'eer', 'ɛr': 'err', 'juː': 'ew', 'jʊər': 'ewr', \
#         'aɪ': 'y', 'ɪ': 'i', 'ɪr': 'irr', 'ɒ': 'o', 'oʊ': 'oh', \
#         'uː': 'oo', 'ʊər': 'oor', 'ɔər': 'or', 'ɔr': 'or', 'ɒr': 'orr', \
#         'aʊ': 'ow', 'aʊər': 'owr', 'ɔɪ': 'oy', 'ʌ': 'u', 'ɜr': 'ur', \
#         'ɝː': 'ur', 'ʌr': 'urr', 'ʊ': 'uu', 'aɪər': 'yr'}
# consonants = {'b': 'b', 'tʃ': 'ch', 'd': 'd', 'ð': 'th', 'f': 'f', \
#             'ɡ': 'g', 'h': 'h', 'dʒ': 'j', 'k': 'k', 'x': 'kh', 'l': 'l', \
#             'm': 'm', 'n': 'n', 'ŋ': 'ng', 'p': 'p', 'r': 'r', 's': 'ss', \
#             'ʃ': 'sh', 't': 't', 'θ': 'th', 'v': 'v', 'w': 'w', 'hw': 'wh', \
#             'j': 'y', 'z': 'z', 'ʒ': 'zh'}

ipa = {'æ': 'a', 'ɑː': 'ah', 'ɛər': 'air', 'ɑr': 'ar', \
        'ær': 'arr', 'ɔː': 'aw', 'eɪ': 'ay', 'ə': 'uh', 'ɨ': 'uh', \
        'ər': 'er', 'ɚ': 'er', 'ɛ': 'e', 'iː': 'ee', 'i': 'ee', \
        'ɪər': 'eer', 'ɛr': 'err', 'juː': 'ew', 'jʊər': 'ewr', \
        'aɪ': 'y', 'ɪ': 'i', 'ɪr': 'irr', 'ɒ': 'o', 'oʊ': 'oh', \
        'uː': 'oo', 'ʊər': 'oor', 'ɔər': 'or', 'ɔr': 'or', 'ɒr': 'orr', \
        'aʊ': 'ow', 'aʊər': 'owr', 'ɔɪ': 'oy', 'ʌ': 'u', 'ɜr': 'ur', \
        'ɝː': 'ur', 'ʌr': 'urr', 'ʊ': 'uu', 'aɪər': 'yr', 'b': 'b', \
        'tʃ': 'ch', 'd': 'd', 'ð': 'th', 'f': 'f', 'ɡ': 'g', 'h': 'h', \
        'dʒ': 'j', 'k': 'k', 'x': 'kh', 'l': 'l', 'm': 'm', 'n': 'n', \
        'ŋ': 'ng', 'p': 'p', 'r': 'r', 's': 'ss', 'ʃ': 'sh', 't': 't', \
        'θ': 'th', 'v': 'v', 'w': 'w', 'hw': 'wh', 'j': 'y', 'z': 'z', \
        'ʒ': 'zh', 'ᵻ': 'i'}

in_text = sys.argv[1]

if __name__ == "__main__":
    split_text = in_text.split() # convert to list of words
    out_text = ''

    for word in split_text:
        temp = ''
        for letter in word:
            if (letter in ipa or letter.isalpha()) and letter != 'ˌ' and letter != 'ˈ' and letter != 'ː':
                temp += letter
        word = temp
        while len(word) > 0:
            if word[:4] in ipa:
                out_text += ipa[word[:4]]
                word = word[4:]
            elif word[:3] in ipa:
                out_text += ipa[word[:3]]
                word = word[3:]
            elif word[:2] in ipa:
                out_text += ipa[word[:2]]
                word = word[2:]
            elif word[:1] in ipa:
                out_text += ipa[word[:1]]
                word = word[1:]
            else:
                out_text += word[:1]
                word = word[1:]
        out_text += ' '
    print(out_text.strip())

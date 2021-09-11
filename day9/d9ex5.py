from string import punctuation


def word_in_srt(srt_inp):
    for item in punctuation:
        srt_inp = srt_inp.replace(item, " ", srt_inp.count(item))
    srt_inp = srt_inp.split()
    return len(srt_inp)


srt_input = input('Enter word`s= ')
print(word_in_srt(srt_input))

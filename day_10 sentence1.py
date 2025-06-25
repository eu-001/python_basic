import numpy as np

#처리할 문장들
sentences=[
    "나는 밥을 먹었다",
    "나는 밥을 안 먹었다",
    "나는 학교에 갔다"
]

#단어 사전 만들기(word -> index)
word_to_index={}
index=0

for sentence in sentences:
    words=sentence.split()
    for word in words:
        if word not in word_to_index:
            word_to_index[word]=index
            index+=1

print(f"단어사전: {word_to_index}")            
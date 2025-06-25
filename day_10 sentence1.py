import numpy as np
from numpy.linalg import norm

#처리할 문장들
sentences=[
    "나는 밥을 먹었다",
    "나는 밥을 안 먹었다",
    "나는 학교에 갔다",
    "니 얼굴"
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
#문장을 숫자 벡터로 바꾸기 (문장 -> 점수 리스트)
vectorized_sentences=[]

for sentence in sentences:
    words = sentence.split()
    """
    vector= [
        word_to_index["나는"],
        word_to_index["밥을"],
        word_to_index["먹었다"]
    ]
    == vector = [ 1,2,3]
    """
    vector = [word_to_index[word] for word in words]
    vectorized_sentences.append(vector)

print(f"숫자 벡터화:", vectorized_sentences)

#길이를 맞춰서 numpy 배열로 변환 (padding)
"""
vectorized_sentences = [
    [1, 2, 3],        # 첫 번째 문장 (길이 3)
    [4, 5],           # 두 번째 문장 (길이 2)
    [6, 7, 8, 9]      # 세 번째 문장 (길이 4)
]
한 문장씩 길이 확인하면:
len([1, 2, 3]) → 3  
len([4, 5]) → 2  
len([6, 7, 8, 9]) → 4
"""
max_len= max(len(v) for v in vectorized_sentences)
print(f"max_leng: {max_len}")

"""
sentences 개수만큼 줄(row)을 만들고,
max_len 길이만큼 칸(column)을 만들어서
모두 0으로 채운 2차원 배열을 만드는 코드입니다.

sentences = [
    ["나는", "밥을", "먹었다"],
    ["너는", "잤다"]
]
# 각 문장 → 숫자로 바꾸고 나면:
vectorized_sentences = [
    [1, 2, 3],
    [4, 5]
]
# 가장 긴 문장의 길이
max_len = 3

# 문장 개수
len(sentences) = 2

# 만들고 싶은 배열의 크기 → (2줄, 3칸)
"""
padded_array=np.zeros((len(sentences),max_len),dtype=int)
print(f"padded_array.shape : {padded_array.shape}")

'''
numpy sentence:
[[0 1 2 0]
 [0 1 3 2]
 [0 4 5 0]
 [6 7 0 0]]
''' 
#저게 행렬이랜다
#나는 기존 문장에서 니 얼굴 까지 적어서 터미너 값이 달라질 수도 있음

for i,vector in enumerate(vectorized_sentences):
    padded_array[i, :len(vector)]=vector

print(f"numpy sentence:")
print(padded_array)    

# word_to_index : 단어사전,   sentence: 새로운 문장
def sentence_to_vector(sentence, word_to_index, max_len):
    words = sentence.split()
    vector = [word_to_index.get(word, -1) for word in words]
    #없는 단어는 제거
    vector = [v for v in vector if v != -1]
    padded = np.zeros((max_len,), dtype=int)
    padded[:len(vector)] = vector[:max_len]
    return padded
def cosine_similarity(vec1, vec2):
    if norm(vec1)==0 or norm(vec2) ==0:
        return 0.0
    return np.dot(vec1,vec2)/((norm(vec1)*norm(vec2)))

def find_most_similar(sentence,sentences,padded_array
                      ,word_to_index,max_len):
    new_vec=sentence_to_vector(sentence,word_to_index,max_len)
    best_score=-1
    best_index=-1
    for i, old_vec in enumerate(padded_array):
        score=cosine_similarity(new_vec,old_vec)    
        print(f"-> {sentences[i]} 와 유사도 : {score:.2f}")          
        if score > best_score:
            best_score = score
            best_index = i
    if best_score == 1.0:
        print(" ##완전히 같은 문장이 있습니다")
    else:
        print(f"가장 유사한 문장: {sentences[best_index]}")
        print(f"유사도:{best_score:.2f}")     

new_sentence = "나는 밥을 안먹었다"
find_most_similar(new_sentence, sentences, padded_array
                  , word_to_index, max_len)



   ''' 

    # 아래는 아까 수정한 부분들을 # 주석으로 짚어가며 다시 정리한 코드입니다.

    # 1. 단어 사전 만들기
    # 각 문장을 띄어쓰기로 분리해서, 새로운 단어가 나오면 인덱스를 부여합니다.
    word_to_index = {}
    index = 0
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            if word not in word_to_index:
                word_to_index[word] = index
                index += 1
    print(f"단어사전: {word_to_index}")

    # 2. 문장을 숫자 벡터로 변환
    # 각 문장을 단어 인덱스의 리스트로 변환합니다.
    vectorized_sentences = []
    for sentence in sentences:
        words = sentence.split()
        vector = [word_to_index[word] for word in words]
        vectorized_sentences.append(vector)
    print(f"숫자 벡터화:", vectorized_sentences)

    # 3. 패딩(padding) 처리
    # 가장 긴 문장 길이에 맞춰 0으로 채운 2차원 배열을 만듭니다.
    max_len = max(len(v) for v in vectorized_sentences)
    padded_array = np.zeros((len(sentences), max_len), dtype=int)
    for i, vector in enumerate(vectorized_sentences):
        padded_array[i, :len(vector)] = vector
    print(f"padded_array.shape : {padded_array.shape}")
    print(f"numpy sentence:")
    print(padded_array)

    # 4. 새로운 문장을 벡터로 변환하는 함수
    def sentence_to_vector(sentence, word_to_index, max_len):
        words = sentence.split()
        vector = [word_to_index.get(word, -1) for word in words]
        vector = [v for v in vector if v != -1]  # 없는 단어는 제거
        padded = np.zeros((max_len,), dtype=int)
        padded[:len(vector)] = vector[:max_len]
        return padded

    # 5. 코사인 유사도 함수
    def cosine_similarity(vec1, vec2):
        if norm(vec1) == 0 or norm(vec2) == 0:
            return 0.0
        return np.dot(vec1, vec2) / (norm(vec1) * norm(vec2))

    # 6. 가장 유사한 문장 찾기
    def find_most_similar(sentence, sentences, padded_array, word_to_index, max_len):
        new_vec = sentence_to_vector(sentence, word_to_index, max_len)
        best_score = -1
        best_index = -1
        for i, old_vec in enumerate(padded_array):
            score = cosine_similarity(new_vec, old_vec)
            print(f"-> {sentences[i]} 와 유사도 : {score:.2f}")
            if score > best_score:
                best_score = score
                best_index = i
        if best_score == 1.0:
            print(" ##완전히 같은 문장이 있습니다")
        else:
            print(f"가장 유사한 문장: {sentences[best_index]}")
            print(f"유사도:{best_score:.2f}")

    # 7. 테스트: 새로운 문장과 기존 문장들 비교
    new_sentence = "나는 밥을 안먹었다"
    find_most_similar(new_sentence, sentences, padded_array, word_to_index, max_len)

    '''
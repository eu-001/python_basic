from sentence_transformers import SentenceTransformer,util

model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')

sentence1="고양이가 이상해요"
sentence2="고양이가 요상해요"

embedding1=model.encode(sentence1,convert_to_tensor=True)
embedding2=model.encode(sentence2,convert_to_tensor=True)

similarity=util.pytorch_cos_sim(embedding1,embedding2)
print(f"유사도: {similarity.item()}")



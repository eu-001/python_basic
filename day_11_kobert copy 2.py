from sentence_transformers import SentenceTransformer,util
import torch

model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')

user_input="배송은 얼마나 걸리나요?"
user_embedding=model.encode(user_input, convert_to_tensor=True)

data = torch.load("questions_embeddings.pt")
saved_embeddings = data["embeddings"]
saved_ids = data["ids"]
saved_questions = data["questions"]

cos_sim= util.pytorch_cos_sim(user_embedding, saved_embeddings)[0]
top_k=torch.topk(cos_sim, k=1)
top_idx=top_k.indices[0].item()
print(f"가장 유사한 질문:{saved_questions[top_idx]}")
print(f"DB ID:{saved_ids[top_idx]}")
print(f"유사도 점수:{top_k.values[0].item()}")

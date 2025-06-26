from sentence_transformers import SentenceTransformer,util

model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')

questions=[]
ids=[]

with open("questions.txt","r",encoding="utf-8") as f:
    for line in f:
        line=line.strip()
        print(f"line:{line}")
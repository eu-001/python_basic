from sentence_transformers import SentenceTransformer,util

model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')

questions=[]
ids=[]

with open("questions.txt","r",encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        print(f"line:{line}")
        if "__DB__id=" in line:
            question_part, id_part = line.split("__DB__id=")
            question = question_part.strip()
            db_id = int(id_part.strip())
            questions.append(question)
            ids.append(db_id)
print(questions)
print(ids)

embeddings = model.encode(questions, convert_to_tensor=True)

torch.save({
    "embeddings": embeddings,
    "ids": ids,
    "questions": questions
}, "questions_embeddings.pt")
print(f"임베딩 저장 완료! 총 {len(questions)}개의 질문이 저장되었습니다.")


def build_context(df, n=5):
    return df.head(n).to_string()

def rag_query(df, question, llm):
    context = build_context(df)

    prompt = f"""
You are a data analyst AI.

Context:
{context}

Question:
{question}

Give a clear answer with reasoning.
"""

    return llm(prompt)
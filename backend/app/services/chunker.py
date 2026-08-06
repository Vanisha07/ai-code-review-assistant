from langchain_text_splitters import RecursiveCharacterTextSplitter


splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100,
)


def split_documents(files):

    documents = []

    for file in files:

        chunks = splitter.split_text(file["content"])

        for i, chunk in enumerate(chunks):

            documents.append(
                {
                    "path": file["path"],
                    "chunk_id": i,
                    "content": chunk,
                }
            )

    return documents
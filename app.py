from model import vector_index
import gradio as gr 
import os
from timeit import default_timer as timer
import pickle
from llama_index.core import TreeIndex, VectorStoreIndex
from llama_index.llms.groq import Groq
from llama_index.core import get_response_synthesizer

with open("tree_index_list.pkl","rb") as f:
    tree_index_list=pickle.load(f)

with open("chapter_index.pkl","rb") as f:
    chapter_index=pickle.load(f)

groq_api_key = os.getenv('GROQ_API_KEY')

groq_llm = Groq(api_key=groq_api_key, model="gemma2-9b-it")

response_synthesizer = get_response_synthesizer(response_mode="compact", llm=groq_llm)

def response(user_query, vector_index=vector_index, tree_index_list=tree_index_list, chapter_index=chapter_index, response_synthesizer=response_synthesizer):
    
    start_time=timer()
    
    retriever1=vector_index.as_retriever(similarity_top_k=3)
    retrieved_nodes1=retriever1.retrieve(user_query)
    
    tree_index=tree_index_list[chapter_index[retrieved_nodes1[0].metadata["chapter"]]]
    
    if retrieved_nodes1[0].metadata["section"]=="poem":
        retriever = tree_index.as_retriever(similarity_top_k=5, retriever_mode="all_leaf")
        retrieved_nodes3=retriever.retrieve("summarize this chapter")
        answer = response_synthesizer.synthesize(query=user_query, nodes=retrieved_nodes3)
        return answer.response.strip(), round(timer()-start_time,4)
        
    retriever = tree_index.as_retriever(similarity_top_k=1,retriever_mode="root", 
                                        search_kwargs={"num_children":4})

    retrieved_nodes2=retriever.retrieve("summarize this chapter")
    
    combined_nodes=retrieved_nodes1+retrieved_nodes2
    
    answer = response_synthesizer.synthesize(query=user_query, nodes=combined_nodes)
    pred_time=round(timer()-start_time,3)
    
    return answer.response.strip(), pred_time

title=""" 
📚 Ask ZERO, Learn Like a Legend!
"For every question in Kaleidoscope, ZERO delivers a knockout answer." 🥊💡🔥
"""

description=""" 
🥊Answer Like Zero!🧠⚡
This model’s name is ZERO — and it ain’t got nothin’ to prove!
📘 Ask any question from Kaleidoscope – 12th NCERT and watch ZERO hit back with lightning-fast answers!
🎯 Study smarter, learn sharper, and knock confusion out cold — with ZERO in your corner! 💥📚💡
"""

article=""" 
How It Works:
Vector Indexing: Retrieves the most relevant text with semantic search. 🎯
Tree Indexing: Summarizes and organizes content with a hierarchical structure. 📚
LLM: Delivers context-rich responses with intelligence and power of gemma2-9b-it state-of-the-art open source model! 🏆
"""

examples_list=["Who is Joseph Conrad?", "Summarize the story Tomorrow", "Who is author of the poem Blood?"]

interface = gr.Interface(fn=response, inputs=gr.Textbox(lines=2, placeholder="Enter your query here...", label="User Query"), 
                         outputs=[ gr.Textbox(label="Answer"), gr.Textbox(label="Response Time")], 
                         title=title, description=description, 
                         article=article, examples=examples_list )

interface.launch()

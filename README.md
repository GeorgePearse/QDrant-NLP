# QDrant-NLP
Keeping the Human in the LOOP. I am not a developer at QDrant, nor directly associated with them, but I think they've built something excellent, and thus far under-appreciated. This repo is here to act as a demo more than anything else.

https://github.com/qdrant/qdrant

I'll call it done once it's tidy and available on DockerHub. Just enough that you could maybe use it to run your own POC without any additional code. 

You can achieve almost half of this tool just via their swagger UI, but obviously, that's designed for hitting simple APIs, not data-centric AI workflows, so it's missing a few useful components. This work is written up in more depth here https://medium.com/@george.pearse.
 
<img width="202" alt="image" src="https://user-images.githubusercontent.com/47161914/186397107-5706db97-6404-40fd-8ce1-b42bb83249c2.png">

The toy logo is somewhere between a magnifying glass for how the tooling enables you to really focus in on a specific data subset, and a classic bayesian graph for if I get carried away enough to try to add active learning in. 

Finding the documentation for hugging-face sentence-transformers via Google Search drove me mad, it lives here https://www.sbert.net/docs/hugging_face.html

Quick labelling with hugging-face, streamlit and QDrant. First I'll support NLP, then I'll think about adding image support (which is where this idea came from).

- [X] Supports interactively creating and storing queries for the QDrant Vector Database for an NLP dataset.
- [X] For each query, show the positives, show the negatives, then display the results.
- [ ] Maybe support Active Learning (eventually). Can have a two part system, one part using Active Learning to optimise the similarity search, the other to optimize downstream finetuning. Or one to update which datapoint a nearest neighbour approach is least certain about (because this can be almost instantly updated) and another to correct the model which generates the embeddings.

<img width="1331" alt="image" src="https://user-images.githubusercontent.com/47161914/186453861-e4c2b2e6-6a1d-4039-b044-8029d97dfdb5.png">


See Kern.AI for a full blown solution which uses QDrant behind the scenes. This tool is meant to be simple enough to act as an intro to vector databases. You can write and see the requests, just as you would via the python API. 

Similarly, koaning/bulk is excellent, but what if UMAP (insert alternative dimensionality reduction technique here) loses all of the nuance, and high-level visualizations fail to provide value for your dataset? 

I also wanted to give FastAPI a tiny test run, so for each query (post request) you save, you can receive its results by hitting the FastAPI endpoint with the name of the query.

To apply these tools to a multi-modal dataset you would only need to concatenate the embeddings for each component and away you go with all the same technqiues. 

NB: Consider calling this thing grouper if you take it more seriously and upgrade the components

Might make sense to apply a similarity cut off instead of the nearest K. 

# To Run:

Currently clone the repo and then run. From 1 terminal:
```
docker-compose up
```
To start the QDrant vector database. 
From another, run:
```
streamlit run intro.py
```
For the streamlit UI.
If you want the FastAPI endpoints which just provide a way to access the results of your queries by name it's
```
uvicorn api:app --reload
```
(think --reload is for dev only)

But I'll be making this available on DockerHub soon to simplify all of that. It'll also be available via Streamlit cloud and hopefully make it into the Streamlit Gallery.

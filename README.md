# QDrant-NLP
Keeping the Human in the LOOP. I am not a developer at QDrant, nor directly associated with them, but I think they've built something excellent, and thus far under-appreciated. This repo is here to act as a demo more than anything else.

<img width="202" alt="image" src="https://user-images.githubusercontent.com/47161914/186397107-5706db97-6404-40fd-8ce1-b42bb83249c2.png">

The toy logo is somewhere between a magnifying class for how the tooling enables you to really focus in on a specific data subset, and a classic bayesian graph for if I get carried away enough to try to add active learning in. 

Finding the documentation for sentence-transformers via Google Search drove me mad, it lives here https://www.sbert.net/docs/hugging_face.html

Quick labelling with hugging-face, streamlit and QDrant. First I'll support NLP, then I'll think about adding image support (which is where this idea came from).

- [ ] Supports interactively creating and storing queries for the QDrant Vector Database for an NLP dataset.
- [ ] For each query, show the positives, show the negatives, then display the results.
- [ ] Maybe support Active Learning (eventually) 

See Kern.AI for a full blown solution using very similar technology behind the scenes. This tool is meant to be simple enough to act as an intro to vector databases. You can write and see the requests, just as you would via the python API. 

Similarly, koaning/bulk is excellent, but what if UMAP (insert alternative dimensionality reduction technique here) loses all of the nuance, and high-level visualizations fail to provide value for your dataset? 

I also wanted to give FastAPI a tiny test run, so for each query (post request) you save, you can receive its results by hitting the FastAPI endpoint with the name of the query.

To apply these tools to a multi-modal dataset you would only need to concatenate the embeddings for each component and away you go with all the same technqiues. 

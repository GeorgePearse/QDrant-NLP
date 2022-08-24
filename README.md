# QDrant-NLP
Keeping the Human in the LOOP. I am not a developer at QDrant, nor directly associated with them, but I think they've built something excellent, and thus far under-appreciated. This repo is here to act as a demo more than anything else.

Quick labelling with hugging-face, streamlit and QDrant. First I'll support NLP, then I'll think about adding image support (which is where this idea came from).

- [ ] Supports interactively creating and storing queries for the QDrant Vector Database for an NLP dataset.
- [ ] For each query, show the positives, show the negatives, then display the results.
- [ ] Maybe support Active Learning (eventually) 

See Kern.AI for a full blown solution using very similar technology behind the scenes. This tool is meant to be simple enough to act as an intro to vector databases. You can write and see the requests, just as you would via the python API. 

Similarly, koaning/bulk is excellent, but what if UMAP (insert alternative dimensionality reduction technique here) loses all of the nuance, and high-level visualizations fail to provide value for your dataset? 


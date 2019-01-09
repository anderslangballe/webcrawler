# webcrawler
Multi-threaded webcrawler made as a part of the Web Intelligence course at AAU. Follows (somewhat) the Mercator crawler design.

Group participants:
* Anders Langballe Jakobsen

## Postings list data structure
- Postings lists are stored as Python dictionaries
  - Allows us to store the frequency of the term for each document the term appears in
- Time complexity of intersection and union is `O(n+m)` in the average case

## Boolean query processing
- In order to optimise boolean queries, we can sequentially process ANDs in order of increasing document frequency for each term
- I have cut a corner here by not processing the terms in that sequence
 
## Individual document indexing
- Whenever I perform an index, I only index one document at once
- This means I don't do the core step of sorting (Term, Document ID) pairs
# Totlahtol, an app for learning languages
## Enhanced with Machine Learning Features

### FELI GENTLE, [Machine Learning Engineer](https://github.com/oro13)

In collaboration with

### ARMAND VILLAVERDE, [Data Engineer, Full Stack Dev](https://github.com/xochozomatli)

(This repository contains research and development for ML and data pipeline. The code base is hosted [here](https://github.com/xochozomatli/totlahtol))

---

Our app, Totlahtol, is named for the word ‘Languages,’ in Nahuatl: the Aztec language once widely spoken on this continent and in Central America.

My friend in El Paso began working on this application over a year ago. Now I’m helping him enhance the prototype with advanced Machine Learning components. Including, natural language processing of user generated content and a recommender of lessons based on user interests.

Tech Stack Tools:

Front End 
• [React JS](https://github.com/facebook/react)
• [Flask](https://github.com/pallets/flask)

Back End 
• [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy)
• [Keras/Tensorflow](https://github.com/keras-team/keras)
• [Python](https://github.com/python/)
• [Numpy](https://github.com/numpy/numpy)
• [Pandas](https://github.com/pandas-dev/pandas)

The app (prototype) in action:

<p align="center">
  <img src=/media/app_prototype.gif width='90%' height='auto'>
  <br><i>A user logins in, adds a lesson, and gets lessons specifically curated to their interests</i>
</p>



### Why NLP? Why Recommenders?

While there are many Language Apps available, 
Totlahtol stands out by offering:

- User Generated Lessons, 
- Recommendation of Content specific to User interests and activity, 
- A seamless, interactive user interface to immerse users in the target language. 


Whether you’re the type of polyglot who speaks Spanish and French or the kind who speaks Python and Javascript, feel free to reach out to learn more.

---

## The Data Pipeline

My Research has centered on the most important app use case of uplading a lesson and recommending it to users if their activity implies it'd be relevent to them.

In general, a Recommender Needs these Three Steps:

1. item candidate generation
2. user specific scoring of items
3. reranking, or sorting the items based on relevance to the user

Our Model has the additional step of processing lessons for its latent topics, to give more signal for the 
Here’s How:

<p align="center">
  <img src=/media/uml-basic.png width='90%' height='50%'>
</p>

1. A user uploads a lesson

<p align="center">
  <img src=/media/add_lesson.gif width='90%' height='50%'>
</p>

2. NLP for processing the text and discerning the lesson topics

3. The lesson specific word and topic embeddings are available for the recommender model
<p align="center">
  <img src=/media/tf_embedding_board.png width='80%' height='auto'>
  <br><i>TensorBoard diagram of Word2Vec Embedding Process.</i>
</p>

4. Common lessons are grouped together by topic

<p align="center">
  <img src=/media/pylda_vis.gif width='90%' height='50%'>
</p>

5. User ratings and lesson activity are made available for the recommender model

<p align="center">
  <img src=/media/user_activity.png width='25%' height='20%'>
  <br><i>Users give thumbs up (1) or thumbs down ratings (-1), for explicit feedback for the recommender.</i>
</p>

6. The recommender gets an input of these and other features about the users and lessons

7. The recommender, a combination of deep neural network and matrix factorization, returns the probable ratings for lessons each user has not seen yet

8. These predicted ratings are sorted to find the highest ratings

9. When a user opens their feed, these lessons are suggested to them first

## ML components

### User Generated Lessons and NLP Topic Modeling

When a user uploads a lesson:
Model and Embed Word Tokens and Latent Topics of Lessons, to Understand the Content
(through NLP, LDA, word embeddings, and a Neural Network)

Doing so allows the app to group similar lessons together, on the fly, enabling:
User Specific Recommendations based on Activity and Lesson Preferences 
(through Matrix Factorization and Deep Neural Network)


---
### Why NLP?

topic modeling
checking for duplicate lesson (hashing tokens)

Prototype: LDA

Production: lda2Vec, word2vec, multilingual embeddings, Deep Neural Network, consider Rust HuggingFace tokenizers for speed

<p align="center">
  <img src=/media/overview-1-shorten2.gif></img>
  <br><i>Embedding Space using TensorBoard Project</i>
</p>

<p align="center">
  <img src=/media/topics-1-shorten2.gif></img>
  <br><i>Topic Modeling with Embedding, to show how similar lessons can be grouped for specific user interests. </i>
</p>

Tag the Lessons with specific topics, to generate more signal for the recommender.

### Why Recommenders?

Prototype: Sparse Matrix Factorization

Pros: quick, reliable when signal is reliable (enough user activity)

Cons: bad with limited data on new users (cold start), inputs restricted to User and Items matrix

Production: Deep Neural Network

---

Takeaways:

Learned a number of libraries, such as Keras/Tensorflow, and worked with more familiar with creating custom functions in Pandas and Numpy, and text processing and NLP in GenSim and NLTK

Faced the Challenge of working remotely with the software engineer, my friend, in a different time zone, and had to iteratively adjust the app to implement changes.

Got experience working with machine learning in a production web development environment; being the domain expert to recommend best practice for performance and scalability; had to weigh trade offs of having a fast working prototype and implementing the best available solutions for a given task, faced this at nearly every step; sometimes making prototype is the clear priority, but some best practices shouldn’t be compromised, and found that out the hard way when late in the project decided to reimplement many features using Keras/Tensorflow to achieve state of the art recommendation, like those seen on Youtube, and FaceBook.

If interested in knowing more about the application, whether you’re the type of polyglot who speaks Spanish and French or the kind who speaks Python and Javascript, feel free to reach out! We intend to keep working on the app until we have a deliverable prototype.


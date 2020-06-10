# Machine Learning Enhanced 
# Language Learning App

Totlahtol Language App

FELI GENTLE

<p align="center">
  <img src=/media/login.gif width='90%' height='50%'>
</p>

FELI GENTLE

Machine Learning Enhanced Language Learning App 

Our app, Totlahtol, is named for the word ‘Languages,’ in Nahuatl: the Aztec language once widely spoken on this continent. 
My friend in El Paso began working on this application over a year ago. Now I’m helping him enhance the prototype with advanced Machine Learning components.

Tech used:

Front End 
• React JS
• Flask

Back End 
• SQLAlchemy
• Keras/Tensorflow
• Python/Numpy/Pandas


While there are many Language Apps available, 
Totlahtol stands out by offering:
User Generated Lessons, 
Recommendation of Content specific to User interests and activity, 
A seamless, interactive user interface to immerse users in the target language. 


Whether you’re the type of polyglot who speaks Spanish and French or the kind who speaks Python and Javascript, feel free to reach out to learn more.

---

## The Data Pipeline

My Research has centered on the most important app use case of uplading a lesson and recommending it to users if their activity implies it'd be relevent to them.


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
4. User ratings and lesson activity are made available for the recommender model
5. The recommender gets an input of these and other features about the users and lessons
6. The recommender, a combination of deep neural network and matrix factorization, returns the probable ratings for lessons each user has not seen yet
7. These predicted ratings are sorted to find the highest ratings
8. When a user opens their feed, these lessons are suggested to them first

## ML components

### User Generated Lessons and NLP Topic Modeling

When a user uploads a lesson:
Model and Embed Word Tokens and Latent Topics of Lessons, to Understand the Content
(through NLP, LDA, word embeddings, and a Neural Network)

Doing so allows the app to group similar lessons together, on the fly, enabling:
User Specific Recommendations based on Activity and Lesson Preferences 
(through Matrix Factorization and Deep Neural Network)

...
Why NLP?

topic modeling
checking for duplicate lesson (hasing tokens)

Prototype: LDA

Production: lda2Vec, word2vec, multilingual embeddings, Deep Neural Network, consider Rust HuggingFace tokenizers for speed

Embedding Space

<p align="center">
  <img src=/media/overview-1-shorten2.gif></img>
</p>

Topic Modeling with Embedding

<p align="center">
  <img src=/media/topics-1-shorten2.gif></img>
</p>

            
### Recommendation
recommendation systems consist of 3 key stages:

Why Recommenders?

Prototype: Sparse Matrix Factorization

Pros: quick, reliable when signal is reliable (enough user activity)

Cons: bad with limited data on new users (cold start), inputs restricted to User and Items matrix

Production: Deep Neural Network


Recommender Process:

1. item candidate generation
2. user specific scoring of items
3. reranking, or sorting the items based on relevance to the user


Takeaways:

Learned a number of libraries, such as Keras/Tensorflow, Gensim, and worked with more familiar Pandas and Numpy, and NLTK

Faced the Challenge of working remotely with the software engineer, my friend, in a different time zone, and had to iteratively adjust the app to implement changes

Got experience working with machine learning in a production web development environment; being the domain expert to recommend best practice for performance and scalability; had to weigh trade offs of having a fast working prototype and implementing the best available solutions for a given task, faced this at nearly every step; sometimes making prototype is the clear priority, but some best practices shouldn’t be compromised, and found that out the hard way when late in the project decided to reimplement many features using Keras/Tensorflow to achieve state of the art recommendation, like those seen on Youtube, and FaceBook.

If interested in knowing more about the application, whether you’re the type of polyglot who speaks Spanish and French or the kind who speaks Python and Javascript, feel free to reach out! We intend to keep working on the app until we have a deliverable prototype.


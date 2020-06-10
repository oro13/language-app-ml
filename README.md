# language_app_ml


FELI GENTLE

Totlahtol Language App

Machine Learning Components (Prototype Development, Research)

Implementing Machine Learning Features in a Language App;

Using Natural Language Processing for Topic Modeling to Understand the Content of User Uploaded Lessons; Using Matrix Factorization and Deep Neural Networks to Make User Specific Recommendations based on Activity and Preferences

*Totlahtol* Languages in Nahuatl, the once widely spoken Aztec ‘Lingua Franca’ of . 

My friend in El Paso began working on this application over a year ago; now I’m helping him bring it to fruition. To help the App stand out, we are making a prototype enhanced with machine learning components. We hope it will excel in for user enjoyment and  provide effective language instruction.

While there are many Language Apps out there, few, if any, harness the power of combining: 

 - User Generated Lessons, 
 - Machine Learning accelerated Recommendation of Content specific to User interests and activity, and a 
 - interactive, social-network driven user interface for a personalized immersion the target language. 
 
Totlahtol aims to deliver on all these and more.

## The Data Pipeline

My Research has centered on the most important app use case of uplading a lesson and recommending it to users if their activity implies it'd be relevent to them.

1. A user uploads a lesson
2. NLP for processing the text and discerning the lesson topics
3. The lesson specific word and topic embeddings are available for the recommender model
4. User ratings and lesson activity are made available for the recommender model
5. The recommender gets an input of these and other features about the users and lessons
6. The recommender, a combination of deep neural network and matrix factorization, returns the probable ratings for lessons each user has not seen yet
7. These predicted ratings are sorted to find the highest ratings
8. When a user opens their feed, these lessons are suggested to them first

## ML components

**User Generated Lessons and NLP**

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

            
**ML Recommender**

Why Recommenders?

...what's available

Prototype: Sparse Matrix Factorization

Pros: quick, reliable when signal is reliable (enough user activity)

Cons: bad with limited data on new users (cold start), inputs restricted to User and Items matrix

Production: Deep Neural Network

### Recommendation
recommendation systems consist of 3 key stages:

1. item candidate generation
2. user specific scoring of items
3. reranking, or sorting the items based on relevance to the user



Learned a number of libraries, such as Keras/Tensorflow, Gensim, and worked with more familiar Pandas and Numpy, and NLTK

Faced the Challenge of working remotely with the software engineer, my friend, in a different time zone, and had to iteratively adjust the app to implement changes

Got experience working with machine learning in a production web development environment; being the domain expert to recommend best practice for performance and scalability; had to weigh trade offs of having a fast working prototype and implementing the best available solutions for a given task, faced this at nearly every step; sometimes making prototype is the clear priority, but some best practices shouldn’t be compromised, and found that out the hard way when late in the project decided to reimplement many features using Keras/Tensorflow to achieve state of the art recommendation, like those seen on Youtube, and FaceBook.


If interested in knowing more about the application, whether you’re the type of polyglot who speaks Spanish and French or the kind who speaks Python and Javascript, feel free to reach out! We intend to keep working on the app until we have a deliverable prototype.



Tech used:

Front End 
• React JS
• Flask
• 
Back End 
• SQLAlchemy
• Keras/Tensorflow
• Python/Numpy/Pandas

Project links: 
[Link github repos and demos here]


overview:



recommender pipeline:

    user 1 (uploader) uploads lesson
    topic model lesson content according to large word2vec embedding matrix
        'projector' visualization of topic model (explain how neighbors are calculated for topics)
            https://projector.tensorflow.org/
        explain advantages of using word embedding to find latent topics, vs first attempt with LDA
    store tags with lesson
        show how 2 lessons are considered similar vs 2 that are considered different based on score/latent topics
    user 2 (learner), opens the home screen, prompting a query
    candidate items lessons are prompted (double check position)
        dnn that takes into account user activity likes/dislikes AND the corresponding lesson tags (latent topics + uploader gen tags), in different layers
        possible other models that filter out spam/clickbait/offensive content
    candidate items are ranked on a common scale, taking their different scoring metrics into account

    items are reordered according to this rank

    rerun models every so often to include recent user activity, promotes freshness, diversity of content
        use warm start to avoid retraining entirely (eg for matrix factorization warm start the previously seen embeddings)
    optimize recommender by including different input information such as geographical/demographic info to ensure users see fresh content on new topics

App specific considerations:

    unveil certain supported languages gradually, after enough quality content has been contributed during an 'alpha' testing period
    watch for fairness metrics concerning latent biases in content and recommendations, particularly in languages from areas with ethnic conflict, hegemonic power struggles/propaganda, etc
    seek expert advice
    make models specifically for 'average users' of different clusters,
        consider demographics and observe quality of recommendation
    include content from underrespresented groups in corpus so low volume deters it from being considered

Questions I'm walking away with:

Offline embedding matrix, warm start subsampling

lda2vec plus word2vec

querying for recommendations best practices candidate generation, user specific scoring in efficient time, reranking

when to rerun the model
In [ ]:



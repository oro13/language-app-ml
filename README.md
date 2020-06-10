# language_app_ml


overview:

recommendation systems consist of 3 key stages:

1. item candidate generation
2. user specific scoring of items
3. reranking, or sorting the items based on relevance to the user

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



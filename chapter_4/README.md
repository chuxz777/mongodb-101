HW4_3: create indexes for the blog

1. For home page

db.posts.ensureIndex({ date : -1 })

2. For post by permalink

db.posts.ensureIndex({ permalink : 1 })

3. For posts by tags

db.posts.ensureIndex({tags: 1, date: -1})

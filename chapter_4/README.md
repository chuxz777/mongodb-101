## HW4_3: create indexes for the blog

1. For home page

```js
db.posts.ensureIndex({ date : -1 })
```

2. For post by permalink

```js
db.posts.ensureIndex({ permalink : 1 })
```

3. For posts by tags

```js
db.posts.ensureIndex({tags: 1, date: -1})
```

## HW4_4 : profile log query

```js
db.profile.find({ns:/school2.students/}).sort({millis:-1}).limit(10).pretty()
```

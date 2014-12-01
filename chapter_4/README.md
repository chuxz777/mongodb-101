## HW4_3: create indexes for the blog

For home page

```js
db.posts.ensureIndex({ date : -1 })
```

For post by permalink

```js
db.posts.ensureIndex({ permalink : 1 })
```

For posts by tags

```js
db.posts.ensureIndex({tags: 1, date: -1})
```

## HW4_4 : profile log query

```js
db.profile.find({ns:/school2.students/}).sort({millis:-1}).limit(10).pretty()
```

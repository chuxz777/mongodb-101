## HW5_1 : most frequent author

```js
db.posts.aggregate([
  {
    $unwind : '$comments'
  },
  {
    $group : {
     _id :  '$comments.author' ,
     'count': {"$sum": 1},
    }
  },
  {
    $sort : {
    count : -1
    }
  }
])
```

## HW5_2 : crunching the zipcode dataset

```js
db.zips.aggregate([
  
  {
    $match : {
     $or : [ { state : 'CA' }, { state : 'NY'} ],
    }
  },
  {
    $group : {
      _id : '$city',
      totalPop : { $sum : '$pop' },
    }
  },
  {
    $match : {
     totalPop : { $gte : 25000 }
    }
  },
  {
    $group : {
      _id : 'toto',
      avgPop : { $avg : '$totalPop' },
    }
  }
])
```

## HW5_3 : easy grader

```js
db.grades.aggregate([
  {
    $unwind : '$scores'
  },
  {
    $match : {
      'scores.type' : { $not : /quiz/ }
    }
  },
  {
    $group : {
      _id : { student : '$student_id', class : '$class_id'},
      GPA : { $avg : '$scores.score' },
    }
  },
  {
    $group : {
      _id : '$_id.class',
      class_GPA : { $avg : '$GPA' },
    }
  },
  {
    $sort : {
      class_GPA : -1
    }
  }
])
```

## HW5_4 : removing rural residents

```js
db.zips.aggregate([
  
  {$project: 
     {
    	first_char: {$substr : ["$city",0,1]},
    	city : '$city',
    	pop : '$pop'
     }
  },
  {$match:
    {
      first_char: /[0-9]/
    }
  },
  {$group:
    {
      _id : 'rurals',
      totalPop : { $sum : '$pop' },
    }
  }
])
```


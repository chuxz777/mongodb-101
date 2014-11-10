<!DOCTYPE html>
<html>
<head>
<title>Hello World</title>
</head>
<body>
    <h1>Welcome {{username}}</h1>
    <p>Here are your things:</p>
    <ul>
    % for thing in things:
        <li>{{thing}}</li>
    % end
    </ul>
    <p>What's your favorite fruit?</p>
    <form action="/favorite_fruit" method="POST">
        <input type="text" name="fruit" size="40" value="">
        <input type="submit" value="Submit">
    </form>
</body>
</html>

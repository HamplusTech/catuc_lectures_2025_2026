<?php
require './includes/header.php';
?>
<h1>Log in</h1>
<form method="post">
<fieldset>
    <legend>Fill all Details</legend>
    <div>
        <input type="text" name="username" id="username" placeholder="Username">
    </div>
    <div>
        <input type="password" name="password" id="password" placeholder="Password">
    </div>
    <div>
        <input type="submit" value="Log in" name="login">
        <input type="reset" value="Clear" name="clear">
    </div>
    <h3>New User? <a href="./register.php">Register</a></h3>
</fieldset>
<h4><a href="./index.php">Home</a></h4>
</form>
<?php
include './includes/footer.php';
?>

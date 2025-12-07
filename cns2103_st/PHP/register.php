<?php
require './includes/header.php';
include "./includes/logic/register.php"
?>
<h1>Register</h1>
<form method="post" action=>
<fieldset>
    <legend>Fill all Details</legend>
    <div>
        <input type="text" name="fullname" id="fullname" placeholder="Full name">
    </div>
    <div>
        <input type="text" name="username" id="username" placeholder="Username">
    </div>
    <div>
        <input type="password" name="password" id="password" placeholder="Password">
    </div>
    <div>
        <input type="tel" name="phone" id="phone" placeholder="Phone Number">
    </div>
    <div>
        <select name="gender" id="gender">
            <option value="">Select Gender</option>
            <option value="0">Female</option>
            <option value="1">Male</option>
        </select>
    </div>
    <div>
        <input type="submit" value="Register" name="register">
        <input type="reset" value="Clear" name="clear">
    </div>
    <h3>Already registered? <a href="./login.php">Log in</a></h3>
    <h3><?php echo $msg; ?></h3>
</fieldset>
<h4><a href="./index.php">Home</a></h4>
</form>
<?php
include './includes/footer.php';
?>

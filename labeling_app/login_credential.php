<?php
session_start();

// Redirect to index.php if the user is already authenticated
if (isset($_SESSION['valid_credential'])) {
    header("Location: index.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Credential Required</title>

    <!-- Add Bootstrap CDN link -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <!-- web icon -->
    <link rel="icon" type="image/x-icon" href="resources/icons8-geometry-40.ico" />

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Cambria, Cochin, Georgia, Times, "Times New Roman", serif;
        }
    </style>
</head>

<body>
    <br><br><br><br><br>
    <div class="text-center container px-4 mt-5">
        <!-- Display error messages if any -->
        <?php if (isset($_SESSION['invalid_credential'])) : ?>
            <div class="alert alert-danger" role="alert">
                <?php echo $_SESSION['invalid_credential']; ?>
            </div>
            <?php unset($_SESSION['invalid_credential']); ?>
        <?php endif; ?>

        <?php if (isset($_SESSION['expired_credential'])) : ?>
            <div class="alert alert-warning" role="alert">
                <?php echo $_SESSION['expired_credential']; ?>
            </div>
            <?php unset($_SESSION['expired_credential']); ?>
        <?php endif; ?>

        <form action="verify_credential.php" method="post">
            <div class="form-group">
                <h2>Credential</h2>
                <input type="text" class="text-center form-control" id="credentialInput" name="credentialInput" required>
            </div>
            <br><br>
            <button type="submit" class="btn-lg btn btn-dark" style="width: 12rem;">Send →</button>
        </form>
    </div>

    <!-- Add Bootstrap JS and Popper.js CDN links -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

</body>

</html>
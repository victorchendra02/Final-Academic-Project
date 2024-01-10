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
</head>

<body>
    <div class="container mt-5">
        <form action="verify_credential.php" method="post">
            <div class="form-group">
                <label for="input_text">Credential</label>
                <input type="text" class="form-control" id="input_text" name="input_text" required>
            </div>
            <button type="submit" class="btn btn-primary">Send →</button>
        </form>
    </div>

    <!-- Add Bootstrap JS and Popper.js CDN links -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    <script>
        // Check if there is a value in localstorage named "credential"
        const storedCredential = localStorage.getItem("credential");

        // If the credential is present, redirect users to "index.php"
        if (storedCredential) {
            window.location.href = "index.php";
        }
    </script>

</body>

</html>
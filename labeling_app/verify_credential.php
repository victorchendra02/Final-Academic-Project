<?php
session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // User input from the form
    $enteredCredential = $_POST['credentialInput'];

    require "config.php";

    $conn = new mysqli($servername, $username, $password, $dbname);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Validate the user's credential against the database
    $sql = "SELECT * FROM credential_table WHERE credential = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $enteredCredential);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        if ($row['is_active'] == 1) {
            // Valid credential, set session variable and redirect to index.php
            $_SESSION['valid_credential'] = true;
            $_SESSION['credential_used'] = $enteredCredential;
            header("Location: index.php");
            exit();
        } else {
            // Expired credential, show an error message and redirect back to login_credential.php
            $_SESSION['expired_credential'] = "Credential is expired.";
            header("Location: login_credential.php");
            exit();
        }
    } else {
        // Invalid credential, show an error message and redirect back to login_credential.php
        $_SESSION['invalid_credential'] = "Invalid credential. Please try again.";
        header("Location: login_credential.php");
        exit();
    }

    $stmt->close();
    $conn->close();

} else {
    // If the request is not a POST request, redirect to login_credential.php
    header("Location: login_credential.php");
    exit();
}

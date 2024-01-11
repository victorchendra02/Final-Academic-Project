<?php
session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Clear all sessions
    session_unset();
    session_destroy();

    // Redirect back to index.php or any other desired page
    header("Location: index.php");  // SAME if redirect to `login_credential.php`
    exit();
} else {
    header("Location: index.php");
    exit();
}

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Replace the database connection details
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "artofproblemsolving";

    $conn = new mysqli($servername, $username, $password, $dbname);

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $labels = $_POST['label'];

    // Loop through each label and corresponding id_key
    foreach ($labels as $id_key => $label) {
        // Update the label in the database
        $sql = "UPDATE imo SET label='$label' WHERE id_key='$id_key'";
        $conn->query($sql);
    }

    $conn->close();
    header("Location: index.php"); // Redirect back to the labeling page
}

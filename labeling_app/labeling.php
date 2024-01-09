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

    // Create or update JSON file
    $jsonFile = 'log.json';
    $logData = [];

    if (file_exists($jsonFile)) {
        // Read existing JSON file
        $logData = json_decode(file_get_contents($jsonFile), true);
    }

    // Set the timezone to Asia/Jakarta (UTC+7)
    date_default_timezone_set('Asia/Jakarta');

    // Loop through each label and corresponding id_key
    foreach ($labels as $id_key => $label) {
        // Update the label in the database
        $sql = "UPDATE imo SET label='$label' WHERE id_key='$id_key'";
        $conn->query($sql);

        // Log the action with UTC+7 timestamp
        $logData['time'][] = date('Y-m-d H:i:s');
    }

    // Write the updated log data to the JSON file
    file_put_contents($jsonFile, json_encode($logData));

    $conn->close();
    header("Location: index.php"); // Redirect back to the labeling page
}

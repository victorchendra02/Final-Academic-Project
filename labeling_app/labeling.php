<?php
session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user_input = $_POST['data_to_parse'];

    // ----------------- LOG -----------------
    // Set the timezone to Asia/Jakarta (UTC+7)
    date_default_timezone_set('Asia/Jakarta');
    $jsonFile = 'log.json';
    $logData = [];

    // Check for different client IP headers
    if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
        $ipaddress = $_SERVER['HTTP_CLIENT_IP'];
    } elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
        $ipaddress = $_SERVER['HTTP_X_FORWARDED_FOR'];
    } else {
        $ipaddress = $_SERVER['REMOTE_ADDR'];
    }

    // Read existing JSON file
    if (file_exists($jsonFile)) {
        $logData = json_decode(file_get_contents($jsonFile), true);
    }
    // ---------------------------------------

    // Validate user input
    // Input is null
    if (count($user_input) == 0) {
        // ----------------- LOG ACTION -----------------
        $logData['time'][] = date('Y-m-d H:i:s');
        $logData['ipaddress'][] = $ipaddress;
        $logData['status'][] = "invalid input";

        // Write the updated log data to the JSON file
        file_put_contents($jsonFile, json_encode($logData));
        // ---------------------------------------------

        $_SESSION['emptyinput'] = "Please provides input!";
        header("Location: index.php");
        exit();

    // Input not null
    } else {
        $servername = "localhost";
        $username = "root";
        $password = "";
        $dbname = "artofproblemsolving";

        // Create database connection
        $conn = new mysqli($servername, $username, $password, $dbname);

        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        // Use prepared statements to prevent SQL injection
        $stmt = $conn->prepare("UPDATE imo SET label=? WHERE id_key=?");
        $stmt->bind_param("si", $label, $id_key);

        // Loop through each label and corresponding id_key
        foreach ($user_input as $id_key => $label) {
            // Update the label in the database using prepared statements
            $stmt->execute();
        }

        // Close the prepared statement
        $stmt->close();

        // ----------------- LOG ACTION -----------------
        $logData['time'][] = date('Y-m-d H:i:s');
        $logData['ipaddress'][] = $ipaddress;
        $logData['status'][] = "submitted";

        // Write the updated log data to the JSON file
        file_put_contents($jsonFile, json_encode($logData));
        // ---------------------------------------------

        // Close the database connection
        $conn->close();

        // Redirect back to the labeling page
        $_SESSION['submitsuccess'] = "Data successfully submitted!";
        header("Location: index.php");
        exit();
    }
}

<?php
session_start();

// Check if the user has entered credentials
if (!isset($_SESSION['valid_credential'])) {
    header("Location: login_credential.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>IMO Classification</title>

    <!-- Add Bootstrap CDN link -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <!-- web icon -->
    <link rel="icon" type="image/x-icon" href="resources/icons8-geometry-40.ico" />

    <!-- style -->
    <link rel="stylesheet" type=text/css href="styles/style.css" />

</head>

<body>
    <svg xmlns="http://www.w3.org/2000/svg" class="d-none">
        <symbol id="check-circle-fill" viewBox="0 0 16 16">
            <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"></path>
        </symbol>
        <symbol id="info-fill" viewBox="0 0 16 16">
            <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zm.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2z"></path>
        </symbol>
        <symbol id="exclamation-triangle-fill" viewBox="0 0 16 16">
            <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"></path>
        </symbol>
    </svg>

    <div class="m-5">
        <!-- Alert for notification -->
        <?php

        // Check for error message
        if (isset($_SESSION['emptyinput'])) {
            $message = $_SESSION['emptyinput'];
            unset($_SESSION['emptyinput']); // Clear the session variable
            echo "
                <div class='alert alert-warning d-flex align-items-center alert-dismissible fade show' role='alert'>
                    <svg class='bi flex-shrink-0 me-2' role='img' aria-label='Warning:' height='1em' width='1em'><use xlink:href='#exclamation-triangle-fill'/></svg>
                    <div>$message</div>
                    <button type='button' class='btn-close' data-bs-dismiss='alert' aria-label='Close'></button>
                </div>
            ";
        }

        // Check for success message
        if (isset($_SESSION['submitsuccess'])) {
            $message = $_SESSION['submitsuccess'];
            unset($_SESSION['submitsuccess']); // Clear the session variable
            echo "
                <div class='alert alert-success d-flex align-items-center alert-dismissible fade show' role='alert'>
                    <svg class='bi flex-shrink-0 me-2' role='img' aria-label='Success:' height='1em' width='1em'><use xlink:href='#check-circle-fill'></use></svg>
                    <div>$message</div>
                    <button type='button' class='btn-close' data-bs-dismiss='alert' aria-label='Close'></button>
                </div>
            ";
        }
        ?>

        <!-- FOR MAINTENANCE -->
        <!-- <div class="text-center alert alert-primary" role="alert">
            We're under maintenance 🔨 <br>
            Please wait ☺️
        </div> -->
        <!-- FOR MAINTENANCE -->

        <h1>IMO Classification</h1>

        <form action="verify_submission.php" method="post" id="labelForm">

            <table class="table table-hover">
                <thead>
                    <tr class="table-dark">
                        <th scope="col">ID</th>
                        <th scope="col">No</th>
                        <th scope="col">Problem</th>
                        <th scope="col">Year</th>
                        <th scope="col" style="width: 6rem;">Link</th>
                        <th scope="col" style="width: 12rem;">Label</th>
                    </tr>
                </thead>

                <tbody>
                    <!-- Fetch and display shuffled data from your database where label is NULL -->
                    <?php
                    // Fetch data from your database and display rows
                    $servername = "localhost";
                    $username = "root";  // aopsimol_root
                    $password = "";      // <aopsimol_root>
                    $dbname = "aopsimol_artofproblemsolving";

                    $conn = new mysqli($servername, $username, $password, $dbname);

                    if ($conn->connect_error) {
                        die("Connection failed: " . $conn->connect_error);
                    }

                    $sql = "SELECT id_key, no, post_rendered, year, link, label FROM imo WHERE label IS NULL";
                    $result = $conn->query($sql);

                    if ($result->num_rows > 0) {
                        // Fetch all rows into an associative array
                        $rows = $result->fetch_all(MYSQLI_ASSOC);

                        // Shuffle the array
                        shuffle($rows);

                        // Limit the array to the first 20 elements
                        $selectedRows = array_slice($rows, 0, 20);

                        // Process the selected rows and display them
                        foreach ($selectedRows as $row) {
                            echo "<tr>";
                            echo "<td>" . $row['id_key'] . "</td>";
                            echo "<td class='text-danger'>" . $row['no'] . "</td>";
                            echo "<td>" . $row['post_rendered'] . "</td>";
                            echo "<td class='text-success' style='font-size: 14px;'>" . $row['year'] . "</td>";
                            echo "<td><a href='" . $row['link'] . "' target='_blank'>check</a></td>";
                            echo "<td><select class='form-select' name='data_to_parse[" . $row['id_key'] . "]' aria-label='Label selection'>
                                        <option value='' selected disabled hidden></option>
                                        <option value='Algebra'>Algebra</option>
                                        <option value='Combinatorics'>Combinatorics</option>
                                        <option value='Geometry'>Geometry</option>
                                        <option value='Number Theory'>Number Theory</option>
                                    </select></td>";
                            echo "</tr>";
                        }
                    } else {
                        echo "<tr><td colspan='6'>No data to label!</td></tr>";
                    }

                    $conn->close();
                    ?>
                </tbody>
            </table>

            <div class="text-center">
                <p class="p-3" style="background-color: #F8E559; border-radius: 10px;">
                    <strong>NOTE:</strong> Please ensure that your inputs are correct before submitting. Submissions cannot be reversed. Thank you!
                </p>
                <br>

                <!-- Button to trigger the modal -->
                <!-- FOR MAINTENANCE -->
                <!-- <button type="button" class="btn btn-lg btn-dark" data-bs-toggle="modal" data-bs-target="#confirmationModalUnderMaintenance" style="width: 20rem;"> -->
                <!-- FOR MAINTENANCE -->
                <button type="button" class="btn btn-lg btn-dark" data-bs-toggle="modal" data-bs-target="#confirmationModal" style="width: 20rem;">
                    Submit →
                </button>

                <br>
                <p>Your submission is highly appreciated!</p>
            </div>

        </form>

    </div>

    <!-- Bootstrap modal for confirmation -->
    <!-- Good -->
    <div class="modal fade" id="confirmationModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Confirmation!</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    Are you sure you want to submit?
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-primary" id="submitBtn">Submit</button>
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Under maintenance -->
    <div class="modal fade" id="confirmationModalUnderMaintenance" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Under Maintenance! 🔨</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    Sorry, but we're under maintenance :( <br>
                    Try again or try to contact support.
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>

    <!-- JavaScript to handle the modal confirmation and form submission -->
    <script>
        document.getElementById('submitBtn').addEventListener('click', function() {
            document.getElementById('labelForm').submit();
        });
    </script>

    <!-- Add Bootstrap JS and Popper.js CDN links -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    <!-- Footer -->
    <br><br><br>
    <footer class="bg-dark text-white text-center p-5">
        <h1 class="display-4">THANK YOU</h1>

        <div class="container">
            <p class="lead">
                Created by Victor Chendra <br>
                Student at Calvin Institute of Technology <br>
                Majoring in IT & Big Data Analytics
            </p>

            <div class="mt-4">
                <p class="mb-1">Contact:</p>
                <a class="text-white" target="_blank" href="mailto:victorchendra02@gmail.com?subject=About%20IMO%20Classification%20App">victorchendra02@gmail.com</a> <br>
                <a class="text-white" target="_blank" href="https://instagram.com/victorchendraa">instagram.com/victorchendraa</a> <br>
            </div>
        </div>
    </footer>

</body>

</html>
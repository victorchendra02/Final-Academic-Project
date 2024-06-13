<?php
session_start();
header('Content-Type: text/html; charset=utf-8');

// Check if the user has entered credentials
if (!isset($_SESSION['valid_credential'])) {
    header("Location: login_credential.php");
    exit();
}

require "config.php";
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

    <div class="m-5 mt-4">
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

        <!-- NOTIFICATION DO NOT REFRESH PAGE -->
        <div class='alert alert-warning d-flex align-items-center alert-dismissible fade show' role='alert'>
            <svg class='bi flex-shrink-0 me-2' role='img' aria-label='Warning:' height='1em' width='1em'>
                <use xlink:href='#info-fill' />
            </svg>
            <div>
                <strong>NOTE:</strong> Do not refresh the page! <br>
                <strong>IF</strong> labels that have been assigned (but not yet submitted) <strong>will not be saved</strong>, and <strong>the data will be shuffled</strong>.
            </div>
            <button type='button' class='btn-close' data-bs-dismiss='alert' aria-label='Close'></button>
        </div>

        <!-- NOTIFICATION SAFE TO REFRESH -->
        <div class='alert alert-warning d-flex align-items-center alert-dismissible fade show' role='alert'>
            <svg class='bi flex-shrink-0 me-2' role='img' aria-label='Warning:' height='1em' width='1em'>
                <use xlink:href='#info-fill' />
            </svg>
            <div>
                <strong>NOTE:</strong> Refresh page if no data shown on table.
            </div>
            <button type='button' class='btn-close' data-bs-dismiss='alert' aria-label='Close'></button>
        </div>

        <!-- NOTIFICATION YOU CAN LEAVE BLANK -->
        <div class='alert alert-info d-flex align-items-center alert-dismissible fade show' role='alert'>
            <svg class='bi flex-shrink-0 me-2' role='img' aria-label='Warning:' height='1em' width='1em'>
                <use xlink:href='#info-fill' />
            </svg>
            <div>
                <strong>NOTE:</strong> You can still submit and leave it blank if you're not sure (Only those that have been labeled will be submitted).
            </div>
            <button type='button' class='btn-close' data-bs-dismiss='alert' aria-label='Close'></button>
        </div>

        <!-- FOR MAINTENANCE -->
        <!-- <div class="text-center alert alert-primary" role="alert">
            We're under maintenance 🔨 <br>
            Please wait ☺️
        </div> -->
        <!-- FOR MAINTENANCE -->

        <!-- h1 & End session button -->
        <div class="d-flex justify-content-between align-items-center mb-4">
            <!-- Heading -->
            <h1 class="m-0">IMO Classification</h1>

            <!-- END SESSION BUTTON -->
            <form action="end_session.php" method="post">
                <button type="submit" class="btn btn-danger" name="end_session" style="width: 150px; height: 100%;">End Session</button>
            </form>
        </div>
        <hr class="mb-4">

        <!-- Display Current Database Information -->
        <?php
        $conn = new mysqli($servername, $username, $password, $dbname);

        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        $query = "
            SELECT 
                COUNT(*) AS total,
                SUM(CASE WHEN label='Algebra' THEN 1 ELSE 0 END) AS algebra_count,
                SUM(CASE WHEN label='Combinatorics' THEN 1 ELSE 0 END) AS combinatorics_count,
                SUM(CASE WHEN label='Geometry' THEN 1 ELSE 0 END) AS geometry_count,
                SUM(CASE WHEN label='Number Theory' THEN 1 ELSE 0 END) AS number_theory_count,
                SUM(CASE WHEN label IS NULL THEN 1 ELSE 0 END) AS null_label_count,
                SUM(CASE WHEN label IS NOT NULL THEN 1 ELSE 0 END) AS not_null_label_count
            FROM `imo`
            WHERE contest_name NOT IN (
                'imc', 
                'simon_marais_mathematical_competition'
            )
            AND id_key NOT IN (277, 1236, 1237, 1238, 1239, 1240, 1241)
        ;";

        $result = $conn->query($query);

        if ($result === false) {
            // Handle the error, for example:
            die("Error executing the query: " . $conn->error);
        }

        $row = $result->fetch_assoc();

        $total = $row['total'];
        $algebra = $row['algebra_count'];
        $combinatorics = $row['combinatorics_count'];
        $geometry = $row['geometry_count'];
        $number_theory = $row['number_theory_count'];
        $null_label = $row['null_label_count'];
        $not_null_label = $row['not_null_label_count'];

        $conn->close();
        ?>

        <!-- Display Current Database Information -->
        <div class="container mb-4">
            <h2>Information</h2>

            <div class="row">
                <div class="col-md-6">
                    <div class="card text-center">
                        <div class="card-header bg-info">
                            Total
                        </div>
                        <div class="card-body">
                            <h4 class="card-title"><?php echo $total; ?></h4>
                            Data
                        </div>
                    </div>

                    <br>

                    <div class="row">
                        <div class="col-md-6">
                            <div class="card text-center">
                                <div class="card-header bg-success" style="color: #FFFFFF;">
                                    Labeled
                                </div>
                                <div class="card-body">
                                    <h4 class="card-title"><?php echo $not_null_label; ?></h4>
                                    Data
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="card text-center">
                                <div class="card-header bg-danger" style="color: #FFFFFF;">
                                    Not labeled
                                </div>
                                <div class="card-body">
                                    <h4 class="card-title"><?php echo $null_label; ?></h4>
                                    Data
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-md-6">
                    <div class="row" style="height: 100%;">
                        <div class="row">
                            <div class="col-md-6">
                                <div class="card text-center">
                                    <div class="card-header">
                                        Label
                                    </div>
                                    <div class="card-body">
                                        <h4><?php echo $algebra; ?></h4>
                                        Algebra
                                    </div>
                                </div>
                            </div>

                            <div class="col-md-6">
                                <div class="card text-center">
                                    <div class="card-header">
                                        Label
                                    </div>
                                    <div class="card-body">
                                        <h4><?php echo $combinatorics; ?></h4>
                                        Combinatorics
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="row">
                            <div class="col-md-6">
                                <br>
                                <div class="card text-center">
                                    <div class="card-header">
                                        Label
                                    </div>
                                    <div class="card-body">
                                        <h4><?php echo $geometry; ?></h4>
                                        Geometry
                                    </div>
                                </div>
                            </div>

                            <div class="col-md-6">
                                <br>
                                <div class="card text-center">
                                    <div class="card-header">
                                        Label
                                    </div>
                                    <div class="card-body">
                                        <h4><?php echo $number_theory; ?></h4>
                                        Number Theory
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Progression bar -->
        <div class="progress mb-4">
            <div class="progress-bar bg-success progress-bar-striped progress-bar-animated" role="progressbar" style="width: <?php echo ($not_null_label / $total) * 100; ?>%;" aria-valuenow="<?php echo $not_null_label; ?>" aria-valuemin="0" aria-valuemax="<?php echo $total; ?>">
                <?php echo round(($not_null_label / $total) * 100, 1); ?>%
            </div>
        </div>

        <form action="verify_submission.php" method="post" id="labelForm">

            <table class="table table-hover">
                <thead>
                    <tr class="table-dark">
                        <th scope="col">ID</th>
                        <th scope="col">No</th>
                        <th scope="col">Problem</th>
                        <th scope="col">Contest name</th>
                        <th scope="col">Year</th>
                        <th scope="col" style="width: 6rem;">Link</th>
                        <th scope="col" style="width: 12rem;">Label</th>
                    </tr>
                </thead>

                <tbody>
                    <!-- Fetch and display shuffled data from your database where label is NULL -->
                    <?php
                    // Fetch data from your database and display rows

                    $conn = new mysqli($servername, $username, $password, $dbname);
                    $conn->set_charset('utf8mb4'); // Set the character set to utf8mb4

                    if ($conn->connect_error) {
                        die("Connection failed: " . $conn->connect_error);
                    }

                    // $sql = "SELECT id_key, no, post_rendered, year, link, label FROM imo WHERE contest_name='imo' AND label IS NULL";
                    $sql = "
                        SELECT 
                            id_key, 
                            no, 
                            post_rendered, 
                            contest_name, 
                            year, 
                            link, 
                            label 
                        FROM imo 
                        WHERE contest_name IN (
                            'lusophon_mathematical_olympiad',
                            'romanian_masters_of_mathematics_collection',
                            'imo_shortlist',
                            'european_mathematical_cup',
                            'balkan_mo',
                            'junior_balkan_mo',
                            'baltic_way',
                            'imo_longlists'
                        )
                        
                        AND contest_name NOT IN (
                            'imc', 
                            'simon_marais_mathematical_competition'
                        )
                        AND id_key NOT IN (277, 1236, 1237, 1238, 1239, 1240, 1241)
                        AND label IS NULL
                    ;";
                    $result = $conn->query($sql);

                    if ($result->num_rows > 0) {
                        // Fetch all rows into an associative array
                        $rows = $result->fetch_all(MYSQLI_ASSOC);

                        // Shuffle the array
                        shuffle($rows);

                        // Limit the array to the first 20 elements
                        $selectedRows = array_slice($rows, 0, 50);

                        // Process the selected rows and display them
                        foreach ($selectedRows as $row) {
                            echo "<tr>";
                            echo "<td>" . $row['id_key'] . "</td>";
                            echo "<td class='text-danger'>" . $row['no'] . "</td>";
                            echo "<td>" . $row['post_rendered'] . "</td>";
                            echo "<td class='text-success' style='font-size: 14px;'>" . $row['contest_name'] . "</td>";
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
                        echo "<tr><td colspan='6'>All data has been labeled. Thank you very much 😊</td></tr>";
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
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>IMO Classification</title>

    <!-- Add Bootstrap CDN link -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

    <!-- web icon -->
    <link rel="icon" type="image/x-icon" href="icons8-geometry-40.png" />

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
        }
    </style>

    <!-- style -->
    <!-- <link rel="stylesheet" type=text/css href="resources/styles.css" /> -->

</head>

<body>
    <div class="m-5">
        <h1>IMO Classification</h1>

        <form action="labeling.php" method="post">

            <table class="table table-hover">
                <thead>
                    <tr class="table-dark">
                        <th scope="col">ID</th>
                        <th scope="col">No</th>
                        <th scope="col">Problem</th>
                        <th scope="col">Year</th>
                        <th scope="col">Link</th>
                        <th scope="col" style="width: 170px;">Label</th>
                    </tr>
                </thead>

                <tbody>
                    <!-- Fetch and display data from your database -->
                    <?php
                    // Fetch data from your database and display rows
                    $servername = "localhost";
                    $username = "root";
                    $password = "";
                    $dbname = "artofproblemsolving";

                    $conn = new mysqli($servername, $username, $password, $dbname);

                    if ($conn->connect_error) {
                        die("Connection failed: " . $conn->connect_error);
                    }

                    $sql = "SELECT id_key, no, post_rendered, year, link, label FROM imo WHERE label IS NULL LIMIT 7;";
                    $result = $conn->query($sql);

                    if ($result->num_rows > 0) {
                        while ($row = $result->fetch_assoc()) {
                            echo "<tr>";
                            echo "<td>" . $row['id_key'] . "</td>";
                            echo "<td>" . $row['no'] . "</td>";
                            echo "<td>" . $row['post_rendered'] . "</td>";
                            echo "<td>" . $row['year'] . "</td>";
                            echo "<td><a href='" . $row['link'] . "' target='_blank'>" . $row['link'] . "</a></td>";
                            echo "<td><select class='p-1' name='data_to_parse[" . $row['id_key'] . "]'>
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
            <br>

            <input type="submit" class="btn btn-lg btn-dark px-5" value="Submit" onclick="return confirm('Are you sure you want to submit?')">
        </form>

    </div>

    <!-- Add Bootstrap JS and Popper.js CDN links -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
</body>

</html>
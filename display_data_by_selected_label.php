<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IMO Data Display</title>

    <!-- Add Bootstrap CSS link here -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <style>
        body {
            padding: 20px;
        }
    </style>
</head>

<body>
    <div class="container">
        <h2 class="mt-4 mb-4">IMO Display Labeled Data</h2>

        <!-- Dropdown menu for selecting the label -->
        <form method="post" class="mb-4" id="labelForm">
            <label for="labelSelect" class="form-label">Select Label:</label>
            <select name="label" id="labelSelect" class="form-select" onchange="submitForm()">
                <option value="" selected disabled hidden></option>
                <option value="Algebra">Algebra</option>
                <option value="Combinatorics">Combinatorics</option>
                <option value="Geometry">Geometry</option>
                <option value="Number Theory">Number Theory</option>
            </select>
        </form>

        <?php
        // Database credentials
        $servername = "localhost";
        $username = "root";
        $password = "";
        $dbname = "aopsimol_artofproblemsolving";

        // Database connection
        $conn = new mysqli($servername, $username, $password, $dbname);

        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        // Fetch data based on the selected label
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $selectedLabel = $_POST["label"];
            $sql = "SELECT id_key, no, post_rendered, year, link, label FROM `imo` WHERE label='$selectedLabel'";
            $result = $conn->query($sql);
        } else {
            // Default query for Algebra
            $sql = "SELECT id_key, no, post_rendered, year, link, label FROM `imo` WHERE label='Algebra'";
            $result = $conn->query($sql);
        }

        // Pagination configuration
        $results_per_page = 10;
        $number_of_results = $result->num_rows;
        $number_of_pages = ceil($number_of_results / $results_per_page);

        // Get current page number
        if (!isset($_GET['page'])) {
            $page = 1;
        } else {
            $page = $_GET['page'];
        }

        // Calculate the SQL LIMIT starting number for the results on the displaying page
        $this_page_first_result = ($page - 1) * $results_per_page;

        // Display data in a table
        if ($result->num_rows > 0) {
            echo "<table class='table table-bordered table-hover'>
                <thead class='table-primary'>
                    <tr>
                        <th scope='col'>ID</th>
                        <th scope='col'>No</th>
                        <th scope='col'>Post Rendered</th>
                        <th scope='col'>Year</th>
                        <th scope='col'>Link</th>
                        <th scope='col'>Label</th>
                    </tr>
                </thead>
                <tbody>";

            // Modify your SQL query to include LIMIT for pagination
            $sql .= " LIMIT $this_page_first_result, $results_per_page";
            $result = $conn->query($sql);

            while ($row = $result->fetch_assoc()) {
                echo "<tr>
                    <td>" . $row["id_key"] . "</td>
                    <td>" . $row["no"] . "</td>
                    <td>" . $row["post_rendered"] . "</td>
                    <td>" . $row["year"] . "</td>
                    <td><a href='" . $row["link"] . "' target='_blank'>link</a></td>
                    <td>" . $row["label"] . "</td>
                </tr>";
            }

            echo "</tbody></table>";

            // Display pagination links
            echo "<nav aria-label='Page navigation'>";
            echo "<ul class='pagination justify-content-center'>";

            // Previous button
            if ($page > 1) {
                echo "<li class='page-item'><a class='page-link' href='?page=" . ($page - 1) . "'>&laquo; Previous</a></li>";
            } else {
                echo "<li class='page-item disabled'><span class='page-link'>&laquo; Previous</span></li>";
            }

            // First page button
            if ($page > 3) {
                echo "<li class='page-item'><a class='page-link' href='?page=1'>1</a></li>";
                echo "<li class='page-item disabled'><span class='page-link'>...</span></li>";
            }

            // Page numbers
            $start_page = max(1, $page - 2);
            $end_page = min($number_of_pages, $start_page + 4);

            for ($i = $start_page; $i <= $end_page; $i++) {
                echo "<li class='page-item";
                if ($i == $page) {
                    echo " active";
                }
                echo "'><a class='page-link' href='?page=" . $i . "'>" . $i . "</a></li>";
            }

            // Last page button
            if ($page < $number_of_pages - 2) {
                echo "<li class='page-item disabled'><span class='page-link'>...</span></li>";
                echo "<li class='page-item'><a class='page-link' href='?page=" . $number_of_pages . "'>" . $number_of_pages . "</a></li>";
            }

            // Next button
            if ($page < $number_of_pages) {
                echo "<li class='page-item'><a class='page-link' href='?page=" . ($page + 1) . "'>Next &raquo;</a></li>";
            } else {
                echo "<li class='page-item disabled'><span class='page-link'>Next &raquo;</span></li>";
            }

            echo "</ul></nav>";
        } else {
            echo "<p class='mt-4'>0 results</p>";
        }

        // Close the database connection
        $conn->close();
        ?>

    </div>

    <!-- Add Bootstrap JS and Popper.js scripts here -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    <script>
        // JavaScript function to submit the form on dropdown change
        function submitForm() {
            document.getElementById("labelForm").submit();
        }
    </script>
</body>

</html>
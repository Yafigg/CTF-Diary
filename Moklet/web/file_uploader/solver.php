<?php

// Specify the file you want to read
$file = 'flag.txt';

// Check if the file exists before trying to read it
if (file_exists($file)) {
    // Read the file content
    $content = file_get_contents($file);

    // Display the file content
    echo nl2br(htmlspecialchars($content));
} else {
    echo "File not found.";
}

?>

<?php
        if ($_SERVER["REQUEST_METHOD"] == "PUT")

        {
        unset($_PUT['submit']);
        exec('run01.sh');
        }
?>
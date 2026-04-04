#!/bin/bash

# Update system
yum update -y

# Install Apache & PHP
yum install -y httpd php php-mysqlnd

# Start Apache
systemctl start httpd
systemctl enable httpd

# Create sample app
cat <<EOF > /var/www/html/index.php
<?php
\$conn = new mysqli("DB_ENDPOINT", "admin", "password", "mydb");

if (\$conn->connect_error) {
    die("Connection failed: " . \$conn->connect_error);
}

echo "Connected to RDS successfully!";
?>
EOF

# Set permissions
chown -R apache:apache /var/www/html
chmod -R 755 /var/www/html

# Restart Apache
systemctl restart httpd

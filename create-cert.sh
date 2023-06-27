#!/bin/bash

# Generate a self-signed SSL certificate and private key

# Set the common name for the certificate (e.g., domain name)
COMMON_NAME="C:\Program Files\Git\CN=example.com"

# Set the validity period for the certificate (in days)
VALIDITY_DAYS=365

# Set the output directory for the certificate and key
OUTPUT_DIR="./ssl"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Generate the private key
openssl genrsa -out "$OUTPUT_DIR/private.key" 2048

# Generate the certificate signing request (CSR)
openssl req -new -key "$OUTPUT_DIR/private.key" -out "$OUTPUT_DIR/certificate.csr" -subj "/CN=$COMMON_NAME"

# Generate the self-signed certificate using the private key and CSR
openssl x509 -req -in "$OUTPUT_DIR/certificate.csr" -signkey "$OUTPUT_DIR/private.key" -out "$OUTPUT_DIR/certificate.crt" -days $VALIDITY_DAYS

# Print the summary of the generated certificate
openssl x509 -in "$OUTPUT_DIR/certificate.crt" -text -noout

echo "SSL certificate and private key generated successfully!"
echo "Certificate path: $OUTPUT_DIR/certificate.crt"
echo "Private key path: $OUTPUT_DIR/private.key"

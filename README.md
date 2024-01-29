# Lonca Case Study Project

## Introduction

This project is a Python-based application that transforms raw product data into a more structured and usable format. It uses BeautifulSoup to parse and extract specific information from the product descriptions.

## Getting Started

To get this project up and running, follow the steps below:

### 1. Clone the repository

Clone this repository to your local machine using `git clone`.

```bash
git clone https://github.com/egebgs/lonca-case-study.git
```

### 2. Install the requirements
This project uses Python and pip. Make sure you have both installed on your machine. Then, navigate to the project directory and run the following command to install the necessary Python packages.

```bash
pip install -r requirements.txt
```

### 3. Set up the environment variables

The project uses environment variables to configure certain aspects of its operation. These are defined in the .env file. Set the port, database_name, and collection_name according to your MongoDB setup. The environment variables will be provided.

### 4. Run the application

You can run the project using your preferred Python IDE. If you're using the command line, navigate to the project directory and run:

```bash
python main.py
```

### Design Decisions

The project is designed with simplicity and modularity in mind. The main function, transform_data, takes in raw product data and transforms it into a more structured format. This function uses helper functions to extract specific pieces of information from the product descriptions.

The extract_description_info function uses BeautifulSoup to parse the HTML in the product descriptions and extract specific pieces of information. This function is designed to be flexible and can easily be modified to extract different pieces of information if needed.
The transformed data includes detailed product information such as product ID, name, images, price, discounted price, product type, quantity, color, fabric, series, sample size, model measurements, product measurements, status, and whether the product is discounted.

The project uses environment variables for configuration to make it easy to adapt the project to different environments without changing the code. These variables are defined in the .env file.

It is important to note that the 'price unit' field is empty since there are no example uses in the raw data. If there were, the 'price unit' field would be populated with the corresponding price unit by the implementation of the extraction function.
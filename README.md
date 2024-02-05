Laundry Management System (LMS)

Table of Contents

		Overview
		Features
Installation
Step 1: Clone the Repository
Step 2: Create Virtual Environment
Step 3: Activate Virtual Environment
Step 4: Install Dependencies
Step 5: Apply Database Migrations
Step 6: Create Superuser (Admin)
Step 7: Run the Development Server
Step 8: Visit Admin Interface
Step 9: Access Application
Usage
Laundry Requests
Complaints
Order Tracking
		Contributing
		License
Overview

The Laundry Management System (LMS) is a robust web application developed using Django, designed to streamline laundry-related tasks within an academic institution. From submitting laundry requests to tracking orders and handling complaints, LMS provides an intuitive interface for seamless user interaction.

Features

		Laundry Requests
Users can easily submit laundry requests by providing essential details such as personal information, service type (Dryclean or NormalWash), quantity, and the expected delivery date.
		Complaints
Users have the flexibility to raise complaints, providing valuable feedback on specific orders or general suggestions. This feature enhances communication and ensures user satisfaction.
		Order Tracking
The system enables users to track the status of their laundry orders, providing transparency and efficient order management.
Installation

Step 1: Clone the Repository

bash



Copy code

git clone https://github.com/your-username/lms.git cd lms

Step 2: Create Virtual Environment

bash



Copy code

python -m venv venv

Step 3: Activate Virtual Environment

On Windows:

bash



Copy code

venv\Scripts\activate

On macOS/Linux:

bash



Copy code

source venv/bin/activate

Step 4: Install Dependencies

bash



Copy code

pip install -r requirements.txt

Step 5: Apply Database Migrations

bash



Copy code

python manage.py migrate

Step 6: Create Superuser (Admin)

bash



Copy code

python manage.py createsuperuser

Step 7: Run the Development Server

bash



Copy code

python manage.py runserver

Step 8: Visit Admin Interface

Open a browser and go to http://127.0.0.1:8000/admin/ to log in with the superuser credentials.

Step 9: Access Application

Visit http://127.0.0.1:8000/ to access the Laundry Management System.

Usage

Laundry Requests

		Navigate to the "Laundry Request" section in the user interface.
		Fill in the required details.
		Submit your request.
Complaints

		Visit the "Raise Complaints" section.
		Provide order-specific or general feedback.
Order Tracking

Check the "Track Status" page to monitor the progress of your laundry orders.

Contributing

Contributions to the project are welcome! Please follow the Contribution Guidelines for more details.

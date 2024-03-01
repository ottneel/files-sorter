This project is inspired by [Alex Freberg's](https://www.linkedin.com/in/alex-freberg?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BloKu8xQsQ0uVDWhlYpqDVw%3D%3D) [Python](https://youtu.be/gs0FNQR0njI?si=fOlRC_ZVdlc9qNbr) video on creating an automatic file sorter. It takes a directory path as input and utilizes Python standard library modules such as **os, shutil, and sys**. For each file in the directory, the script creates folders based on their file extensions and moves the files into their respective folders. For instance, if the directory contains CSVs and PDFs, the script will generate a "csv" folder and a "pdf" folder, then relocate the CSVs and PDFs accordingly, ensuring each file is housed in its appropriate folder.

While the script performs effectively in most scenarios, it may encounter performance issues with directories containing a large number of files. Additionally, it lacks robust error handling and unit testing capabilities.

Nevertheless, I find this script valuable as it provided an opportunity for me to practise my Python programming skills and enhance my logical thinking. It also helped me organize my media directory.


I created a Docker image for my file sorter script. It's a simple way for people to run the script in a container without any setup hassle.






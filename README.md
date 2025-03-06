# Student Portfolio

This project is a personal portfolio built using Python Streamlit, showcasing my academic journey, projects, skills, and achievements. The portfolio is designed to stand out to tech recruiters and provide a comprehensive view of my capabilities and experiences.

## Table of Contents
- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/your-username/student-portfolio.git
   ```
2. Navigate to the project directory:
   ```
   cd student-portfolio
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Features

- **Home Page**: Displays personal profile information and a downloadable resume.
- **Projects Section**: Showcases various projects with filtering options.
- **Skills & Achievements**: Visual representation of skills using progress bars.
- **Customize Profile**: Dynamic editing of profile details.
- **Contact Form**: Allows visitors to send messages and connect via social media links.
- **Testimonials**: Section for classmates and mentors to leave feedback.
- **Animations**: Smooth transitions and hover effects for an enhanced user experience.

## Usage

To run the portfolio, execute the following command in the project directory:
```
streamlit run portfolio.py
```
This will start a local server, and you can view the portfolio in your web browser at `http://localhost:8501`.

## Project Structure

```
student-portfolio
├── src
│   ├── pages
│   │   ├── home.py
│   │   ├── projects.py
│   │   ├── skills_achievements.py
│   │   ├── customize_profile.py
│   │   └── contact.py
│   ├── components
│   │   ├── project_card.py
│   │   ├── skill_bar.py
│   │   └── testimonial.py
│   ├── assets
│   │   ├── profile_picture.jpg
│   │   └── resume.pdf
│   └── utils
│       ├── filters.py
│       └── animations.py
├── .gitignore
├── requirements.txt
├── portfolio.py
└── README.md
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or features, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
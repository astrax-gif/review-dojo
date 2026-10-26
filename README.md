<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=220&section=header&text=Review%20Dojo&fontSize=70&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Train%20your%20code%20review%20skills&descAlignY=58&descSize=20" alt="Review Dojo banner" width="100%" />

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=36BCF7&center=true&vCenter=true&width=700&lines=Spot+the+bug+before+it+ships.;Review+realistic+pull+requests.;Catch+security+holes+and+messy+design.;Get+scored.+Learn+why.+Level+up." alt="Typing animation" />
</a>

<br/>

![Status](https://img.shields.io/badge/status-in%20development-orange?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Frontend](https://img.shields.io/badge/frontend-TypeScript%20%2B%20React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Backend](https://img.shields.io/badge/backend-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Database](https://img.shields.io/badge/database-PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)

</div>

---

## Table of Contents

1. [What is Review Dojo?](#what-is-review-dojo)
2. [The Problem](#the-problem)
3. [The Solution](#the-solution)
4. [Who Is It For?](#who-is-it-for)
5. [How It Works](#how-it-works)
6. [Planned Features](#planned-features)
7. [Tech Stack](#tech-stack)
8. [Project Structure](#project-structure)
9. [Roadmap](#roadmap)
10. [Current Status](#current-status)
11. [Getting Started](#getting-started)
12. [Contributing](#contributing)
13. [License](#license)
14. [Author](#author)

---

## What is Review Dojo?

A *dojo* is a Japanese training hall, the place where people practice a skill again and again until it becomes second nature. **Review Dojo** is a training hall for one of the most important and least taught skills in software engineering: **code review**.

In a real software team, one developer writes code and a teammate reads it before it goes live, checking for bugs, security problems, and messy design. That reading and checking is called a code review. Review Dojo is like a training gym for the person doing the checking.

The platform shows you realistic code changes written by a pretend teammate. Hidden inside are planted flaws. Your job is to find them, explain them clearly, and get scored on how well you did.

---

## The Problem

Code review is a huge part of a professional developer's daily work, yet almost nobody is taught how to do it.

- **Universities teach writing code, not reading it.** Students graduate knowing how to build features but have never been trained to critique someone else's work.
- **New developers are expected to review code from day one.** Companies assume the skill already exists, and junior developers often learn it slowly, by trial and error, while real products are at stake.
- **Weak reviews are expensive.** Bugs and security holes that slip through a review reach production, where they cost far more to fix.
- **There is no safe place to practice.** Reviewing real company code is risky, and open source pull requests do not come with an answer key or a score.
- **Existing tools solve a different problem.** Popular tools such as AI reviewers and static analyzers review your code for you. They do not train *you* to become a better reviewer.

---

## The Solution

Review Dojo gives developers a safe, structured, and scored place to practice reviewing code.

- Realistic pull requests with **planted flaws** across bugs, security, performance, and design.
- A review interface that feels like the tools used in real teams.
- **Automatic scoring** based on what you caught, what you missed, and how useful your feedback was.
- **Clear explanations** for every flaw, so each exercise teaches something.
- **Progress tracking** that builds into a review skill score over time.

---

## Who Is It For?

| Audience | How Review Dojo helps |
| --- | --- |
| **Computer science and software engineering students** | Practice a skill that university courses rarely cover, before the first job. |
| **Junior developers** | Build confidence reviewing code and learn what experienced reviewers look for. |
| **Bootcamps and universities** | Add hands-on code review training to a curriculum. |
| **Job seekers** | Show employers a measurable review skill score. |
| **Mentors and team leads** | Use the exercises to train new team members. |

---

## How It Works

1. **Pick an exercise.** Choose a language and a difficulty level.
2. **Read the pull request.** You see a realistic code change, with a title, description, and the changed files.
3. **Leave review comments.** Click on lines of code and write comments, just like on GitHub.
4. **Submit your review.** Finish when you think you have found the problems.
5. **Get scored.** The platform compares your comments with the planted flaws.
6. **Learn from the results.** See which flaws you caught, which you missed, and an explanation of each one.
7. **Track your growth.** Your scores build into a profile that shows your strengths and weak spots.

---

## Planned Features

- [ ] Library of realistic pull request exercises
- [ ] Practice code in multiple languages: Python, JavaScript, Java, and SQL
- [ ] Flaw categories: logic bugs, security vulnerabilities, performance issues, readability, and design
- [ ] Inline commenting on lines of code
- [ ] Scoring engine that rates what you caught, what you missed, and false alarms
- [ ] Feedback quality rating: is your comment clear, specific, and kind?
- [ ] Detailed explanation for every planted flaw
- [ ] User accounts and progress tracking
- [ ] Review skill score and history
- [ ] Difficulty levels from beginner to advanced
- [ ] Leaderboard and achievements
- [ ] Tools for teachers to assign exercises to a class

---

## Tech Stack

| Layer | Technology | Why |
| --- | --- | --- |
| **Frontend** | TypeScript + React | Type-safe, component-based, and an industry standard for building interactive interfaces. |
| **Backend** | Python | Readable, fast to build with, and great for the scoring and analysis logic. |
| **Database** | PostgreSQL | A reliable relational database for users, exercises, flaws, and scores. |
| **Version control** | Git and GitHub | Collaboration, history, and project hosting. |

---

## Project Structure

```text
review-dojo/
├── frontend/     # TypeScript + React user interface
├── backend/      # Python API and scoring logic
├── docs/         # Design notes and documentation
├── LICENSE
└── README.md
```

---

## Roadmap

- [x] **Phase 0: Setup.** Create the repository and project structure.
- [ ] **Phase 1: Backend foundation.** Python API, database models, and the first exercise data.
- [ ] **Phase 2: Frontend foundation.** React app and the pull request viewer.
- [ ] **Phase 3: Review flow.** Inline commenting and review submission.
- [ ] **Phase 4: Scoring engine.** Compare reviews against planted flaws and generate feedback.
- [ ] **Phase 5: Accounts and progress.** Sign up, login, and skill tracking.
- [ ] **Phase 6: Content.** Build a library of exercises across languages and difficulty levels.
- [ ] **Phase 7: Deployment.** Put the platform live on the internet.
- [ ] **Phase 8: Launch.** Share it with students, universities, and the developer community.

---

## Current Status

> **Project setup is complete and development is starting.** The repository structure is in place, and the backend is the next milestone. This README will grow as the project does.

---

## Getting Started

The application is not ready to run yet. Setup instructions will be added here as soon as the first working version is available.

To follow the project, click **Watch** and **Star** at the top of this repository.

---

## Contributing

Contributions, ideas, and feedback are welcome once the first version is ready. For now, feel free to open an issue with suggestions.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Author

Built by a software engineering student at the University of Europe for Applied Sciences.

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,50:203a43,100:0f2027&height=120&section=footer" alt="footer wave" width="100%" />

</div>
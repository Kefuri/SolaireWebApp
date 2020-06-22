# Solaire

## The Turn-Based Strategy Game, Revisited! 

### About

Solaire was the name of the final project I built for my A-Level coursework in 2019. It covered user research, development frameworks and communicating with stakeholders to build an app meeting user requirements.

Despite not much time having passed since I finished this project, I've learned a lot from a software development standpoint, and I'd love to see what the project will become with my new skills.

### MVP
<img width="700" alt="Screenshot 2020-06-12 at 10 57 40" src="https://user-images.githubusercontent.com/41115973/84490799-9650af80-ac9b-11ea-9b9b-0cd9b00890a8.png">

A small brainstorming session using the knowledge vs priority grid has helped prioritize features I want to work on first.
Features like a login system and displaying assets on the web-app are features that are both high priority and I have a high knowledge of how to do them.
Meanwhile, a feature like moving health bars that are in coordination with the monster health points is a feature I have less knowledge of how to do, but also is not as high a priority for the final product.

### Database Structure

<img width="887" alt="Screenshot 2020-06-12 at 11 35 43" src="https://user-images.githubusercontent.com/41115973/84494164-e9793100-aca0-11ea-9542-faa1c55987a5.png">
The screenshot above displays the planned structure for tables that involve user management. This includes their login details and the teams they've built. Because a user can have many teams, and a team can have many monsters, a joining table called team monsters was required to hold which monsters are used in which team.

<img width="923" alt="Screenshot 2020-06-12 at 11 24 01" src="https://user-images.githubusercontent.com/41115973/84493942-8daea800-aca0-11ea-9add-1480526d968f.png">

When looking at the tables needed for monster information, a similar pattern arises. A monster will have many moves, and a move can be used on many monsters. Hence the use of a MonsterMoves table, which connects the two. 


## Local Deployment

Running the project locally will require a few steps of setting up.

1. Clone the repository locally

2. Ensure you have Python3 installed - you can find a guide to do so [here](https://docs.python-guide.org/starting/install3/osx/)

3. Navigate to ../SolaireDjango/Solaire

4. Run `python3 manage.py seed` to add data to the database. You can also use this command to clear the database, by running `python3 manage.py seed --mode clear`

## Dannie's Game

The need for Dannie's game arose on 4th January 2020 where my extended family couldn't all play "Dannie's game", named after my cousin Dannie, at the same time without one person needing to be quiz master.

I solved this with a simple python app on the day using my phone but I have decided to create a project using TDD and Django to make the solution available to my cousin and her family any time.

#### Is Django the best tool for the job?
Absolutely not. It is complete overkill but I wanted to use the TDD methodology to build a simple Django app from first principles, and this seemed like the perfect project in terms of scope. The methodology used in this is heavily inspired by Harry Percival's excellent book: Test-Driven Development with Python.

#### How does the game work?
* The game is played in a group. Each player submits a name of a person or fictional character to the quiz master.
* The quiz master then reads all the names out once, and only once.
* The youngest player then begins by addressing any one other player and says are you ___ ?
* If they are correct, the other player joins the youngest player's team and they question another person.
* If they are incorrect, the chance to ask a question moves to the player to whom the question was posed, and they ask another player a question.
* The game continues until everyone is one one big team.

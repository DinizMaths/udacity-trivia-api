# Backend - Trivia API

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

Create Environment Variables in Windows:

```bash
set FLASK_APP=flaskr
set FLASK_ENV=development
set DB_USER=YOUR_USER
set DB_PASSWORD=YOUR_PASS
set DB_HOST=localhost
set DB_PORT=5432
```

Remenber to replace `YOUR_USER` and `YOUR_PASS` with your Postgres username and password.

With Postgres running, create a `trivia` database:

```bash
createdb trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Documentation

### `GET /`

  Returns a json object with success message.

  ```json
  {
    "success": True,
    "message": "Welcome to the Trivia API!"
  }
  ```

### `GET /categories`
  
  Returns a json object with a list of categories.

  ```json
  {
    "success": True,
    "categories": {
      "1": "Science",
      "2": "Art",
      "3": "Geography",
      "4": "History",
      "5": "Entertainment",
      "6": "Sports"
    }
  }
  ```

### `GET /questions`

  Returns a json object with a list of questions, total number of questions, categories and current category.

  ```json
  {
    "success": True,
    "questions": [
      {
        "id": 1,
        "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
        "answer": "Apollo 13",
        "category": 5,
        "difficulty": 4
      },
      {
        "id": 2,
        "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?",
        "answer": "Tom Cruise",
        "category": 5,
        "difficulty": 4
      },
      ...
    ],
    "total_questions": 19,
    "categories": {
      "1": "Science",
      "2": "Art",
      "3": "Geography",
      "4": "History",
      "5": "Entertainment",
      "6": "Sports"
    },
    "current_category": None
  }
  ```

### `DELETE /questions/<int:question_id>`
    
  Deletes the question with the given id.

  Returns a json object with the id of the deleted question.

  ```json
  {
    "success": True,
    "message": "Question successfully deleted"
  }
  ```

### `POST /questions`

  Creates a new question.

  Returns a json object with the id of the created question.

  ```json
  {
    "success": True,
    "message": "Question successfully created"
  }
  ```

### `POST /questions/search`
  
  Searches for questions that contain the given search term.

  Returns a json object with a list of questions, total number of questions, categories and current category.

  ```json
  {
    "success": True,
    "questions": [
      {
        "id": 1,
        "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
        "answer": "Apollo 13",
        "category": 5,
        "difficulty": 4
      },
      {
        "id": 2,
        "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?",
        "answer": "Tom Cruise",
        "category": 5,
        "difficulty": 4
      },
      ...
    ],
    "total_questions": 19,
    "categories": {
      "1": "Science",
      "2": "Art",
      "3": "Geography",
      "4": "History",
      "5": "Entertainment",
      "6": "Sports"
    }
  }
  ```

### `GET /categories/<int:category_id>/questions`
  
  Returns a json object with a list of questions, total number of questions, categories and current category.

  ```json
  {
    "success": True,
    "questions": [
      {
        "id": 1,
        "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
        "answer": "Apollo 13",
        "category": 5,
        "difficulty": 4
      },
      {
        "id": 2,
        "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?",
        "answer": "Tom Cruise",
        "category": 5,
        "difficulty": 4
      },
      ...
    ],
    "total_questions": 19,
    "categories": {
      "1": "Science",
      "2": "Art",
      "3": "Geography",
      "4": "History",
      "5": "Entertainment",
      "6": "Sports"
    }
  }
  ```

### `POST /quizzes`
  
  Returns a json object with a random question from the given category.

  ```json
  {
    "success": True,
    "question": {
      "id": 1,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4
    }
  }
  ```

## Testing

To deploy the tests, run

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
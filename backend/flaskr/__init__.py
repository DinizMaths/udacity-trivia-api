import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import db, setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        """
        Set Access-Control-Allow
        """
        response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
        response.headers.add("Access-Control-Allow-Methods", "GET, POST, PATCH, DELETE, OPTIONS")

        return response
    
    @app.route("/categories")
    def get_categories():
        """
        Get all categories
        """
        categories = db.session.query(Category).all()
        formatted_categories = [category.format() for category in categories]

        if len(formatted_categories) == 0:
            abort(404)

        return jsonify({
            "success": True,
            "categories": formatted_categories
        })
    
    @app.route("/questions")
    def get_questions():
        """
        Get all questions
        """
        page = request.args.get("page", 1, type=int)
        start = (page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE

        questions = db.session.query(Question).all()
        formatted_questions = [question.format() for question in questions]
        categories = db.session.query(Category).all()
        formatted_categories = [category.format() for category in categories]

        if len(formatted_questions[start:end]) == 0:
            abort(404)

        return jsonify({
            "success": True,
            "questions": formatted_questions[start:end],
            "total_questions": len(formatted_questions),
            "categories": formatted_categories
        })
    
    @app.route("/questions/<int:question_id>", methods=["DELETE"])
    def delete_question(question_id):
        """
        Delete a question by id
        """
        question = db.session.query(Question).get(question_id)

        if question is None:
            abort(422)

        question.delete()

        return jsonify({
            "success": True,
            "message": "Question successfully deleted"
        })

    @app.route("/questions", methods=["POST"])
    def create_question():
        """
        Create a new question
        """
        data = request.get_json()

        if data["question"] is None or data["answer"] is None or data["difficulty"] is None or data["category"] is None:
            abort(422)

        question = Question(
            question=data["question"],
            answer=data["answer"],
            difficulty=data["difficulty"],
            category=data["category"]
        )

        question.insert()

        return jsonify({
            "success": True,
            "message": "Question successfully created"
        })
    
    @app.route("/questions/search", methods=["POST"])
    def search_questions():
        """
        Search questions by search term
        """
        data = request.get_json()
        search_term = data["searchTerm"]

        questions = db.session.query(Question).filter(Question.question.ilike(f"%{search_term}%")).all()
        formatted_questions = [question.format() for question in questions]

        if len(formatted_questions) == 0:
            abort(404)

        return jsonify({
            "success": True,
            "questions": formatted_questions,
            "total_questions": len(formatted_questions)
        })

    @app.route("/categories/<int:category_id>/questions")
    def get_questions_by_category(category_id):
        """
        Get questions by category id
        """
        questions = db.session.query(Question).filter(Question.category == category_id).all()
        formatted_questions = [question.format() for question in questions]

        if len(formatted_questions) == 0:
            abort(404)

        return jsonify({
            "success": True,
            "questions": formatted_questions,
            "total_questions": len(formatted_questions)
        })
    
    @app.route("/quizzes", methods=["POST"])
    def get_quiz_question():
        """
        Get a random question for a quiz
        """
        data = request.get_json()
        previous_questions = data["previous_questions"]
        quiz_category = data["quiz_category"]

        if quiz_category["id"] == 0:
            questions = db.session.query(Question).all()
        else:
            questions = db.session.query(Question).filter(Question.category == quiz_category["id"]).all()

        formatted_questions = [question.format() for question in questions]
        filtered_questions = [question for question in formatted_questions if question["id"] not in previous_questions]

        if len(filtered_questions) == 0:
            random_question = None
        else:
            random_question = random.choice(filtered_questions)

        if random_question is None:
            abort(404)

        return jsonify({
            "success": True,
            "question": random_question
        })
    
    @app.errorhandler(400)
    def bad_request(error):
        """
        Error handler for 400
        """
        return jsonify({
            "success": False,
            "message": "Bad request"
        }), 400
    
    @app.errorhandler(404)
    def not_found(error):
        """
        Error handler for 404
        """
        return jsonify({
            "success": False,
            "message": "Not found"
        }), 404
    
    @app.errorhandler(422)
    def unprocessable_entity(error):
        """
        Error handler for 422
        """
        return jsonify({
            "success": False,
            "message": "Unprocessable entity"
        }), 422
    
    @app.errorhandler(500)
    def internal_server_error(error):
        """
        Error handler for 500
        """
        return jsonify({
            "success": False,
            "message": "Internal server error"
        }), 500

    return app

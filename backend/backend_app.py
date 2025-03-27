from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initial hardcoded posts
POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


# Step 1 & 6: List Endpoint with optional sorting functionality
@app.route('/api/posts', methods=['GET'])
def get_posts():
    posts = POSTS.copy()

    # Optional sorting parameters
    sort_field = request.args.get('sort')
    direction = request.args.get('direction', 'asc')

    if sort_field:
        if sort_field not in ['title', 'content']:
            return jsonify({"error": "Invalid sort field. Must be 'title' or 'content'."}), 400
        if direction not in ['asc', 'desc']:
            return jsonify({"error": "Invalid sort direction. Must be 'asc' or 'desc'."}), 400

        reverse = True if direction == 'desc' else False
        posts.sort(key=lambda post: post.get(sort_field, ""), reverse=reverse)

    return jsonify(posts)


# Step 2: Add Endpoint
@app.route('/api/posts', methods=['POST'])
def add_post():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    title = data.get("title")
    content = data.get("content")

    missing_fields = []
    if title is None:
        missing_fields.append("title")
    if content is None:
        missing_fields.append("content")

    if missing_fields:
        return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

    # Generate a new unique id
    new_id = max([post["id"] for post in POSTS], default=0) + 1
    new_post = {"id": new_id, "title": title, "content": content}
    POSTS.append(new_post)
    return jsonify(new_post), 201


# Step 3: Delete Endpoint
@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global POSTS
    post = next((p for p in POSTS if p["id"] == post_id), None)
    if post is None:
        return jsonify({"error": f"Post with id {post_id} not found."}), 404
    POSTS = [p for p in POSTS if p["id"] != post_id]
    return jsonify({"message": f"Post with id {post_id} has been deleted successfully."}), 200


# Step 4: Update Endpoint
@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    post = next((p for p in POSTS if p["id"] == post_id), None)
    if post is None:
        return jsonify({"error": f"Post with id {post_id} not found."}), 404

    data = request.get_json()
    # Update fields only if provided; otherwise, keep the old values.
    title = data.get("title", post["title"])
    content = data.get("content", post["content"])

    post["title"] = title
    post["content"] = content

    return jsonify(post), 200


# Step 5: Search Endpoint
@app.route('/api/posts/search', methods=['GET'])
def search_posts():
    title_query = request.args.get("title", "").lower()
    content_query = request.args.get("content", "").lower()

    filtered_posts = []
    for post in POSTS:
        title_match = title_query in post["title"].lower() if title_query else True
        content_match = content_query in post["content"].lower() if content_query else True
        if title_match and content_match:
            filtered_posts.append(post)
    return jsonify(filtered_posts), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
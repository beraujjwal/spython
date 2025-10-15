from flask import jsonify




def register_error_handlers(app):
  @app.errorhandler(404)
  def not_found(e):
    return jsonify({'error': 'not found'}), 404


@app.errorhandler(Exception)
  def internal_error(e):
  app.logger.exception(e)
    return jsonify({'error': 'internal server error'}), 500
from myapp import create_app
import config

app = create_app(config)
if __name__ == '__main__':
  print app.name
  app.run(host='0.0.0.0', debug=True)

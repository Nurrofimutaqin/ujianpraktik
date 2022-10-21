from pyexpat import model
from flask import Flask, render_template, request, jsonify
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
from func import make_model

app = Flask(__name__)


dic = {0 : 'butterfly', 1 : 'cat', 2 : 'chicken', 3 : 'cow', 4 : 'dog', 5 : 'elephant', 6 : 'horse', 7 : 'sheep', 8 : 'spider', 9 : 'squirrel'}

model = make_model()
model.load_weights('model.h5')

model.make_predict_function()

def predict_label(img_path):
	i = image.load_img(img_path, target_size=(100,100))
	i = image.img_to_array(i)/255.0
	i = i.reshape(1, 100,100,3)
	prediction = model.predict_classes(i)
	return dic[prediction[0]]


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/api/deteksi", methods = ['GET','POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/uploads/" + img.filename	
		img.save(img_path)

		prediction = predict_label(img_path)

	# return render_template("index.html", prediction = prediction, img_path = img_path)
		return jsonify({
					"prediksi": prediction,
					"gambar_prediksi": img_path
				})
	else:
            # Return hasil prediksi dengan format JSON
            gambar_prediksi = '(none)'
            return jsonify({
                "prediksi": prediction,
                "gambar_prediksi": img_path
            })


if __name__ =='__main__':
	#app.debug = True
	app.run(host="localhost", port=5000, debug = True)
from flask import Flask, request, json
import requests

app = Flask(__name__)

@app.before_request
def before_request():
	if request.path != '/account':
		if request.method == 'POST':
			r = requests.post('https://api.silentclient.net' + request.path, data=request.data)
		elif request.method == 'GET':
			r = requests.get('https://api.silentclient.net' + request.path)
		elif request.method == 'PUT':
			r = requests.put('https://api.silentclient.net' + request.path, data=request.data)
		elif request.method == 'DELETE':
			r = requests.delete('https://api.silentclient.net' + request.path)
		print(request.path)
		print(r.text)
		return r.text
	
@app.route('/account', methods=['GET'])
def account():
	resp = app.response_class(
		response = '{"errors":null,"account":{"id":333,"username":"dutixlf","cosmetics":{"capes":[{"id":48,"texture":"/assets/textures/cosmetics/capes/48/0.png","name":"Telegram Cape","price":1,"sale_price":1,"normal_price":1,"category":"Silent Client","preview":"/assets/preview/capes/telegram_cape.png","created_at":"2023-02-27T17:09:48.000+03:00","updated_at":"2023-03-15T19:42:44.000+03:00","is_private":1,"is_animated":0,"frames":1,"frame_delay":150,"partner_id":null},{"id":45,"texture":"/assets/textures/cosmetics/capes/45","name":"Lampa Cape","price":129,"sale_price":129,"normal_price":129,"category":"Lampa","preview":"/assets/preview/capes/lampa_cape.png","created_at":"2023-02-23T20:16:30.000+03:00","updated_at":"2023-03-15T19:42:44.000+03:00","is_private":0,"is_animated":1,"frames":6,"frame_delay":60,"partner_id":203},{"id":67,"texture":"/assets/textures/cosmetics/capes/67","name":"Lampa Cape v2","price":129,"sale_price":129,"normal_price":129,"category":"Lampa","preview":"/assets/preview/capes/lampa_cape_v2.png","created_at":"2023-03-25T21:20:12.000+03:00","updated_at":"2023-03-25T21:20:12.000+03:00","is_private":0,"is_animated":1,"frames":20,"frame_delay":150,"partner_id":203},{"id":69,"texture":"/assets/textures/cosmetics/capes/69","name":"Zekich Cape v3","price":129,"sale_price":129,"normal_price":129,"category":"Zekich","preview":"/assets/preview/capes/zekich_cape_v3.png","created_at":"2023-03-28T17:33:12.000+03:00","updated_at":"2023-03-28T17:33:12.000+03:00","is_private":0,"is_animated":1,"frames":15,"frame_delay":150,"partner_id":110},{"id":36,"texture":"/assets/textures/cosmetics/capes/36","name":"Klyrri Cape","price":129,"sale_price":129,"normal_price":129,"category":"Klyrri","preview":"/assets/preview/capes/klyrri_cape.png","created_at":"2023-02-20T00:23:45.000+03:00","updated_at":"2023-03-15T19:42:44.000+03:00","is_private":0,"is_animated":1,"frames":15,"frame_delay":100,"partner_id":34},{"id":70,"texture":"/assets/textures/cosmetics/capes/70","name":"Barfi Cape v3","price":129,"sale_price":129,"normal_price":129,"category":"Barfi","preview":"/assets/preview/capes/barfi_cape_v3.png","created_at":"2023-03-29T15:29:55.000+03:00","updated_at":"2023-03-29T15:29:55.000+03:00","is_private":0,"is_animated":1,"frames":16,"frame_delay":150,"partner_id":121}],"wings":[{"id":3,"texture":"/assets/textures/cosmetics/wings/3/0.png","name":"Black Glitched Wings","price":149,"sale_price":149,"normal_price":149,"category":"Silent Client","preview":"/assets/preview/wings/black_glitched_wings.png","created_at":"2023-02-20T00:56:32.000+03:00","updated_at":"2023-03-15T19:42:44.000+03:00","is_private":0,"partner_id":null},{"id":4,"texture":"/assets/textures/cosmetics/wings/4/0.png","name":"Orange Galaxy Wings","price":149,"sale_price":149,"normal_price":149,"category":"Silent Client","preview":"/assets/preview/wings/orange_galaxy_wings.png","created_at":"2023-02-21T04:33:12.000+03:00","updated_at":"2023-03-15T19:42:44.000+03:00","is_private":0,"partner_id":null}],"icons":[],"bandanas":[{"id":12,"texture":"/assets/textures/cosmetics/bandanas/12","name":"Mishq Bandana","price":99,"sale_price":99,"normal_price":99,"category":"mishq","preview":"/assets/preview/bandanas/mishq_bandana.png","is_animated":1,"frames":20,"frame_delay":71,"partner_id":2785,"created_at":"2023-04-02T17:11:08.000+03:00","updated_at":"2023-04-02T17:11:08.000+03:00","is_private":0},{"id":6,"texture":"/assets/textures/cosmetics/bandanas/6","name":"Error Bandana White","price":99,"sale_price":99,"normal_price":99,"category":"Silent Client","preview":"/assets/preview/bandanas/error_bandana_white.png","is_animated":1,"frames":15,"frame_delay":150,"partner_id":null,"created_at":"2023-03-26T08:26:04.000+03:00","updated_at":"2023-03-26T08:26:04.000+03:00","is_private":0}]},"selected_cape":69,"selected_wings":null,"is_admin":0,"remember_me_token":null,"created_at":"2023-02-21T19:18:32.000+03:00","updated_at":"2023-04-02T19:24:13.000+03:00","original_username":"dutixlf","email":"zahatema2016@ya.ru","selected_icon":0,"is_online":0,"last_online":"2023-04-02T19:02:09.000+03:00","is_plus":1,"plus_expiration":"2023-10-02T13:34:54.000+03:00","plus_icon":1,"custom_cape":0,"overvall_playtime":5799,"plus_icon_color":-8439583,"discord_id":null,"telegram_id":1062081089,"custom_skin":0,"skin_type":"default","is_partner":0,"partner_balance":0,"is_banned":0,"last_update":null,"selected_bandana":null,"cape_type":"dynamic_curved","cape_shoulders":1,"is_tester":1,"is_staff":0}}',
		status = 200,
		mimetype='application/json'
	)
	return resp

if __name__ == '__main__':
    app.run(host='api.silentclient.net', port='80', debug=True)

import bottle

@bottle.route("<filepath:path>")
def server_static(filepath):
    return bottle.static_file(filepath, root=".")

bottle.run(host='localhost', port=8080)
import json

users = {"demo": "pimpass"}       
stg = {}                           

def login(username: str, password: str):
    if username in users and users[username] == password:
        return json.dumps({"status": "ok", "user": username})
    else:
        return json.dumps({"status": "error", "message": "invalid credentials"})

def search_page(query: str):
    if not query:
        return json.dumps({"status": "error", "message": "query cannot be empty"})
    return json.dumps({"status": "ok", "query": query})

def in_place_viewer(title: str):
    rec = stg.get(title)
    if not rec:
        return json.dumps({"status": "error", "message": "not found"})
    return json.dumps({"status": "ok", "title": title, "preview": rec["body"][:50]})

def particle_viewer(title: str):
    rec = stg.get(title)
    if not rec:
        return json.dumps({"status": "error", "message": "not found"})
    return json.dumps({"status": "ok", "title": title, "body": rec["body"]})

def create_particle(user: str, cont: str):
    if user not in stg:
        stg[user] = {"title": user, "body": cont, "version": 1}
        return json.dumps({"status": "ok"})
    else:
        return json.dumps({"status": "error", "message": "title already exists"})

def edit_particle(phead: str, new_body: str):
    if phead in stg:
        stg[phead]["body"] = new_body
        stg[phead]["version"] += 1
        return json.dumps({"status": "ok"})
    else:
        return json.dumps({"status": "error", "message": "not found"})


if __name__ == "__main__":
    print("== Login ==")
    print(login("demo", "pimpass"))
    print(login("demo", "wrong"))

    print("\n== Create ==")
    print(create_particle("Gut Health", "Intro to microbiome."))
    print(create_particle("Gut Health", "Duplicate"))

    print("\n== Search ==")
    print(search_page("gut"))

    print("\n== In-place Viewer ==")
    print(in_place_viewer("Gut Health"))

    print("\n== Particle Viewer ==")
    print(particle_viewer("Gut Health"))

    print("\n== Edit ==")
    print(edit_particle("Gut Health", "Updated info."))
    print(particle_viewer("Gut Health"))
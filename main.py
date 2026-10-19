from pyscript import document

grade7 = {"Estelle Chavez", "Aaliyah Pardilla", "Ronald Saludar"}
grade8 = {"Erich Eligino", "Bella Moncupa", "Jibril Abdul"}
grade9 = {"Julia Ramos", "Orange Mendoza", "Christian Mnahan"}
grade10 = {"Vyelle Bunag", "Maiselle Marin", "Andrik David"}

all_members = grade7 | grade8 | grade9 | grade10

members_list = "<br>".join(sorted(all_members))
document.getElementById("members").innerHTML = members_list
document.getElementById("total").innerText = f"TOTAL MEMBERS: {len(all_members)}"

def add_member(event):
    global all_members

    first = document.getElementById("first").value.strip().title()
    last = document.getElementById("last").value.strip().title()

    new_member = first + " " + last

    all_members = all_members | {new_member}

    members_list = "<br>".join(sorted(all_members))
    document.getElementById("members").innerHTML = members_list
    document.getElementById("total").innerText = f"TOTAL MEMBERS: {len(all_members)}"

    document.getElementById("first").value = ""
    document.getElementById("last").value = ""

import tkinter as tk

# -----------------------------
# Personal Information
# -----------------------------

name = "Krutik Hirudkar"
age = 20
role1 = "Engineer"
role2 = "AI Systems Architect"
vision = "Building self-healing AI systems using logic and math"
philosophy = "Logical architecture is more important than prompt engineering"
music = "Synthwave"
food = "Pizza"

# -----------------------------
# App Setup
# -----------------------------

app = tk.Tk()
app.title("Krutik Hirudkar | Architect of Resilience")
app.geometry("1200x750")
app.configure(bg="#F5F5F0")

# Grid Configuration

for i in range(6):
    app.grid_columnconfigure(i, weight=1)

for i in range(4):
    app.grid_rowconfigure(i, weight=1)

# -----------------------------
# Helper Function
# -----------------------------

def card(parent, bg):
    return tk.Frame(parent, bg=bg, bd=2, relief="ridge")

# -----------------------------
# Hero Card
# -----------------------------

hero = card(app, "white")
hero.grid(row=0, column=0, columnspan=4, rowspan=2,
          padx=10, pady=10, sticky="nsew")

tk.Label(hero,
         text="Human / Engineer / India 🇮🇳",
         bg="white",
         font=("Arial", 14)).pack(anchor="w", padx=20, pady=10)

tk.Label(hero,
         text=f"{name}",
         bg="white",
         font=("Arial", 36, "bold"),
         justify="left").pack(anchor="w", padx=20)

tk.Label(hero,
         text="Architecting AI-native resilience for the future.\n"
              "Currently bridging logic, mathematics and AI systems.",
         bg="white",
         justify="left",
         font=("Arial", 15)).pack(anchor="w", padx=20, pady=20)

# -----------------------------
# Age Card
# -----------------------------

age_card = card(app, "#8B5CF6")
age_card.grid(row=0, column=4, columnspan=2,
              padx=10, pady=10, sticky="nsew")

tk.Label(age_card,
         text=str(age),
         bg="#8B5CF6",
         fg="white",
         font=("Arial", 52, "bold")).pack(expand=True)

tk.Label(age_card,
         text="Years of Growth",
         bg="#8B5CF6",
         fg="white",
         font=("Arial", 16, "bold")).pack(pady=15)

# -----------------------------
# Vision Card
# -----------------------------

vision_card = card(app, "white")
vision_card.grid(row=2, column=0, columnspan=3,
                 padx=10, pady=10, sticky="nsew")

tk.Label(vision_card,
         text="VISION 2026",
         bg="white",
         font=("Arial", 18, "bold")).pack(anchor="w", padx=20, pady=10)

tk.Label(vision_card,
         text=vision,
         bg="white",
         justify="left",
         wraplength=500,
         font=("Arial", 14)).pack(anchor="w", padx=20)

# -----------------------------
# Philosophy Card
# -----------------------------

philosophy_card = card(app, "white")
philosophy_card.grid(row=2, column=3, columnspan=3,
                     padx=10, pady=10, sticky="nsew")

tk.Label(philosophy_card,
         text="PHILOSOPHY",
         bg="white",
         font=("Arial", 18, "bold")).pack(anchor="w", padx=20, pady=10)

tk.Label(philosophy_card,
         text=f'"{philosophy}"',
         bg="white",
         justify="left",
         wraplength=500,
         font=("Arial", 14)).pack(anchor="w", padx=20)

# -----------------------------
# Music Card
# -----------------------------

music_card = card(app, "white")
music_card.grid(row=3, column=0, columnspan=2,
                padx=10, pady=10, sticky="nsew")

tk.Label(music_card,
         text="FLOW STATE",
         bg="white",
         font=("Arial", 18, "bold")).pack(anchor="w", padx=20, pady=10)

tk.Label(music_card,
         text="🎵 " + music,
         bg="white",
         font=("Arial", 20)).pack(anchor="w", padx=20)

# -----------------------------
# Food Card
# -----------------------------

food_card = card(app, "#FFF4E8")
food_card.grid(row=3, column=2, columnspan=2,
               padx=10, pady=10, sticky="nsew")

tk.Label(food_card,
         text="🍕",
         bg="#FFF4E8",
         font=("Arial", 50)).pack(pady=10)

tk.Label(food_card,
         text=food.upper(),
         bg="#FFF4E8",
         font=("Arial", 20, "bold")).pack()

# -----------------------------
# Roles Card
# -----------------------------

roles_card = card(app, "white")
roles_card.grid(row=3, column=4, columnspan=2,
                padx=10, pady=10, sticky="nsew")
tk.Label(roles_card,
         text="ROLES",
         bg="white",
         font=("Arial", 18, "bold")).pack(anchor="w", padx=20, pady=10)

tk.Label(roles_card,
         text=f"• {role1}\n• {role2}",
         bg="white",
         justify="left",
         font=("Arial", 15)).pack(anchor="w", padx=20)

# -----------------------------
# Run
# -----------------------------

app.mainloop()

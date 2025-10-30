class Korea:
    def speak(self):
        print("speak in Korean")

class Bangladesh:
    def speak(self):
        print("speak in Bangla")
def translation(people):
    people.speak()

k=Korea()
b=Bangladesh()

translation(k)
translation(b)
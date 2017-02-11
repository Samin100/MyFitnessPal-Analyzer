import User
import myfitnesspal

client = myfitnesspal.Client('samin100')

samin = User.User(client)

print(samin)
#Get instance
import instaloader
import stdiomask

L = instaloader.Instaloader()

#Login or load session
print("\n")
username = input("Input your instagram username: ")
# password = stdiomask.getpass(prompt="Input your instagram password: ", mask="X")
password = input("Input your instagram password: ")
L.login(username, password)  #(login)

print("\n")
print("Login to " + username + " account. . . . .")

#Save list
def save_list(data, filename):
    print("\n")
    save_aggrement = input("Do you want to save the " + filename + " list on a file.txt (y/n)? ")
    print("\n")
    if save_aggrement == "y":
        for x in data:
            file = open(username + "_" + filename + ".txt", "a+")
            file.write(x)
            file.write("\n")
            file.close()

#Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, username)

#Get list of followers
print("\n")
print("Getting the list of followers (people that follow). . . . .")

followers_list = []
for followers in profile.get_followers():
    followers_list.append(followers.username)
save_list(followers_list, "followers")

#Get list of followees
print("\n")
print("Getting the list of followees (people that followed). . . . .")

followees_list = []
for followees in profile.get_followees():
    followees_list.append(followees.username)
save_list(followees_list, "followees")

#Get list of unfollowers
print("\n")
print("Getting the list of unfollowers (people that followed, but not follow back). . . . .")

unfollowers_list = []
for followees in followees_list:
    if followees not in followers_list:
        unfollowers_list.append(followees)
save_list(unfollowers_list, "unfollowers")

#Get list of unfollowees
print("\n")
print("Getting the list of unfollowees (people that follow, but not followed back). . . . .")

unfollowees_list = []
for followers in followers_list:
    if followers not in followees_list:
        unfollowees_list.append(followers)
save_list(unfollowees_list, "unfollowees")

print("\n")
print("Number of Followers: " + str(len(followers_list)))
print("\n")
print("Number of Followees: " + str(len(followees_list)))
print("\n")
print("Number of Unfollowers: " + str(len(unfollowers_list)))
print("\n")
print("Number of Unfollowees: " + str(len(unfollowees_list)))
print("\n")

input("Press enter to close. . . . .")

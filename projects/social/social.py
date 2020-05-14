import random
from util import Stack, Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range (0, num_users):
            self.add_user(f'User {i}')
        # Create friendships
        # Generate all possible friendship combinations
        possible_friendships = []
        # Avoid duplicates by ensuring the first number is smaller than the second number by adding 1 to user_id as the beginning of the range in the nested for loop
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        #Shuffle the possible friendships to increase balance
        random.shuffle(possible_friendships)
        # Create frienships for the first X pairs of the list
        # X is determined by formula: num_users * avg_friendships // 2
        # Need to divide by 2 since each add_friendship() creates 2 friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    ##create get_friends helper function to use in get_all_social_paths below
    def get_friends(self, user_id):
        friends = self.friendships[user_id]
        return friends

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # self.last_id = 0
        # self.users = {}
        # self.friendships = {}
        # use self.friendships to extract needed data dictionary with integer, set as key, pair
        #first populate visited with user_id provided, we will search out all possible paths from there with bft
        #use Queue
        #also user_id is first element in all friendship paths
        q = Queue()
        q.enqueue([user_id])
        while q.size() > 0:
            ##dequeue first path and store as variable
            p = q.dequeue()
            ##check if last element of path in visited, and if not add both the key and value
            if p[-1] not in visited:
                visited[p[-1]] = p   
                ##find friends, add friends to paths
                friends = self.get_friends(p[-1])
                for friend in friends:
                    copy = p.copy()
                    copy.append(friend)
                    q.enqueue(copy)
                
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

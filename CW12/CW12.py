import json


class UserFiltering:
    def __init__(self, path) -> None:
        self.path = path
        self.file = None

    def __enter__(self):
        self.file = open(self.path, "r")
        self.data = json.load(self.file)
        return self._process_users(self.data)

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        return False

    def _process_users(self, users):
        categories = {"minor": [], "adult": [], "senior": []}

        for user in users:
            if "action" not in user or "age" not in user:
                continue
            if not user["action"]:
                continue
            try:
                age = int(user["age"])
            except (ValueError, TypeError):
                continue

            if age < 18:
                categories["minor"].append(user)
            elif 18 <= age <= 60:
                categories["adult"].append(user)
            else:
                categories["senior"].append(user)

        return categories


with UserFiltering("users.json") as result:
    print(result)

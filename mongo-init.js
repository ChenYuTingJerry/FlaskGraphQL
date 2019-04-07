db.createUser(
        {
            user: "shazam",
            pwd: "shazam",
            roles: [
                {
                    role: "readWrite",
                    db: "graphql"
                }
            ]
        }
);

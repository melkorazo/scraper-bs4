db.createUser(
    {
        user: "scraper",
        pwd: "scraperP4sw0rd",
        roles: [
            {
                role: "readWrite",
                db: "scraper"
            }
        ]
    }
)
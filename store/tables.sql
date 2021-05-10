CREATE TABLE "url_store" (
	"short_url"	TEXT PRIMARY KEY,
	"url"	TEXT NOT NULL,
	"user"	TEXT NULL,
	"created_datetime"	TEXT NOT NULL,
	"updated_datetime"	TEXT NULL
);

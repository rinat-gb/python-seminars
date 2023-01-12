BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "contacts" (
	"owner"	INTEGER NOT NULL,
	"phone"	INTEGER NOT NULL,
	"phone_type"	INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS "names" (
	"id"	INTEGER NOT NULL,
	"first_name"	TEXT,
	"mid_name"	TEXT,
	"last_name"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "phone_types" (
	"id"	INTEGER NOT NULL,
	"description"	TEXT
);
CREATE TABLE IF NOT EXISTS "phones" (
	"id"	INTEGER NOT NULL,
	"number"	TEXT
);
COMMIT;

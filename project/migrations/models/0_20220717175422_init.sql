-- upgrade --
CREATE TABLE IF NOT EXISTS "budget" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "month" INT NOT NULL,
    "year" INT NOT NULL,
    "amount" DECIMAL(9,2) NOT NULL,
    "user_id" BIGINT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);

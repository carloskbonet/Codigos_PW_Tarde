-- CreateTable
CREATE TABLE "genre" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "created_at" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" DATETIME NOT NULL
);

-- CreateTable
CREATE TABLE "_genreTomovie" (
    "A" INTEGER NOT NULL,
    "B" INTEGER NOT NULL,
    CONSTRAINT "_genreTomovie_A_fkey" FOREIGN KEY ("A") REFERENCES "genre" ("id") ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT "_genreTomovie_B_fkey" FOREIGN KEY ("B") REFERENCES "movie" ("id") ON DELETE CASCADE ON UPDATE CASCADE
);

-- CreateIndex
CREATE UNIQUE INDEX "genre_id_key" ON "genre"("id");

-- CreateIndex
CREATE UNIQUE INDEX "genre_name_key" ON "genre"("name");

-- CreateIndex
CREATE UNIQUE INDEX "_genreTomovie_AB_unique" ON "_genreTomovie"("A", "B");

-- CreateIndex
CREATE INDEX "_genreTomovie_B_index" ON "_genreTomovie"("B");

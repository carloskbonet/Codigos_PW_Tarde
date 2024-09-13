import { prisma } from "@/db";


// Criar
export async function createGenre(_name:string) {
    const genre = await prisma.genre.create({
        data: {
            name: _name
        }
    });

    return genre;
}

// Procurar
export async function findGenreByName(_name:string) {
    const genre = await prisma.genre.findUnique({
        where: {
            name: _name
        }
    });

    return genre;
}

// Listar
export async function selectGenres() {
    const genres = await prisma.genre.findMany();

    return genres;
}
import { prisma } from "@/db";

export async function createMovie(_name:string , _releaseDate: string, _genres: Array<number> , _imageURL: string , _videoURL: string, _description:string) {
    
    var connectGenres:Array<any> = [];

    _genres.map( genre => (

        connectGenres.push(
            {
                id: genre
            }
        )

    ) );
    
    
    const movie = await prisma.movie.create({
        data: {
            name: _name,
            releaseDate: _releaseDate,
            imageURL: _imageURL,
            videoURL: _videoURL,
            description: _description,
            genres: {
                connect: connectGenres
            }
        }
    });

    return movie;
}

export async function findMovieByName(_name:string) {
    const movie = await prisma.movie.findUnique({
        where: {
            name: _name
        },
        include: {
            ratings: {
                include: {
                    user: true
                }
            },
            genres: true
        }
    });

    return movie;
}

export async function selectMovies() {
    const movies = await prisma.movie.findMany();

    return movies;
}
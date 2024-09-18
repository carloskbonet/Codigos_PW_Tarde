import { createMovie , findMovieByName , selectMovies } from "../model/movie";
import { findGenreByName } from "../model/genre";


export async function createMovieC(_name:string , _releaseDate: string , _genres: Array<any> ,  _description:string,  _imageURL="" , _videoURL="") {
    try {
        const movieByName = await findMovieByName(_name);

        if ( movieByName != undefined ) {
            return { status: 400, message: 'Name already registered' };
        }

        var verifiedGenres = [];

        for ( let i=0; i < _genres.length; i ++ ) {
            let genreByName = await findGenreByName(_genres[i]);
            
            if ( genreByName == undefined ) {
                return { status: 404, message: 'Genre not found' };
            }

            verifiedGenres.push(genreByName.id);
        }

        const response = await createMovie(_name , _releaseDate, verifiedGenres , _imageURL , _videoURL , _description);

        return { status: 201, message: 'Movie created', data: response };
    }
    catch(err){
        return { status: 500, message: 'Something went wrong' };        
    }
}



export async function findMovieByNameC(name: string) {
    try {
        const movieByName = await findMovieByName(name);

        if ( movieByName == undefined) {
            return { status: 404, message: 'Movie not found' };
        }
        else {
            return { status: 200, message: 'Movie found', data: movieByName };
        }

    }
    catch (err) {
        return { status: 500, message: 'Something went wrong' };
    }
}



export async function selectMoviesC() {
    try {
        const movies = await selectMovies();

        return { status: 200, message: 'Select movies', data: movies };
    }
    catch(err){
        return { status: 500, message: 'Something went wrong' };
    }
}
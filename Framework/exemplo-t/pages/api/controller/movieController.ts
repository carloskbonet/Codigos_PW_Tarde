import { createMovie , findMovieByName } from "../model/movie";


export async function createMovieC(_name:string , _releaseDate: string , _description:string,  _imageURL="" , _videoURL="") {
    try {
        const movieByName = await findMovieByName(_name);

        if ( movieByName != undefined ) {
            return { status: 404, message: 'Name already registered' };
        }

        const response = await createMovie(_name , _releaseDate , _imageURL , _videoURL , _description);

        return { status: 201, message: 'Movie created', data: response };
    }
    catch(err){
        return { status: 500, message: 'Something went wrong' };        
    }
}
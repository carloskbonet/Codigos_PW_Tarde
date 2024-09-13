import { createGenre , findGenreByName, selectGenres } from "../model/genre";

export async function createGenreC(_name:string) {
    try {

        // Verificações para a criação
        const genreByName = await findGenreByName(_name);

        if ( genreByName != undefined ) {
            return { status: 400, message: 'Genre already registered' };
        }

        const response = await createGenre(_name);

        return { status: 201, message: 'Genre created', data: response };

    }
    catch (err) {
        return { status: 500, message: 'Something went wrong' };
    }
}



export async function selectGenresC() {
    try {
        const response = await selectGenres();

        return { status: 200, message: 'Select genres', data: response };

    }
    catch (err) {
        return { status: 500, message: 'Something went wrong' };
    }
}
import { NextApiRequest , NextApiResponse } from "next";
import { createMovieC } from "../../controller/movieController";

export default async ( req:NextApiRequest , res:NextApiResponse ) => {
    if ( req.method != 'POST' ) {
        return res.status(405).json({ message: 'Method not allowed' });
    }

    const { name , releaseDate , imageURL , videoURL , description , genres } = req.body;

    // Enviar para o controller
    const response = await createMovieC(name , releaseDate , genres , description , imageURL , videoURL);

    return res.status(response.status).json( { message: response.message } );
}
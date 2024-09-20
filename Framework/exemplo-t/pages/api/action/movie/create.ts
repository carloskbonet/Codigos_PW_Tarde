import { NextApiRequest , NextApiResponse } from "next";
import { createMovieC } from "../../controller/movieController";
import { movieRequest } from "@/request/movieRequest";

export default async ( req:NextApiRequest , res:NextApiResponse ) => {
    if ( req.method != 'POST' ) {
        return res.status(405).json({ message: 'Method not allowed' });
    }

    const { name , releaseDate , imageURL , videoURL , description , genres } = req.body;

    const checkRequest = movieRequest(name , releaseDate , videoURL , description);

    if ( checkRequest.response == false ) {
        return res.status(400).json( { message: checkRequest.message } );
    }

    // Enviar para o controller
    const response = await createMovieC(name , releaseDate , genres , description , imageURL , videoURL);

    return res.status(response.status).json( { message: response.message } );
}
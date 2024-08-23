import { NextApiRequest , NextApiResponse } from "next";
import { createMovieC } from "../../controller/movieController";

export default async ( req:NextApiRequest , res:NextApiResponse ) => {
    if ( req.method != 'POST' ) {
        return res.status(403).json({ message: 'Method not allowed' });
    }

    const { name , releaseDate , imageURL , videoURL , description } = req.body;

    // Enviar para o controller
    const response = await createMovieC(name , releaseDate , description , imageURL , videoURL);

    console.log(response);

    return res.status(response.status).json(response.message);
}
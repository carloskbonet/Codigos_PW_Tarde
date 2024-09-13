import { NextApiRequest , NextApiResponse } from "next";
import { createGenreC } from "../../controller/genreController";

export default async ( req:NextApiRequest , res:NextApiResponse ) => {
    if ( req.method != 'POST' ) {
        return res.status(405).json({ message: 'Method not allowed' });
    }

    const { name } = req.body;
    
    // Enviar para o controller
    const response = await createGenreC(name);

    return res.status(response.status).json( { message: response.message } );
}
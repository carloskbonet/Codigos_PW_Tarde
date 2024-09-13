import { NextApiRequest , NextApiResponse } from "next";
import { selectGenresC } from "../../controller/genreController";

export default async ( req:NextApiRequest , res:NextApiResponse ) => {
    if ( req.method != 'GET' ) {
        return res.status(405).json({ message: 'Method not allowed' });
    }

    // Enviar para o controller
    const response = await selectGenresC();


    return res.status(response.status).json( { message: response.message , data: response.data } );
}
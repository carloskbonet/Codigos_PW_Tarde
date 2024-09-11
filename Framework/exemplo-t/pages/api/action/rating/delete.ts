import { NextApiRequest , NextApiResponse } from "next";
import { deleteRating } from "../../controller/ratingController";

export default async ( req:NextApiRequest , res:NextApiResponse ) => {
    if ( req.method != 'DELETE' ) {
        return res.status(405).json({ message: 'Method not allowed' });
    }

    const { email , moviename } = req.body;

    // Enviar para o controller
    const response = await deleteRating(email , moviename);

    return res.status(response.status).json( { message: response.message } );
}
import { NextApiRequest , NextApiResponse } from "next";
import { createUserC } from "../../controller/userController";

export default async ( req:NextApiRequest , res:NextApiResponse ) => {
    if ( req.method != 'POST' ) {
        return res.status(403).json({ message: 'Method not allowed' });
    }

    const { name , email , username , password , cPassword } = req.body;

    // Enviar para o controller
    const response = await createUserC(name , email , username , password , cPassword);

    return res.status(response.status).json(response.message);
}
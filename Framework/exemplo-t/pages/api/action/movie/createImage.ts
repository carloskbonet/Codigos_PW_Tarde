import { NextApiRequest , NextApiResponse } from "next";
import { getImage } from '@/utils/formidable'
import { uploadImage } from '@/utils/cloudinary'

export const config = {
    api: {
        bodyParser: false,
    }
}

export default async ( req:NextApiRequest , res:NextApiResponse ) => {
    if ( req.method != 'POST' ) {
        return res.status(403).json({ message: 'Method not allowed' });
    }

    // Recebe um arquivo e verifica se é uma imagem
    const image = await getImage(req);
    
    if ( !image ) {
        return res.status(404).json({ message: 'Cant handle this file' });
    }

    // Enviar a imagem para o site
    const imgData = await uploadImage(image[0].filepath);

    return res.status(200).json(imgData);
}
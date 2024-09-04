import { prisma } from "@/db";


export async function createRatingModel( _value:number , _comment:string , _userId:number , _movieId:number ) {
    const rating = await prisma.rating.create({
        data: {
            value: _value,
            comment: _comment,
            user: {
                connect: {
                    id: _userId
                }
            },
            movie: {
                connect: {
                    id: _movieId
                }
            }
        }
    });

    return rating;
}
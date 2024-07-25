import { prisma } from "@/db";

export async function createUser(_name:string , _email:string , _username:string , _password:string) {
    const user = await prisma.user.create({
        data: {
            name: _name , 
            email: _email ,
            username: _username ,
            password: _password
        }
    });


    return user;
}


export async function findUserByEmail(_email:string) {
    const user = await prisma.user.findUnique({
        where: {
            email: _email
        }
    });

    return user;
}

export async function findUserByUsername(_username:string) {
    const user = await prisma.user.findUnique({
        where: {
            username: _username
        }
    });

    return user;
}
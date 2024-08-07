import Head from "next/head";
import Link from "next/link";
import styles from '@/styles/register.module.css';
import { useState } from "react";
import { getCookie } from "cookies-next";
import { checkToken } from "@/services/tokenConfig";
import { useRouter } from "next/router";

export default function Register() {
    const router = useRouter();

    const [ formData , setFormData ] = useState(
    {
        name: "",
	    email: "",
	    username: "",
	    password: "",
	    cPassword: ""
    }
    
    );

    function handleFormEdit(event:any , field:string) {
        setFormData({
            ...formData,
            [field]: event.target.value
        });
    }

    async function formSubmit(event:any) {
        event.preventDefault();

        try {
            const response = await fetch(`/api/action/user/create` , {
                method: 'POST',
                headers: { 'Content-type':'application/json' },
                body: JSON.stringify(formData)
            });

            const responseJson = await response.json();

            alert(`${responseJson}`);

            if ( response.status == 201 ) {
                router.push(`/user/login`);
            }

        }
        catch (err) {
            console.log(err);
        }

    }


    return (
        <main id={styles.mainContainer} className='flex min-h-screen flex-col'>
            <Head>
                <title> Cadastro </title>
            </Head>

            <div className={styles.image}>
            </div>

            <div>
                <h1 className={styles.text} >Página de Cadastro</h1>

                <form className={styles.container} onSubmit={formSubmit}>

                    <input className={styles.input} type="text" placeholder="Nome (Opcional)" onChange={(event) => {handleFormEdit(event , 'name')}}  /><br />
                    <input className={styles.input} type="email" placeholder="Email" onChange={(event) => {handleFormEdit(event , 'email')}} /><br />
                    <input className={styles.input} type="text" placeholder="Nome de Usuário" onChange={(event) => {handleFormEdit(event , 'username')}} /><br />
                    <input className={styles.input} type="password" placeholder="Senha" onChange={(event) => {handleFormEdit(event , 'password')}} /><br />
                    <input className={styles.input} type="password" placeholder="Confirmação de Senha" onChange={(event) => {handleFormEdit(event , 'cPassword')}} /><br />

                    <input className={styles.sendBtn} type="submit" value="Criar Conta" />


                    <br /><br />
                    <Link href={`/user/login`}>Já tenho uma conta</Link>

                </form>
            </div>

        </main>
    );
}

export function getServerSideProps( { req , res }:any ) {
    try {
        const token = getCookie('authorization' , {req , res});

        if ( !token ) {
            throw new Error('Invalid Token');
        }
        else {
            checkToken(token);
        }

        return {
            redirect: {
                permanent: false,
                destination: '/'
            },
            props: {}
        }

    }
    catch(err){
        return {
            props: {}
        }
    }
}
import Head from "next/head";
import styles from "@/styles/login.module.css";

export default function Login() {
    
    return (
        <main>
            <Head>
                <title>Login</title>
            </Head>

            <form>
                <input type="text" placeholder="Login" />
                <input type="text" placeholder="Senha" />

                <input type="submit" value="Entrar" />
            </form>


        </main>
    );
}
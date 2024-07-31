import Head from "next/head";
import styles from "@/styles/login.module.css";

export default function Login() {

    return (
        <main id={styles.mainContainer} className='flex min-h-screen flex-col'>
            <Head>
                <title>Login</title>
            </Head>

            <div className={styles.image}>
            </div>

            <div>
                <h1 className={styles.text} >Página de Login</h1>
                <form className={styles.container}>
                    <input className={styles.input} type="text" placeholder="Login" /><br />
                    <input className={styles.input} type="text" placeholder="Senha" /><br />

                    <input className={styles.sendBtn} type="submit" value="Entrar" />
                </form>
            </div>


        </main>
    );
}
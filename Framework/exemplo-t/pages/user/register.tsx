import Head from "next/head";
import styles from '@/styles/register.module.css';

export default function Register() {

    return (
        <main id={styles.mainContainer} className='flex min-h-screen flex-col'>
            <Head>
                <title> Cadastro </title>
            </Head>

            <div className={styles.image}>
            </div>

            <div>
                <h1 className={styles.text} >Página de Cadastro</h1>

                <form className={styles.container}>

                    <input className={styles.input} type="text" placeholder="Nome (Opcional)" /><br />
                    <input className={styles.input} type="email" placeholder="Email" /><br />
                    <input className={styles.input} type="text" placeholder="Nome de Usuário" /><br />
                    <input className={styles.input} type="password" placeholder="Senha" /><br />
                    <input className={styles.input} type="password" placeholder="Confirmação de Senha" /><br />

                    <input className={styles.sendBtn} type="submit" value="Criar Conta" />

                </form>
            </div>

        </main>
    );
}
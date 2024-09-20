import styles from "@/styles/components/navbar.module.css";
import { deleteCookie } from "cookies-next";
import Link from "next/link";
import { useRouter } from "next/router";
import { PropsWithChildren } from "react";

export default function Navbar( {children} : PropsWithChildren ) {
    const router = useRouter();

    function logOut() {
        deleteCookie('authorization');
        router.push(`/user/login`);
    }


    function iconClick() {
        router.push(`/`);
        //router.reload();
    }

    return (

        <nav className={styles.navBar} >
            <img src="/pipoca.png" className={styles.icon} alt="" onClick={iconClick} />

            {children}

            <Link href={`/movie/create`} className={styles.createMovie}>Criar Filme</Link>
            <button className={styles.logoutBtn} onClick={logOut} >Logout</button>
        </nav >
    );
}
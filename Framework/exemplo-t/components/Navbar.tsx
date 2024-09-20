import Link from "next/link";
import React from "react";
import styles from "@/styles/home.module.css"
import { useRouter } from "next/router";
import { deleteCookie } from "cookies-next";

export default function Navbar() {

    const router = useRouter();

    function iconClick() {
        router.push(`/`);
    }


    function logOut() {
        deleteCookie('authorization');
        router.push(`/user/login`);
    }

    return (
        <nav className={styles.navBar}>
            <img onClick={iconClick} src="/pipoca.png" className={styles.icon} alt="" />




            <Link href={`/movie/create`} className={styles.createMovie}>Criar Filme</Link>
            <button className={styles.logoutBtn} onClick={logOut}>Logout</button>


        </nav>
    );
};
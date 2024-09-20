import { PropsWithChildren } from "react";
import Navbar from "./Navbar";

export default function Layout( {children} : PropsWithChildren ) {

    return (
        <>
            <Navbar></Navbar>
            <div className="container">

                {children}

            </div>
        </>
    );
}
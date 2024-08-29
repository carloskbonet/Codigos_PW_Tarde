import { checkToken } from "@/services/tokenConfig";
import { deleteCookie, getCookie } from "cookies-next";
import styles from "@/styles/home.module.css"
import { useState, useEffect } from "react";
import Link from "next/link";
import { useRouter } from "next/router";

export default function Home() {
  const router = useRouter();
  const [data, setData]: any = useState(undefined);

  async function fetchData() {
    try {
      const response = await fetch(`/api/action/movie/select`, {
        method: 'GET'
      });

      const responseJson = await response.json();

      setData(responseJson.data);
    }
    catch (err) {
      console.log(err);
    }
  }

  useEffect(() => {
    fetchData();
  }, [])

  function logOut() {
    deleteCookie('authorization');
    router.push(`/user/login`);
  }

  function movieClick(movieName: string) {
    router.push(`/movie/` + movieName);
  }


  return (
    <main id={styles.main} className="flex min-h-screen flex-col">

      {/* Barra superior de navegação */}
      <nav className={styles.navBar}>
        <img src="/pipoca.png" className={styles.icon} alt="" />

        <div className={styles.searchContainer}>
          <input type="text" className={styles.searchBar} />
          <button className={styles.send}>Enviar</button>
        </div>


        <Link href={`/movie/create`} className={styles.createMovie}>Criar Filme</Link>
        <button className={styles.logoutBtn} onClick={logOut}>Logout</button>


      </nav>

      {/* Container principal. Ele vai conter o GRID */}
      <div className={styles.mainContainer}>

        {/* Painel esquerdo */}
        <div className={styles.leftContainer}>

        </div>

        {/* Painel direito */}
        <div className={styles.rightContainer}>

          {data != undefined && data instanceof Array ?

            data.map(movie => (
              <div onClick={() => { movieClick(movie.name) }} className={styles.card}>
                <img src={movie.imageURL} className={styles.cardImg} alt="" />
                <div className={styles.cardInfos}>
                  <h2>{movie.name}</h2>
                  <p>{movie.releaseDate}</p>
                  <p>Generos do Filme</p>
                  <p>{movie.description}</p>
                </div>
              </div>
            ))

            :

            <p>No movies Found</p>

          }


        </div>

      </div>

    </main>
  );
}



export function getServerSideProps({ req, res }: any) {
  try {
    const token = getCookie('authorization', { req, res });

    if (!token) {
      throw new Error('Invalid Token');
    }
    else {
      checkToken(token);
    }

    return {
      props: {}
    }

  }
  catch (err) {
    return {
      redirect: {
        permanent: false,
        destination: '/user/login'
      },
      props: {}
    }
  }
}